# Calculates the miles traveled by a car that is moving at 70mph based on
# different travel times. Then estimates miles traveled based on user input.
# 6/8/2017
# CTI-110 M2HW1 - Distance Traveled 
# Allie Beckman

speed = int(70)
print('In six hours a car driving 70mph will go ' + str(speed*6) + ' miles.')
print('In ten hours a car driving 70mph will go ' + str(speed*10) + ' miles.')
print('And in fifteen hours a car driving 70mph will go ' + str(speed*15) + ' miles')
print('How fast will you be driving?')
while True:
    while True:
        try:
            userSpeed = int(input('Enter your MPH: '))
            break
        except ValueError:
            print('Invalid input.')
    while True:
        try:
            userTime = int(input('How many hours are you driving? '))
            break
        except ValueError:
            print('Invalid input, please remember to round to the nearest hour.')
    while True:
        print('On a scale of 1 to 3, 1 being no traffic and 3 being heavy traffic, how much traffic will likley be on your trip?')
        try:
            traffic = int(input('Traffic: '))
            break
        except ValueError:
            print('Please only enter a number 1 to 3')
    travelTime = round(((userSpeed/traffic)*userTime), 2)
    print('You will travel about ' + str(travelTime) + ' miles.')
    while True:
        print('Would you like to estemate another trip?')
        userContinue = input('y or n: ')
        if userContinue == 'y' or userContinue == 'n':
            if userContinue == 'y':
                break
            if userContinue == 'n':
                print('goodbye')
                quit()
        else:
            print('Invalid input please enter y or n')
