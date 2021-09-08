# Purpose           : This program makes a GET call to the Chuck Norris Jokes API and lets the user read jokes.
#                     The user can continue to ask for more jokes till user decides to terminate.
# Assignment Number : 10.1
# Author            : Tinto T. Kurian


import requests     # Importing request
import json         # ImPorting JSON


url = "https://api.chucknorris.io/jokes/random"     # the link to the AIP is stored in the url variable.

# Below function makes a GET request to the url and converts it into JSON
# and then returns just the Joke from the response of the API
def api_call():
    try:
        response = requests.get(url).json()         # Makes get request to url and converts it to JSON
    except Exception as e:
        print(e)
    else:
        # return('\n\nChuck Norris Joke: {}\n'.format(response['value']))     # From the JSON fetches onnly the value of the Key "value"
        return response
# The below functions asks if the user wants to hear more Jokes, the user can enter "Y" or "y" as we convert the imput to lower anyway
# The user can enter any other key to end the program
def more_jokes():
    while True:
        try:
            yes_more = str(input('\nPlease enter "Y" if you want to hear another Chuck Norris Joke'
                                 ' \nOR\nEnter any other key to terminate\n')).lower()          # we convert the user input to lower.
        except Exception as e:
            print(e)
        else:
            return yes_more

# The below function displays a welcome message for the user.
def welcome_user():
    print('\n\n{}'.format('*'*100))
    print('Welcome user, here you are read as much Chuck Norris jokes as you would like to\nLaughter is the best medicine')
    print('{}'.format('*' * 100))


# Below id the main function which calls all other functions.
def main():
    try:
        welcome_user()                      # Calls welcome_user() function and displays a welcome message
        print(api_call())                   # call api_call() functions and prints the return, which is the joke
        while more_jokes() == 'y':          # Checks if the user input is 'y'( remember we converted the user input to lower)
            print(api_call())               # keeps printing new jokes till the user input is not equal to 'y'
    except Exception as e:
        print(e)
    else:
        pass
    finally:
        print('The program have ended')     # Lets the user know the program have ended.


if __name__ == '__main__':
    main()