# A small program to convert a numerical grade to a letter grade
# the projects purpose was to debug the if else statements that compared the scores
# 6/14/2017
# CTI-110 M3T2 - Debugging
# Allie Beckman

while True:
    while True:
        try:
            score = int(input('what was your numerical score? '))
            break
        except ValueError:
            print('Please enter a whole number.')
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    
    if score >= A_score:
        print('Your grade is A.')
    elif score >= B_score:
        print('Your grade is B.')
    elif score >= C_score:
        print('Your grade is C.')
    elif score >= D_score:
        print('Your grade is D.')
    else:
        print('Your grade is F.')
        
    while True:
        yOrN = input('Would you like to enter another grade? y/n ')
        if yOrN == 'y' or yOrN == 'Y':
            break
        elif yOrN == 'n' or yOrN == 'N':
            quit()
        else:
            print('Please enter a y or n.')
