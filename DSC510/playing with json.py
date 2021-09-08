import json, re
from pprint import pprint

#json_file='a.json'
json_file = './5daysResult.json'
# cube='1'
correct_json={}

with open(json_file) as f:
    data = json.load(f)

# json_data = open(json_file)
# data = json.loads(json_data)
#pprint(data)
# print(data)
print(json.dumps(data, indent=2))


# print(count)


def format_output():
    print('You have chosen {0} City of {1}'.format(data['city']['name'], data['city']['country']))
    print('The city geo location is latitude: {} and longitude: {}'.format(data['city']['coord']['lat'],data['city']['coord']['lon']))
    print('The time of the location is {} Seconds'.format(data['city']['timezone']))
    count = data['cnt']
    for index in range(count):
        # print(index)
        print('\n\n\tAt {}'.format(data['list'][index]['dt_txt']))
        print('\t\tThe temperate : {}'.format(data['list'][index]['main']['temp']))
        print('\t\tThe Minimum temperate : {}'.format(data['list'][index]['main']['temp_min']))
        print('\t\tThe Maximum temperate : {}'.format(data['list'][index]['main']['temp_max']))
        print('\t\tAtmospheric pressure on the sea level by default : {} hPa'.format(data['list'][index]['main']['pressure']))
        print('\t\tAtmospheric pressure on the sea level {} hPa'.format(data['list'][index]['main']['sea_level']))
        print('\t\tAtmospheric pressure on the ground level {} hPa'.format(data['list'][index]['main']['grnd_level']))
        print('\t\tHumidity : {} %'.format(data['list'][index]['main']['humidity']))
         # dont chnage the weather index
        print('\t\tThe Weather condition : {0}, with {1}'.format(data['list'][0]['weather'][0]['main'], data['list'][0]['weather'][0]['description']))

        print('\t\tCloudiness {} % '.format(data['list'][index]['clouds']['all']))
        print('\t\tWind speed : {0} in {1} degrees (meteorological)'.format(data['list'][index]['wind']['speed'],data['list'][index]['wind']['deg']))
        # print('Rain volume for last 3 hours : {} mm '.format(data['list'][index]['rain']['3h']))
        # print('Snow volume for last 3 hours : {}'.format(data['list'][index]['snow']['3h']))


# print(data['list'][0]['weather']['description'])

# print('You have entered the zip code of  {0} City of {1}'.format(data['city']['name'], data['country']))
# print('')
# json_data.close()

# print "Dimension: ", data['cubes'][cube]['dim']
# print "Measures:  ", data['cubes'][cube]['meas']

format_output()