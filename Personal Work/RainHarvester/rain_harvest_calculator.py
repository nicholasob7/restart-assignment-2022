''' a program to calculate rain harvesting across three variables,
requires 2 of the three variables to calculate'''

import math

print('Greetings from on High Rain Harvester!!!')
# client wishes to calculate 1 rain harvesting variable using 2 defined variables.
operation = str(input('Please choose a variable you wish to calculate,\n' + 
'litres captured = l, millimetres rainfall = mm, metres square of effective catchment = m2:\n'))
print(operation)

#client knows catchment area in metres square, rain event in millimetres
if operation == 'l':
    metres_square_catchment = int(input('Please enter the harvesting area in metres square.\n' +
    'Use numbers only with no decimal places:\n'))
    millimetres_rain_event = int(input('Please enter the rain event in millimetres:\n' +
    'Use numbers only with no decimal places. \n'))
    print('{} * {} = '.format(metres_square_catchment, millimetres_rain_event))
    result = metres_square_catchment * millimetres_rain_event
    print (('Congratulations you have harvested, ' + str(result) + ' litres!'))

#client knows litres captured in rain event, 
#catchment area in metres square
elif operation == 'mm':
    litres_captured_rain_event = int(input('Please enter the amount of increase in litres:\n' + 
    'Use numbers only with no decimal places.\n'))
    metres_square_catchment = int(input('Please enter the harvesting area in metres square.\n' +
    'Use numbers only with no decimal places:\n'))
    print('{} / {} = '.format(litres_captured_rain_event, metres_square_catchment))
    result = litres_captured_rain_event / metres_square_catchment
    print(('Thank Heavens you have seen a rain event of ' + str(result) + ' millimetres!'))

#client knows litres captured in rain event, millimetres of rain event
elif operation == 'm2':
    litres_captured_rain_event = int(input('Please enter the amount of increase in litres:\n' +
    'Use numbers only with no decimal places.\n'))
    millimetres_rain_event = int(input('Please enter the rain event in millimetres:\n' +
    'Use numbers only with no decimal places.\n'))
    print('{} / {} = '.format(litres_captured_rain_event, millimetres_rain_event))
    result = litres_captured_rain_event / millimetres_rain_event
    print('Congratulations you have an effective catchment of ' + str(result) + ' metres square.')

else:
    print('You have not typed a recognised value, please run the program again.')