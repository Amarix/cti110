# A program that adds the amount of bugs collected per day for five days and displays
# a total at the end of the five days
# 6/15/2017
# CTI-110 M4T1 - Bug Collector
# Allie Beckman
while True:
    totalBugs = 0
    dayLeft = 5
    dayOn = 1
    while dayLeft > 0:
        try:
            totalBugs = totalBugs + int(input('How many bugs were gathered on day ' + str(dayOn) + ': '))
            dayOn = dayOn+1
            dayLeft = dayLeft-1
        except ValueError:
            print('please only enter a number')

    print('The total number of bugs captured this week is ' + str(totalBugs) + '.')
    while True:
        yOrN = input('Would you like to calculate another week? y/n: ')
        if yOrN == 'y' or yOrN == 'Y':
            break
        elif yOrN == 'n' or yOrN == 'N':
            quit()
        else:
            print('Please enter a y or n value.')
