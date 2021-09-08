# Purpose           : Below is a creating a simple cash register program which keeps adding asm many items as user wants into the shopping cart,
#                     adds the price of each item added and finally prints the total price and the number of the items in the cart.
# Assignment Number : 11.1
# Author            : Tinto T. Kurian


import locale   # imports locale
locale.setlocale(locale.LC_ALL, 'en_US.utf-8') # sets the locale to US English utf8.

# Below we creat a class and define one init method and one instance method called additem.
class CashRegister:
    num_of_items = 0    # Initialised the value of class variable num_of_items to zero

    def __init__(self, item_code):  # In this init method we define a attribute item_code for the class
        self.item_code = item_code

    def additem(self, price): # In this instance method we define a attribute price for the class.
        self.price = price
        CashRegister.num_of_items += 1  # Each time a new instance calls this method to add price the value of num_of_num_of_items increments by one.
        


# Below codes defines a function which creates an instance of the class CashRegister,
# get the item code from the user and
# gets the cost of that item from the user, keeps prompting the user to enter a proper float value as the price.
def addcart():
    purchase_instance = 0
    purchase_instance = CashRegister(input('Please enter the item code\n'))  # Gets the item code from the user and creates an instance of CashRegister class
    while True:
        try:
            purchase_instance.additem(float(input('Please enter the price of the item in USD\n'))) # Gets the price from the user and creates an instance of CashRegister class
        except ValueError:
            print('Invalid input....Please enter a float value as the price of the item\n')
        except Exception as e:
            print(e)
        else:
            return purchase_instance.price


# Below function displays welcome message to the user
def welcome_message():
    print('\n\n{}'.format('*' * 100))
    print('Hi... Welcome to amazing shopping experience\nPlease start adding items to your cart for purchasing\n')
    print('{}'.format('*' * 100))


# The below functions prompts the user to see if they like to add more items to the cart,
# they can enter 'Y' or 'y' to continue of use any other ket to terminate.
def more_purchase():
    while True:
        try:
            yes_more = str(input('\nPlease enter "Y" if you want to continue to add items to the cart'
                                 ' \nOR\nEnter any other key to finish shopping and to exit\n')).lower()          # we convert the user input to lower.
        except Exception as e:
            print(e)
        else:
            return yes_more

# Below function gets the total price as the input and displays the price after converting it to locate currency type, in this case $.
def getTotal(totalprice):
    print('\n\n\nThe total Price is: {}'.format(locale.currency(totalprice, grouping=True)))

# Below function prints the total count of the items in the cart.
def getCount():
    print('\nThe total number of items in your cart is: {}'. format(CashRegister.num_of_items))


# Below id the main function which calls all other functions.
def main():
    try:
        welcome_message()   # calls function welcome_message
        sum = addcart()     # calls functions addcart and assigns the price value to the variable sum
        while more_purchase() == 'y':   # Calls function more_purchase to see if the user want to add more items
            sum = sum + addcart()       # Keeps calling addcart till the user wants and keeps adding the price to the sum
        getTotal(sum)                   # Calls the function getTotal
        getCount()                      # Calls the function getCount
    except Exception as e:
        print(e)
    else:
        pass
    finally:
        print('\nThe program have ended')     # Lets the user know the program have ended.


if __name__ == '__main__':
    main()
