class FormulaError(Exception):
    pass

def calculate(formula):
    try:
        if formula == "quit":
            print("Exiting calculator.")
            return

        elements = formula.split()
        if len(elements) != 3:
            raise FormulaError("Invalid formula. Please provide a number, an operator (+ or -), and another number separated by spaces.")

        num1 = float(elements[0])
        operator = elements[1]
        num2 = float(elements[2])

        if operator not in ['+', '-']:
            raise FormulaError("Invalid operator. Please use + or -.")

        if operator == '+':
            result = num1 + num2
        else:
            result = num1 - num2

        print("Result:", result)

    except ValueError:
        raise FormulaError("Invalid number. Please provide a valid number.")

    except FormulaError as e:
        print("Error:", str(e))

while True:
    try:
        formula = input("Enter a formula (or 'quit' to exit): ")
        calculate(formula)
    except FormulaError as e:
        print("Error:", str(e))
