class EvenNumberException(Exception):
    pass

def check_number():
    try:
        number = int(input("Enter an integer: "))
        if number % 2 == 0:
            raise EvenNumberException("Even numbers are not allowed.")
        else:
            print("Input number is odd:", number)
    except EvenNumberException as e:
        print("Error:", str(e))
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")

check_number()
