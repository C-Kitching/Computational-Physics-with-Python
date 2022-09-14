# HEADER
# Name: Christopher Kitching
# Email: christopher.kitching@postgrad.macnhester.ac.uk
# Date created: 14/09/22
# Date last edited: 14/09/22
# Description: 

# IMPORTS
import numpy as np
import matplotlib.pyplot as plt

def get_height_user():
    """Get initial height of the ball from the user and validate it as a
       number greater than 0

    Returns:
        height (float): initial height of the ball
    """

    # assume invalid input
    valid_input = False

    # continuously ask for input while invalid
    while not valid_input:

        # ask user for input
        height = input("Please input the initial ball height:")
        
        # check if input is number greater than 0
        try:
            value = float(height)
            if value >= 0:
                break
            else: 
                print("Error: please input a number greater than 0")
        except:
            print("Error: please input a number")

    return height

def get_efficincy_user():
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
        efficiency = input("Please input the initial ball height:")
        
        # check if input is number between 0 and 1
        try:
            value = float(efficiency)
            if 0 <= value <= 1:
                break
            else: 
                print("Error: please input a number between 0 and 1")
        except:
            print("Error: please input a number")

    return efficiency

def main():
    """Main function
    """

    # get problem parameters from the user
    initial_height = get_height_user()
    efficiency = get_efficincy_user()




# header guard
if __name__ == "__main__":
    main()