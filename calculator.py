from setuptools.sandbox import setup_context

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

begin = True

while begin:
    print(art.logo)
    first_number = float(input("Enter first number: "))
    operator = input("Enter operator choices are +, -, *, or /: ")
    second_number = float(input("Enter second number: "))

    def math_output(first_number, operator, second_number):
        if operator == "+":
            return operations["+"](first_number, second_number)
        if operator == "-":
            return operations["-"](first_number, second_number)
        if operator == "*":
            return operations["*"](first_number, second_number)
        if operator == "/":
            return operations["/"](first_number, second_number)

    result = math_output(first_number, operator, second_number)
    output = print(f"{first_number} {operator} {second_number} = {math_output(first_number, operator, second_number)}")
    continue_math = input("Do you want to continue working with the previous result? (y/n): ").lower()

    while continue_math == "y":
        new_operator = input("Enter another operator, choices are +, -, *, or /: ")
        another_number =  int(input("Enter another number: "))
        counter = 0
        for count in range(counter + 1):
            new_result = math_output(result, new_operator, another_number)
            output = print(f"{result} {new_operator} {another_number} = {new_result}")
            result = new_result
            continue_math = input("Do you want to continue working with the previous result? (y/n): ").lower()
            begin = False
    else:
        print("\n" * 20)
        begin = True
