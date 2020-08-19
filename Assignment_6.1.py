# Purpose           : This program gets the temperatures from the user till the user enters a sentinel value
#                     and determine the number of temperatures in the program,
#                     determine the largest temperature, and the smallest temperature and prints them.
# Assignment Number : 6.1
# Author            : Tinto T. Kurian


# The below functions lets the user continue till the user choose to enter N for terminating the program.
# the user can enter any other key than N to keep continuing.
def wouldYouContinue():
    print('\n\n\nDo you want to continue,\n\t Enter N to terminate\n\t Or Enter any other key to continue\n')
    if input().upper() == 'N':
        return False
    else:
        return True


temperatures = []  # Defining the empty list called temperatures.


# The below function get the temperatures from the user and appends it to the list temperatures
# the While True, try and except makes sure the user inputted value is float,
# prompts the user otherwise to enter a new value.
def captureTemp():
    while True:
        try:
            usertemp = float(input('Enter the temperature:\n'))
            temperatures.append(usertemp)
            break
        except ValueError:
            print('Not a valid input, Please enter a valid number\n')


# The below function finds the Maximum temperature and prints it.
def findMax():
    print('The Maximum temperature is: {}'.format(max(temperatures)))


# The below function finds the Minimum temperature and prints it.
def findMin():
    print('The Minimum temperature is: {}'.format(min(temperatures)))


# The below function finds the number of temperatures in the list and print it and the list.
def findCount():
    print('The number of Temperatures is {} in list of {} '.format(len(temperatures), temperatures))


# The main function which call all the other functions, loops thru till the sentinel value is False
# and then continues to call other functions.
def main():
    sentinelvalue = wouldYouContinue()
    while sentinelvalue is True:
        captureTemp()
        sentinelvalue = wouldYouContinue()
    findMax()
    findMin()
    findCount()


if __name__ == '__main__':
    main()
