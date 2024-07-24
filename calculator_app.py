def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    if num_2 == 0:
        return num_2 /num_1 # trying to invert calculation to avoid division by zero error
    #     raise ValueError("Dividing by zero will result in an error.")
    # return num_1 / num_2


while True:
    try:
        calculation = input("Enter calculation (add/subtract/multiply/divide): ").strip().lower()
        if calculation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid calculation. Please choose from add, subtract, multiply, divide.")
            continue
        
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))
        
        if calculation == 'add':
            result = add(num_1, num_2)
        elif calculation == 'subtract':
            result = subtract(num_1, num_2)
        elif calculation == 'multiply':
            result = multiply(num_1, num_2)
        elif calculation == 'divide':
            if num_2 == 0:
                result = divide(num_2, num_1) # # trying to invert calculation to avoid division by zero error
            else:
                result = divide(num_1, num_2)
            # except ValueError as ve:
            #     print(ve)
                continue
        
        print(f"Result of {calculation}: {result}")
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"Error: {e}")


