# A program that asks the user how much they paid for a meal, what percentage
# they would like to tip, and then prints out a detailed summery of their purchase
# including the 7% sales tax.
# 6/8/2017
# CTI-110 M2HW2 - Tip Tax Total
# Allie Beckman

print('Hello, please enter the cost of your meal.')
while True:
    while True:
        try:
            mealCost = float(input('Meal cost: '))
            break
        except ValueError:
            print('Input error, please only enter a number.')
    while True:
        try:
            tip = (float(input('What percent would you like to tip? %'))/100)
            break
        except ValueError:
            print('Input error please try again')
        except TypeError:
            print('Input error please try again')
    tipAmount = round(mealCost*tip, 2)
    tax = round(mealCost*0.07, 2)
    mealTotal = round(mealCost+tipAmount+tax, 2)
    print('--------------------------------------------------------------')
    print('Cost Summery:')
    print('There is a 7% sales tax on every meal.')
    print('Meal cost: '+str(mealCost))
    print('Sales Tax: '+str(tax))
    print('Tip: '+str(tipAmount))
    print('Total: '+str(mealTotal)+'$')
    print('Thanks for your service!')
    print('--------------------------------------------------------------')
    while True:
        tryAgain = input('Would you like to enter another meal? y/n: ')
        if tryAgain == 'y' or tryAgain == 'n':
            if tryAgain == 'y':
                break
            else:
                quit()
        else:
            print('Error, please only enter y or n.')
