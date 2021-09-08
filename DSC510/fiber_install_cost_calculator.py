# Purpose           : In this file a function cost is defined which takes two input parameters (feet and price),
#                     calculates the cost of installation and returns the cost of installation,
#                     the function defined here will be called from other files.
# Assignment Number : 4.1
# Author            : Tinto T. Kurian

def cost(num_of_feet, cost_per_feet):
    cost_of_installation = round(num_of_feet * cost_per_feet, 2) # multiples the number of feet with the cost per feet and rounds off by 3
    return cost_of_installation