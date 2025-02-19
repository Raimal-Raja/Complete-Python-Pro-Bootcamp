# calculator

# add
def add (n1, n2):
    return n1 + n2

# substract
def sub(n1, n2):
    return n1 - n2

# multiplication
def multi(n1, n2):
    return n1 * n2

# division
def div(n1, n2):
    # if n2 == 0:
    #     return "Error! Division by zero."  # Handle division by zero
    return n1 / n2

n1 = int(input('Enter number1: '))
n2 = int(input('Enter number2: '))
print('+ = for addition\n- = for substraction\n/ = for division\n* = for multiplication ')
operation = input('which operation have to perform?')

dict = {
    '+': ['result',add(n1,n2)],
    '-': ['result',sub(n1,n2)],
    '*': ['result',multi(n1,n2)],
    '/':['result',div(n1,n2)]
}
if operation =='+':
    print(dict['+'])
elif operation == '-':
    print(dict['-'])
elif operation =='*':
    print(dict['*'])
elif operation =='/':
    print(dict['/'])
else:
    print('Invalid input!')