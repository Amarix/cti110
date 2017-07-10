print('Hello please enter positive numbers. When finished, enter a negative number. I will then display the sum of all positive numbers entered')
total = 0
while True:
    while True:
        try:
            number = int(input('Please enter a whole number. '))
            break
        except ValueError:
            print('Error. Please only enter a whole number.')
    if number >= 0:
        total = total+number
    elif number < 0:
        print('The sum of numbers is ' +str(total)+ '.')
        while True:
            con = input('Would you like to add another set of numbers? y/n: ')
            if con == 'Y' or con == 'y':
                total = 0
                break
            elif con == 'N' or con == 'n':
                print('goodbye')
                quit()
            else:
                print('Error. Please enter a y or n.')
