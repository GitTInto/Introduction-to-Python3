# def get_unit_type():
#     units = ''
#     represent = ''
#     while True:
#         try:
#             print('Please enter which unit you want the temperatures to be displayed')
#             input_int = int(input('Enter \n1 for Fahrenheit,\n2 for Celsius or \n3 for Kelvin\n'))
#             if input_int not in [1, 2, 3]:
#                 raise Exception('Please only enter 1, 2 or 3 to choose the unit correctly')
#             if input_int == 1:
#                 represent = '&units=imperial'
#                 units = 'Fahrenheit'
#             elif input_int == 2:
#                 represent = '&units=metric'
#                 units = 'Celsius'
#             elif input_int == 3:
#                 represent = ''
#                 units = 'Kelvin'
#         except Exception as e:
#             print(e)
#         else:
#             return units,represent
#
#
#
#
# units, represent = get_unit_type()
# # print(get_unit_type())
# print(units)
# print(represent)

import datetime
# timestamp = datetime.datetime.fromtimestamp(1500000000)
# print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))

inta = int(-25200)
# timestamp = datetime.datetime.fromtimestamp(25200)
# print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))

print(datetime.now() - timedelta(seconds=inta))