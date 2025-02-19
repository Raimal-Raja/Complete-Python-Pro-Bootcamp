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



operations = {
    '+':add,
    '-':sub,
    '*':multi,
    '/':div
}

def calculator():
    n1 = int(input('Enter number1: '))
    should_continue = True
    while should_continue:
        print("Available operations: " + " ".join(operations.keys()))
        operation_symbol = input('Pick an operation from the list above: ')
        if operation_symbol not in operations:
            print("Invalid operation. Please try again.")
            continue
        n2 = int(input('Enter number2: '))
        calculate_function = operations[operation_symbol]
        result = calculate_function(n1, n2)
        print(f'{n1} {operation_symbol} {n2} = {result}')
        # if input(f'Type "Y" to continue calculing with {result}, or type "n" to exit: ') =="y":
        conti = input(f'Type "Y" to continue calculing with {result},or type "n" to exit, and "s" for starting from fresh:  ')
        if conti =='y':
            n1 == result
        elif conti == 'n':
            print("Thank you for using the calculator!")
            return 
        elif conti =='s':
            print("Restarting calculator...\n")
            calculator()
        else:
            print("Invalid input. Exiting calculator.")
            should_continue = False

calculator()
print("Thank you for using the calculator!")