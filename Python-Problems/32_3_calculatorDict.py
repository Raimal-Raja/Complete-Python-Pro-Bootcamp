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
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

n1 = int(input('Enter number1: '))
n2 = int(input('Enter number2: '))



operations = {
    '+':add,
    '-':sub,
    '*':multi,
    '/':div
}

for operator in operations:
    print(operator)
operation_symbol = input('Pick an operation from the line above: ')
calculate_function = operations[operation_symbol]
first_answer = calculate_function(n1, n2) 

print(f"{n1} {operation_symbol} {n2} = {first_answer}")

operation_symbol = input('Pick an operation from the line above: ')
n3 = int(input('Enter next number: '))
calculate_function = operations[operation_symbol]
second_answer = calculate_function(calculate_function(n1,n2), n3) 

print(f"{first_answer} {operation_symbol} {n3} = {first_answer}")