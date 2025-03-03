# calculator

# addition
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



operations = {
    '+':add,
    '-':sub,
    '*':multi,
    '/':div
}

should_continue = True
while should_continue:
    print("Available operations: " + " ".join(operations.keys()))
    operation_symbol = input('Pick an operation from the list above: ')

    if operation_symbol not in operations:
        print("Invalid operation. Please try again.")
        continue  # Restart the loop if an invalid operation is entered

    n2 = float(input('Enter next number: '))  # Ask for next number

    calculate_function = operations[operation_symbol]
    result = calculate_function(n1, n2)

    print(f"{n1} {operation_symbol} {n2} = {result}")
    
    # Ask if the user wants to continue
    cont = input("Do you want to continue with this result? (yes/no): ").strip().lower()
    
    if cont == 'yes':
        n1 = result  # Update n1 with the latest result for continuous calculation
    elif cont == 'no':
        should_continue = False
    else:
        print("Invalid input. Exiting calculator.")
        should_continue = False

print("Thank you for using the calculator!")