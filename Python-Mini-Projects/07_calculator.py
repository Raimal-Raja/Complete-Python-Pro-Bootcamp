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

if operation == "+":
    print("result", add(n1=n1, n2=n2))
elif operation == "-":
    print("result",sub(n1=n1,n2=n2))
elif operation == "*":
    print("result",multi(n1,n2))
elif operation =="/":
    print("result",div(n1, n2))
else:
    print('Invalid operation!')