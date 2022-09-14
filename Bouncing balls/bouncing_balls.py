# HEADER
# Name: Christopher Kitching
# Email: christopher.kitching@postgrad.macnhester.ac.uk
# Date created: 14/09/22
# Date last edited: 14/09/22
# Description: 

# IMPORTS
import numpy as np
import matplotlib.pyplot as plt

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
                print("Error: please input a number greater than 0")
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

def results(h_min, h_initial, bounces, time_taken):
    """Print results

    Args:
        h_min (float): minimum height of interest
        h_initial (float): initial height of the ball
        bounces (int): number of bounces
        time_taken (float): time taken
    """
    # print results
    print("The initial height of the ball was {}".format(h_initial))
    print("The minimum height of interest was {}".format(h_min))
    print("The number of bounces was {}".format(bounces))
    print("The time taken was {}".format(time_taken))


def main():
    """Main function
    """
    
    # set gravitational constant
    g = 9.8

    # get problem parameters from the user
    h_initial = get_height_user(False, True)
    h_min = get_height_user(True, False)
    efficiency = get_efficiency_user()

    # handle edge cases
    if h_initial == 0:
        bounces = 0
        time_taken = 0
        results(h_min, h_initial, bounces, time_taken)
    elif h_min == 0:
        bounces = 'infinite'
        time_taken = (np.sqrt(2*h_initial/g)*(1+np.sqrt(efficiency))
                      /(1-np.sqrt(efficiency)))
        results(h_min, h_initial, bounces, time_taken)
    elif h_min >= h_initial:
        bounces = 0
        time_taken = np.sqrt(2*h_initial/g)
        results(h_min, h_initial, bounces, time_taken)





# header guard
if __name__ == "__main__":
    main()