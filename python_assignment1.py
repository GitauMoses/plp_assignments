my_dict = {}
print(type(my_dict))
while True:
        # 1. Convert inputs to numbers immediately after receiving them.
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
        expression = input("Enter a mathematical expression (e.g., +, -, *, /) or 'exit' to quit: ")

        # 2. Add an 'exit' condition to break the loop.
        if expression.lower() == 'exit':
            print("Exiting the calculator.")
            break

        # 3. Perform the mathematical operation with the now-numeric variables.
        if expression == "+":
            result = num_1 + num_2
            print("Result:", result)
        elif expression == "-":
            result = num_1 - num_2
            print("Result:", result)
        elif expression == "*":
            result = num_1 * num_2
            print("Result:", result)
        elif expression == "/":
            # 4. Add a check to prevent division by zero.
            if num_2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num_1 / num_2
                print("Result:", result)
        else:
            print("Invalid expression. Please use +, -, *, or /.")
