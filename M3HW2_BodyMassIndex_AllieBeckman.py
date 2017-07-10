# A program that calculates a persons body mass index based on their height in
# inches and their weight in pounds.
# 6/14/2017
# CTI-110 M3HW2 - Body Mass Index
# Allie Beckman
print('Hello, to calculate an accurate BMI please enter your weight in pounds and your height in inches.')
while True:
    while True:
        try:
            weight = round(float(input('Please enter your weight: ')), 2)
            break
        except ValueError:
            print('Please only enter a numeric value.')
    while True:
        try:
            height = round(float(input('Please enter your height in inches: ')), 2)
            break
        except ValueError:
            print('Please only enter a numeric value.')
    bmi = round((weight * (703/(height*height))), 1)
    if bmi >= 30:
        print('Your BMI is ' + str(bmi) + '.')
        print('This score indicates that you are considered obese.')
    elif bmi >= 25:
        print('Your BMI is ' + str(bmi) + '.')
        print('This score indicates that you are considered overweight.')
    elif bmi >= 18.5:
        print('Your BMI is ' + str(bmi) + '.')
        print('This score indicates that you are considered a normal weight.')
    else:
        print('Your BMI is ' + str(bmi) + '.')
        print('This score indicates that you are considered underweight.')
    while True:
        yOrN = input('Would you like to enter another weight? y/n: ')
        if yOrN == 'y' or yOrN == 'Y':
            break
        elif yOrN == 'n' or yOrN == 'N':
            quit()
        else:
            print('Please enter a y or n.')
