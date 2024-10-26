

import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    does_operations = True
    first_number = float(input("Type the first number: "))

    while does_operations:
        for operator in operations:
            print(operator)
        op_symbol = input("Type the operator symbol: ")
        second_number = float(input("Type the second number: "))
        output = operations[op_symbol](first_number, second_number)
        print(f"{first_number} {op_symbol} {second_number} = {output}")

        continue_operation = input("Would you like to continue? [y/n]: ")

        if continue_operation == "y":
            first_number = output
        else:
            does_operations = False
            print("\n" * 20)
            calculator()

calculator()