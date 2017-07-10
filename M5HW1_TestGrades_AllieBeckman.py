# accepts five number grades and returns the letter grade for each and the average of all grades
# 7/7/2017
# CTI-110 M5HW1 - Test Average and Grade
# Allie Beckman
average = 1
numGrade = 0
letterGrade = 'A'
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
def calc_average(g1,g2,g3,g4,g5):
    total = g1+g2+g3+g4+g5
    average = total/5
    return average
def determine_grade(numGrade):
    if numGrade >= 90:
        letterGrade = 'A'
    elif numGrade >= 80:
        letterGrade = 'B'
    elif numGrade >= 70:
        letterGrade = 'C'
    elif numGrade >= 60:
        letterGrade = 'D'
    else:
        letterGrade = 'F'
    return letterGrade
for counter in range(5):
    while True:
        try:
            numGrade = int(input('Please enter your number grade: '))
            break
        except ValueError:
            print('Please only enter a whole number.')
    letterGrade = determine_grade(numGrade)
    print('The letter grade is '+letterGrade)
    if counter == 4:
        g1 = numGrade
    elif counter == 3:
        g2 = numGrade
    elif counter == 2:
        g3 = numGrade
    elif counter == 1:
        g4 = numGrade
    elif counter == 0:
        g5 = numGrade
    counter = counter - 1
average = calc_average(g1,g2,g3,g4,g5)
letterGrade = determine_grade(average)
print('The numeric average of the scores is '+str(average)+'.')
print('The letter grade for the scores average is '+letterGrade+'.')
while True:
	try:
		quitGame = input("Press Q to quit: ")
		if quitGame == 'Q' or quitGame == 'q':
			quit()
		else:
			raise ValueError
	except ValueError:
		print('That was not a Q')
		
