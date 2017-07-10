# A small project that accepts the length and width of two different rectangles from the user
# and returns which rectangle has the largest area or if they are equal.
# 6/14/2017
# CTI-110 M3T1 - Areas of Rectangles
# Allie Beckman
print('Hello, I will compare the area of two rectangels but first I need their measurements')
while True:
    while True:
        try:
            firstWidth = int(input('What is the width of the first rectangle? '))
            break
        except ValueError:
            print('please only enter a number')
    while True:
        try:
            firstLength = int(input('What is the length of the first rectangle? '))
            break
        except ValueError:
            print('please only enter a number')
    while True:
        try:
            secondWidth = int(input('What is the width of the second rectangle? '))
            break
        except ValueError:
            print('please only enter a number')
    while True:
        try:
            secondLength = int(input('What is the length of the second rectangle? '))
            break
        except ValueError:
            print('please only enter a number')
    firstArea = firstWidth*firstLength
    secondArea = secondWidth*secondLength
    if firstArea == secondArea:
        print('The rectangles have the same area.')
        print('Both are ' + str(firstArea) + ' square units.')
    elif firstArea > secondArea:
        dif = firstArea-secondArea
        print('The first rectangle has a greater area than the second rectangle.')
        print('The difference is ' + str(dif) + ' square units.')
    elif firstArea < secondArea:
        dif = secondArea-firstArea
        print('The first rectangle has a smaller area than the second rectangle.')
        print('The difference is ' + str(dif) + ' square units.')
    while True:
        try:
            yOrN = input('Would you like to try again? y/n: ')
            if yOrN == 'y' or yOrN == 'Y':
                break
            elif yOrN == 'n' or yOrN == 'N':
                quit()
            else:
                print('Please only enter a y or n')
        except ValueError:
            print('Value Error please try again')
