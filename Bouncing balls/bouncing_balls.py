# HEADER
# Name: Christopher Kitching
# Email: christopher.kitching@postgrad.macnhester.ac.uk
# Date created: 14/09/22
# Date last edited: 14/09/22
# Description: 

# IMPORTS
import numpy as np
import matplotlib.pyplot as plt

def get_grav_constant_user():

    # ask user whether they want a custom g or to choose a planet
    custom_or_planet = input("Would you like a custom gravitational constant"\
                             " or to choose a planet?:")
    while custom_or_planet != 'custom' and custom_or_planet != 'planet':
        custom_or_planet = input("Error: please input 'custom' or 'planet':")

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
                if value >= 0:
                    return value
                else: 
                    print("Error: please input a positive number")
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

def results(h_min, h_initial, efficiency, bounces, time_taken):
    """Print results

    Args:
        h_min (float): minimum height of interest
        h_initial (float): initial height of the ball
        efficiency (float): efficiency of each bounce
        bounces (int): number of bounces
        time_taken (float): time taken
    """
    # print results
    print("\nRESULTS")
    print("The initial height of the ball was {}m".format(h_initial))
    print("The minimum height of interest was {}m".format(h_min))
    print("The efficiency of each bounce was {}".format(efficiency))
    print("The number of bounces was {}".format(bounces))
    if efficiency != 1:
        print("The time taken was {:.2f}s".format(time_taken))
    else:
        print("The time taken was {}s".format(time_taken))
        
def edge_cases(h_min, h_initial, efficiency, g):
    """Handle edge cases

    Args:
        h_min (float): minimum height of interest
        h_initial (float): initial ball height
        efficiency (float): efficiency of each bounce
        g (float): gravitational constant
    """

    if h_initial == 0:
        bounces = 0
        time_taken = 0
        results(h_min, h_initial, efficiency, bounces, time_taken)
    elif h_min == 0:
        bounces = 'infinite'
        time_taken = (np.sqrt(2*h_initial/g)*(1+np.sqrt(efficiency))
                      /(1-np.sqrt(efficiency)))
        results(h_min, h_initial, efficiency, bounces, time_taken)
    elif h_min >= h_initial:
        bounces = 0
        time_taken = np.sqrt(2*h_initial/g)
        results(h_min, h_initial, efficiency, bounces, time_taken)
    elif efficiency == 1:
        bounces = 'infinite'
        time_taken = 'infinite'
        results(h_min, h_initial, efficiency, bounces, time_taken)

def regular_cases(h_min, h_initial, efficiency, g):
    """Handle regular cases

    Args:
        h_min (float): minimum height of interest
        h_initial (float): initial ball height
        efficiency (float): efficiency of each bounce
        g (float): gravitational constant
    """

    # set bounce counter to 0
    bounces = 0

    # account for initial drop
    time_taken = np.sqrt(2*h_initial/g)

    # determine height of first bounce
    h = h_initial*efficiency

    # while bounces are greater than h_min, append time and increment counter
    while h > h_min:
        time_taken += 2*np.sqrt(2*h/g)
        bounces += 1
        h *= efficiency

    # print final results
    results(h_min, h_initial, efficiency, bounces, time_taken)

def main():
    """Main function
    """

    # set gravitational constant
    g = 9.8

    # get problem parameters from the user
    h_initial = get_height_user(False, True)
    h_min = get_height_user(True, False)
    efficiency = get_efficiency_user()
    grav_constant = get_grav_constant_user()

    # solve problem
    edge_cases(h_min, h_initial, efficiency, g)
    regular_cases(h_min, h_initial, efficiency, g)

    



# header guard
if __name__ == "__main__":
    main()