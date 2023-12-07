def add(num1, num2):
    """
    Adds two numbers.
    """
    return num1 + num2

def subtract(num1, num2):
    """
    Subtracts two numbers.
    """
    return num1 - num2

def multiply(num1, num2):
    """
    Multiplies two numbers.
    """
    return num1 * num2

def divide(num1, num2):
    """
    Divides two numbers.
    """
    return num1 / num2

# Prompt the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display a menu of operation choices
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get the user's choice
choice = input("Enter your choice: ")

# Perform the calculation based on the user's choice
if choice == "1":
    result = add(num1, num2)
    operation = "+"
elif choice == "2":
    result = subtract(num1, num2)
    operation = "-"
elif choice == "3":
    result = multiply(num1, num2)
    operation = "*"
elif choice == "4":
    result = divide(num1, num2)
    operation = "/"
else:
    print("Invalid operation choice.")
    exit()

# Display the result
print(f"{num1} {operation} {num2} = {result}")