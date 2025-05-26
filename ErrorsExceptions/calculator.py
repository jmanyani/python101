def smart_calculator():
    print("Welcome to SmartCalc — Enter your operation or type 'exit' to quit.")

    while True:
        try:
            user_input = input("\nEnter a math expression (e.g., 4+5 or 4 + 5): ").strip()
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break

            # Handle unspaced expressions by adding spaces around operators
            for op in ['+', '-', '*', '/', '**']:
                user_input = user_input.replace(op, f' {op} ')
            
            # Split and clean up (might have multiple spaces now)
            parts = [p for p in user_input.split() if p]
            
            if len(parts) != 3:
                raise ValueError("Input must be in the format: number operator number (e.g., 4+5 or 4 + 5)")

            num1, op, num2 = parts
            num1 = float(num1)
            num2 = float(num2)

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                result = num1 / num2
            elif op == '**':
                result = num1 ** num2
            else:
                raise ValueError(f"Unsupported operator: {op}")

            print(f"Result: {result}")
            
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            print("Ready for the next calculation...")

if __name__ == "__main__":
    smart_calculator()