# RK-2 method python program
import math
import sympy as sym
from prettytable import PrettyTable
from Equation import Expression
table = PrettyTable()

def main():
    # Inputs
    exp = (input('\nEnter the required expression:\n y\'=f(x,y): '))
    function = Expression(exp, ['x', 'y'])

    print('\nEnter the initial conditions [ y(x0) = y0 ] :')
    x0 = float(input('x0 = '))
    y0 = float(input('y0 = '))

    print('\nEnter the calculation point:')
    xn = sym.sympify(PiConverter(input('xn = ')))

    print('\nEnter the required number of decimal places: ')
    precision = int(input('No. of decimal places: '))

    # Take n or h as input as per the user's choice
    ch = int(
        input('\nEnter 1 to input the value of n or 2 to input the value h:  \n '))
    if ch == 1:
        step = int(input('Enter the number of steps: \nn = '))
        rk2(x0, y0, xn, step, function, precision)

    elif ch == 2:
        step_size = float(input('Enter the step size \nh = '))
        step = round((xn-x0)/step_size)
        rk2(x0, y0, xn, step, function, precision)
    else:
        print('Error! Either 1 or 2 should be entered.')

    #Prompting the user to run the program again  
    answer = str(input('Run again? (y/n): '))
    if answer not in ('y', 'n'):
        print("invalid input.")
    if answer == 'y':
        main()
    else:
        print("Goodbye!")
 

#RK-2 Meethod
def rk2(x0, y0, xn, n, f, precision):
    # Calculating step size
    h = round((xn-x0)/n, precision)

    # Creating the table
    table.title = '~~~~~~SOLUTIONS: RUNGE-KUTTA 2nd ORDER METHOD~~~~~~'
    table.field_names = ['xn', 'yn', 'k1', 'k2',
                         'yn+1', 'interval']

    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h), (y0+k1)))
        k = (k1+k2)/2
        yn = y0 + k
        a = x0+h
        table.add_row([f'{round(value,precision):.{precision}f}' for value in [
                      x0, y0, k1, k2, yn]]+[f'({x0:.{precision}f},{a:.{precision}f})'])
        y0 = yn
        x0 = x0+h

    print('\n')
    print(table)

    print(' \n ~~~~~~RESULT ~~~~~~ \n')
    print(f'At x = {round(xn,precision)}, y = {round(yn,precision)} \n')


# To convert pi from the console into a floating number
def PiConverter(input):
    # Defining dictionary
    symbol = {
        'pi': math.pi
    }
    output = ""
    for i in input:
        # If the value of character i.e. "i" is defined as the keyword in the symbol dictonary then it is replaced and appended in output string else the character itself is appended
        output += symbol.get(i, i)

    return output  # return the converted value


if __name__ == '__main__':
    main()

