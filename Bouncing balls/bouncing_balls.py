# HEADER
# Name: Christopher Kitching
# Email: christopher.kitching@postgrad.macnhester.ac.uk
# Date created: 14/09/22
# Date last edited: 16/09/22
# Description: A program to determine the number of bounces made by a ball,
#              above some minimum height of interest, when dropped from an 
#              initial height. The efficiency of the bounces and the
#              gravitational constant are specified by the user. The user has
#              the option to input their own grav constant or can select from 
#              a series of predermined ones. All edge cases handled such as
#              perfect efficinecy. In the case of sensible parameters an 
#              animated graph has been drawn to display the trajectory.

# IMPORTS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

class Experiment:
    """Class to handle each experiment

    Attributes:
        h_min (float): minimum height of interest
        h_initial (float): initial height of the ball
        g (float): gravitational constant
        efficiency (float): efficiency of each bounce

    Methods:
        get_height_user(): get height value from user
        get_grav_constant_user(): get g from the user
        get_efficiency(): get efficiency from the user
        results(): print results of the experiment
        solve(): solve experiment 
    """

    def __init__(self):
        """Constructs the object
        """
        self.h_min = Experiment.get_height_user(True, False)
        self.h_initial = Experiment.get_height_user(False, True)
        self.g = Experiment.get_grav_constant_user()
        self.efficiency = Experiment.get_efficiency_user()

    def get_grav_constant_user():
        """Get the gravitational constant from the user

        Returns:
            float: gravitational constant
        """

        # ask user whether they want a custom g or to choose a planet
        custom_or_planet = input("Would you like a custom gravitational"\
                                 " constant or to choose a planet?:")
        while(custom_or_planet != 'custom' and custom_or_planet != 'planet'):
            custom_or_planet = input("Error: please input 'custom' or"\
                                     " \'planet':")

        # get custom grav constant
        if custom_or_planet == 'custom':

            # assume invalid input
            valid_input = False

            # continuously ask for input while invalid
            while not valid_input:

                # ask user for input
                grav_constant = input("Please input g(m/s^2):")
                
                # check if input is number greater than 0
                try:
                    value = float(grav_constant)
                    if value > 0:
                        return value
                    else: 
                        print("Error: please input a number greater than 0")
                except:
                    print("Error: please input a number")

        # get planet specific grav constant
        else:

            # create a dictionary of planets
            planet_dict = {'Mercury':3.59, 'Venus':8.87, 'Earth': 9.81, 
                        'Moon': 1.62, 'Mars': 3.77, 'Jupiter': 25.95,
                        'Saturn': 11.08, 'Uranus': 10.67, 'Neptune': 14.07,
                        'Pluto': 0.42, 'Sun': 274.13}
            
            # get user to select a valid planet
            print(planet_dict)
            planet = input("Please select a body from the list above:")
            while planet not in planet_dict:
                print("ERROR: that body does not exist")
                planet = input("Please select a body from the list above:")

            # return corresponding grav constant
            return planet_dict[planet]


    def get_height_user(min, initial):
        """Get height from the user and validate it as a number greater than 0

        Args:
            min (bool): requesting minimum height
            initial (bool): requesting initial height

        Returns:
            height (float): initial height or minimum height
        """

        # assume invalid input
        valid_input = False

        # continuously ask for input while invalid
        while not valid_input:

            # ask user for input
            if initial: height = input("Please input the initial ball height:")
            elif min: height = input("Please input the minimum height:")
            
            # check if input is number greater than 0
            try:
                value = float(height)
                if value >= 0:
                    return value
                else: 
                    print("Error: please input a number greater than or equal \
                        to 0" )
            except:
                print("Error: please input a number")

    def get_efficiency_user():
        """Get efficiency from the user and validate it as a number between 
        0 and 1  

        Returns:
            efficiency (float): efficiency of the bounces
        """

        # assume invalid input
        valid_input = False

        # continuously ask for input while invalid
        while not valid_input:

            # ask user for input
            efficiency = input("Please input the efficiency:")
            
            # check if input is number between 0 and 1
            try:
                value = float(efficiency)
                if 0 <= value <= 1:
                    return value
                else: 
                    print("Error: please input a number between 0 and 1")
            except:
                print("Error: please input a number")

    def results(self, bounces, time_taken):
        """Print results

        Args:
            bounces (int): number of bounces
            time_taken (float): time taken
        """
        # print results
        print("\nRESULTS")
        print("The initial height of the ball was {}m".format(self.h_initial))
        print("The minimum height of interest was {}m".format(self.h_min))
        print("The efficiency of each bounce was {}".format(self.efficiency))
        print("The number of bounces was {}".format(bounces))
        if self.efficiency != 1:
            print("The time taken was {:.2f}s".format(time_taken))
        else:
            print("The time taken was {}".format(time_taken))

    def solve(self):
        """Solve the experiment
        """

        # handle edege cases
        if self.h_initial == 0:
            bounces = 0
            time_taken = 0
            self.results(bounces, time_taken)
        elif self.h_min == 0:
            bounces = 'infinite'
            time_taken = (np.sqrt(2*self.h_initial/self.g)
                          *(1+np.sqrt(self.efficiency))
                          /(1-np.sqrt(self.efficiency)))
            self.results(bounces, time_taken)
        elif self.h_min >= self.h_initial:
            bounces = 0
            time_taken = np.sqrt(2*self.h_initial/self.g)
            self.results(bounces, time_taken)
        elif self.efficiency == 1:
            bounces = 'infinite'
            time_taken = 'infinite'
            self.results(bounces, time_taken)
        
        # regular case
        else:

            # set bounce counter to 0
            bounces = 0

            # account for initial drop
            time_taken = np.sqrt(2*self.h_initial/self.g)

            # determine height of first bounce
            h = self.h_initial*self.efficiency

            # while bounces are greater than h_min, append time and increment 
            # counter
            while h > self.h_min:
                time_taken += 2*np.sqrt(2*h/self.g)
                bounces += 1
                h *= self.efficiency

            # print final results
            self.results(bounces, time_taken)

        # get trajectory
        heights, times = self.trajectory()

        # plot trajectory
        self.plot_trajectory(heights, times)


    def trajectory(self):
        """Calculate the trajectory of ball

        Returns:
            heights (float[]): heights of the ball
            times (float[]): corresponding times
        """

        # number of data points per half bounce
        points_per_bounce = 10

        # calculate initial drop
        t = np.sqrt(2*self.h_initial/self.g)
        times = np.linspace(0, t, points_per_bounce, endpoint = True)
        heights = self.h_initial - 1/2*self.g*times**2

        # determine height of first bounce
        h = self.h_initial*self.efficiency

        # calc trajectory until we fall below h_min
        while h > self.h_min:

            # time to fall from new height
            t_fall = np.sqrt(2*h/self.g)
            times_temp = np.linspace(0, t_fall, points_per_bounce)

            # calculate height trajectories
            fall_heights = h - 1/2*self.g*times_temp**2
            rise_heights = np.flip(fall_heights)
            arc_heights = np.concatenate((rise_heights, fall_heights))

            # store height and time data
            heights = np.concatenate((heights, arc_heights))
            t_new = t + 2*t_fall
            times = np.concatenate((times, np.linspace(t, t_new, 
                                    2*points_per_bounce)))

            # update time and height
            t = t_new
            h *= self.efficiency

        return heights, times

    def plot_trajectory(self, heights, times):
        """Plot an animated trajectory of the ball until it falls below 
           h_min

        Args:
            heights (float[]): heights of the ball over the trajectory
            times (float[]): corresponding times
        """

        # set up graph
        fig = plt.figure()
        ax = fig.add_subplot(111)

        def animate(i):
            """animate the graph

            Args:
                i (int): position in the animation
            """
            ax.clear() # clear the plot
            ax.scatter(times[0], heights[0], color = 'green', 
                       label = 'Initial position') # initial position
            ax.scatter(times[-1], heights[-1], color = 'red', 
                       label = 'Final position') # final position        
            ax.hlines(self.h_min, times[0], times[-1], 
                      label = r'$h_{min}$', linestyle = '--', 
                      color = 'r') # min height
            ax.set_xlabel("Time")
            ax.set_ylabel("Heights")
            ax.set_ylim(0, self.h_initial + 1)
            ax.legend()
            ax.plot(times[:i], heights[:i], color = 'b') # animated part

        # animate
        anim = animation.FuncAnimation(fig, animate, frames = len(times) + 1,
                                        interval = 1, blit = False)
        
        # show graph
        plt.show()

def main():
    """Main function
    """
    # create experiment object and solve
    experiment1 = Experiment()
    experiment1.solve()

# header guard
if __name__ == "__main__":
    main()