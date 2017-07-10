# A small program to classify a persons age group based on their numerical age
# 6/14/2017
# CTI-110 M3HW1 - Age Classifier
# Allie Beckman
print('Hello, this is an age classification program.')
print('Enter an age and we will tell you the persons life stage.')
while True:
    while True:
        try:
            age = round(float(input('Age: ')), 2)
            break
        except ValueError:
            print('Error. Please enter a number')
            
    if age >= 20:
        print('This person is an adult.')
    elif age >= 13:
        print('This person is a teenager.')
    elif age > 1:
        print('This person is a child.')
    elif age >=0:
        print('This person is an infant.')
    else:
        print('This person has not been born yet.')

    while True:
        yOrN = input('Would you like to enter another age? y/n: ')
        if yOrN == 'y' or yOrN == 'Y':
            break
        elif yOrN == 'n' or yOrN == 'N':
            quit()
        else:
            print('Please enter y or n.')
