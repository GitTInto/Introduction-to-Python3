# Purpose           : This program perform various calculations
#                     (addition, subtraction, multiplication, division, and average calculation)
#                     based on user inputted choice of operations.
#                     The user also chooses the numbers on which the operations are done.
# Assignment Number : 5.1
# Author            : Tinto T. Kurian


# This function gets the math operation that the user whats use,
# and prompts user to enter one of the displayed options if the user input is not in the list of allowed operations
# and returns the user chosen math operator.
def captureOperation():
    operations = ['+', '-', '*', '/', 'avg']    # This is the list of allowed operations
    while True:
        print('What math operation would you like to perform\nEnter one of the below '
                '\n\tEnter + for Addition'
                '\n\tEnter - for Subtraction'
                '\n\tEnter * for Multiplication'
                '\n\tEnter / for Division'
                '\n\tEnter avg for Average\n')
        useroperation = input()
        if useroperation in operations:
            return useroperation
            break
        else:
            print('Not a valid input, Please enter a valid operation from the list displayed\n')


# This function gets numbers to be operated on as input from the user
# and validates for correct entry and prompts the user again in-case of invalid entries
# and returns the number entered by the user.
def captureNumbers():
    while True:
        try:
            usernumber = float(input('Please enter a number :\n'))
            return usernumber
            break
        except ValueError:
            print('Not a valid input, Please enter a valid number\n')

# This function does the math operations (+,-,*,/) on use inputted two numbers
# and prints the numbers,the operator and the result.
def performCalculation(calcoperator):
    num1 = captureNumbers()
    print('Your first number is :{}'.format(num1))
    num2 = captureNumbers()
    print('Your second number is :{}'.format(num2))
    if calcoperator == '+':  # does addition if + is the chosen operator
        outputofcalc = num1 + num2
    elif calcoperator == '-':  # does subtraction if - is the chosen operator
        outputofcalc = num1 - num2
    elif calcoperator == '*':   # does multiplication if * is the chosen operator
        outputofcalc = num1 * num2
    elif calcoperator == '/':   # does division if / is the chosen operatoer
        while True:
            try:
                outputofcalc = num1 / num2
                break
            # Prompts the user to enter a different second number,if the user entered 0 and caused zero division error.
            except ZeroDivisionError:
                print('You Cannot divide a number by Zero, Enter another second number\n')
                num2 = captureNumbers()
# below line prints the result
    print('\n\nYour result \n\t {0}{1}{2}={3}\n'.format(num1,calcoperator,num2,outputofcalc))


# The below function gets how many numbers the user wants tio find average of
# and then prompts the user to enter that many numbers
# then calculates the average of those numbers and prints the numbers and result(average).
def calculateAverage():
    listofnumbers=[]    # initializing listofnumbers
    sumofnumber=0.0     # initializing sumofnumber
    while True:
        try:
            while True:
                numofnumbers = int(input('Please enter for how many numbers you want to find average of  :\n'))
# Below like makes sure that the user enters a positive integer value for the count
# of the numbers for this average has to be calculated.
                if numofnumbers > 0:
                    break
                else:
                    print('The number of numbers for which you want to calculate average should be greater than 0\n')
            break
        except ValueError:
            print('Not a valid input, Please enter a valid number\n')

    for i in range(numofnumbers):   # loop that iterates as many number of times as the count of numbers.
        newnum = captureNumbers()
        listofnumbers.append(newnum)    # keeps appending the list with the user entered numbers.
        sumofnumber=sumofnumber + newnum    # Keeps calculating the sum of the user entered numbers.
# Below line prints the list of numbers and the average of those numbers.
    print('The average of the numbers {0} is {1}'.format(listofnumbers, sumofnumber/numofnumbers))


# The below functions lets the user continue till the user choose to enter N for terminating the program.
# the user can enter any other key than N to keep continuing.
def wouldYouContinue():
    print('\n\n\nDo you want to continue,\n\t Enter N to terminate\n\t Or Enter any other key to continue\n')
    if input().upper() == 'N':
        return False
    else:
        return True

# The main function which call all the other functions
def main():
    shallcontinue = wouldYouContinue()  # Gets the answer for "if the user want to continue"
    while shallcontinue == True:
        useroperation = captureOperation()  # Gets the calculation operation.
        if useroperation == 'avg':  # Calls the calculateAverage() function is the operation chosen is avg.
            calculateAverage()
        else:
# Calls the performCalculation() function is any other operation(+,-,*,/) is chosen
            performCalculation(useroperation)
        shallcontinue = wouldYouContinue()


if __name__ == '__main__':
    main()