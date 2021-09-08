# Purpose           : This program gets a ZIP code and ISO 3166 Country codefrom the user
#                     and displays the weather forecast for 5 days with data every 3 hours via a API call to OpenWeatherMap.
#                     The programs lets the user run the program multiple times to allow them to look up weather conditions
#                     for multiple locations, or can choose to exit.

# Assignment Number : 12.1
# Author            : Tinto T. Kurian

import requests, datetime    # Importing request and datetime


api_key = '8e8f5511a2221772afe57d087b2503b3'        # This is the API Key received by registering with OpenWeatherMap
base_url = 'http://api.openweathermap.org/data/2.5/forecast?'   # This is the base URL, additional parameters are added further in the program


# the below function makes a call to the API URL and gets the response in JSON.
# Appropriate try/exception blocks are created to catch the exceptions.
def api_call():
    units, represent = get_unit_type()  #calls the get_unit_type function and assigns the output to variables
    while True:
        try:
            response = requests.get(create_url(represent)).json()         # Makes get request to url and converts it to JSON
            if response['cod'] == '404':                                  # If the response code is 404, displays City not found error
                raise Exception('City not found, Please check the data you entered and try again')
            if response['cod'] == '400':                                  # If the response code is 400, displays Invalid zip code error
                raise Exception('Invalid zip code, Please check the data you entered and try again')
        except Exception as e:
            print(e)
        else:
            # return response
             return response, units


# Below function gets the response of the API call and the user chosen unit
# for temperature and displays the output in a readable format.
# also converts the time to local time of the location by applying the offset.
def format_output(data, units):
    print('\n\n\nYou have chosen {0} City of {1}'.format(data['city']['name'], data['city']['country']))
    print('The city geo location is latitude: {} and longitude: {}'.format(data['city']['coord']['lat'],data['city']['coord']['lon']))
    # print('The UTC - GMT Offset of the location is {} Seconds'.format(data['city']['timezone']))
    offset = data['city']['timezone']
    count = data['cnt']
    for index in range(count):                      # Loops thru all the index of the list and prints the results
        date_time = datetime.datetime.strptime(data['list'][index]['dt_txt'], '%Y-%m-%d %H:%M:%S')  # Converts the dt_txt to date time
        date_with_offset = date_time + datetime.timedelta(seconds=offset)                           # Applies the offset to convert the UTC time to local time of the location
        print('\n\n\tAt local time {0} in {1},{2}'.format(date_with_offset,data['city']['name'], data['city']['country']))
        print('\t\t\tThe temperate : {} {}'.format(data['list'][index]['main']['temp'], units))
        print('\t\t\tThe Minimum temperate : {} {}'.format(data['list'][index]['main']['temp_min'], units))
        print('\t\t\tThe Maximum temperate : {} {}'.format(data['list'][index]['main']['temp_max'], units))
        print('\t\t\tAtmospheric pressure on the sea level by default : {} hPa'.format(data['list'][index]['main']['pressure']))
        print('\t\t\tAtmospheric pressure on the sea level {} hPa'.format(data['list'][index]['main']['sea_level']))
        print('\t\t\tAtmospheric pressure on the ground level {} hPa'.format(data['list'][index]['main']['grnd_level']))
        print('\t\t\tHumidity : {} %'.format(data['list'][index]['main']['humidity']))

        print('\t\t\tThe Weather condition : {0}, with {1}'.format(data['list'][0]['weather'][0]['main'], data['list'][0]['weather'][0]['description']))

        print('\t\t\tCloudiness {} % '.format(data['list'][index]['clouds']['all']))
        print('\t\t\tWind speed : {0} in {1} degrees (meteorological)'.format(data['list'][index]['wind']['speed'],data['list'][index]['wind']['deg']))
        if 'rain' in data['list']:                                                                          # Gets the actual value only if "rain" key exist" else displays default message
            print('\t\t\tRain volume for last 3 hours : {} mm '.format(data['list'][index]['rain']['3h']))
        else:
            print('\t\t\tThere is no rain in the forecast.')
        if 'snow' in data['list']:                                                                          # Gets the actual value only if "snow" key exist" else displays default message
            print('Snow volume for last 3 hours : {}'.format(data['list'][index]['snow']['3h']))
        else:
            print('\t\t\tThere id no snow in the forecast.')



# Below function displays welcome message to the user
def welcome_message():
    print('\n\n{}'.format('*' * 100))
    print('Hi... Here you can get the weather forecast for 5 days with data every 3 hours by providing the zip code\n')
    print('{}'.format('*' * 100))


# The below function gets the ZIP Code and ISO 3166 Country code of the location
# of which the user wants to see the weather forcast.
def get_zip():
    try:
        zip = int(input('\nEnter the ZIP code of the place you want the weather for :\n'))
        country = str(input('\nEnter "Y" if the Country is US\nelse\nEnter the ISO 3166 Country code of the Country\n')).lower()
        if country == 'y':                              # sets the country as US if the user enters "y"
            country_cd = 'us'
        else:
            country_cd = country
    except ValueError:
        print('\nPlease only enter integer for ZIP and string for country code')
    except Exception as e:
        print(e)
    else:
        zip = str(zip)
        return zip, country_cd


# The below program lets the user choose between Fahrenheit, Celsius and Kelvin as a unit of temperature
def get_unit_type():
    units = ''
    represent = ''
    while True:
        try:
            print('Please enter which unit you want the temperatures to be displayed')
            input_int = int(input('Enter \n1 for Fahrenheit,\n2 for Celsius or \n3 for Kelvin\n'))
            if input_int not in [1, 2, 3]:                                      # Checks if the user have inputted anything other than the given options.
                raise Exception('Please only enter 1, 2 or 3 to choose the unit correctly')
            if input_int == 1:
                represent = '&units=imperial'
                units = 'Fahrenheit'
            elif input_int == 2:
                represent = '&units=metric'
                units = 'Celsius'
            elif input_int == 3:
                represent = ''
                units = 'Kelvin'
        except ValueError:
            print('\nPlease only enter 1, 2 or 3 to choose the unit correctly')
        except Exception as e:
            print(e)

        else:
            return units,represent


# The below function uses all the inputs to create the URL with all the parameters
def create_url(represent):
    zipc , ctry_code = get_zip()
    zipcode = 'zip='+ zipc
    url = base_url + zipcode + ','+ctry_code+'&APPID=' + api_key + represent
    return url

# Below function allows the user to call the program to get the forecast of another city as long as he/she enters "y"
def more():
    while True:
        try:
            yes_more = str(input('\nPlease enter "Y" if you want to continue to get the weather forecast of another city' 
                                 ' \nOR\nEnter any other key to finish exit\n')).lower()          # we convert the user input to lower.
        except Exception as e:
            print(e)
        else:
            return yes_more

# This is the main function which calls all the other functions.
def main():
    try:
        welcome_message()
        # print(api_call())
        data, units = api_call()
        format_output(data, units)
        while more() == 'y':                    # Checks if the user entered "y" to enter another city.
            data, units = api_call()
            format_output(data, units)
    except Exception as e:
        print(e)
    else:
        pass
    finally:
        print('\nThe program have ended')  # Lets the user know the program have ended.

if __name__ == '__main__':
    main()

