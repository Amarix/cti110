# A project to display projected profit if it is 23% of total sales
# 6/8/2017
# CTI-110 M2T1 - Sales Prediction
# Allie Beckman

while True:
    print('Please enter your projected amount of total sales.')
    totalSales = float(input('Total sales equals: '))
    totalProfit = float( round(totalSales*0.23, 2))
    print('Your total annual profit will be ' + str(totalProfit) + '$')
    while True:
        print('Would you like to enter a different amount?')
        newSales = input('Enter y or n: ')
        if newSales == ('y') or newSales == ('n'):
            if newSales == 'y':
                break
            else:
                print ('Goodbye')
                quit()
        else:
            print ('Invalid input try again: ')


                 
