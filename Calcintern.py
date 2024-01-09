print("Select operation.")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")
# take input from the user
choice = input("Enter choice(Add/Subtract/Multiply/Divide): ")
# This function adds two numbers
def add(num1, num2):
    return num1 + num2

# This function subtracts two numbers
def subtract(num1, num2):
    return num1 - num2

# This function multiplies two numbers
def multiply(num1, num2):
    return num1 * num2

# This function divides two numbers
def divide(num1, num2):
    return num1 / num2

if choice in ('Add', 'Subtract', 'Multiple', 'Divide'):
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

if choice == 'Add':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 'Subtract':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 'Multiply':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 'Divide':
    print(num1, "/", num2, "=", divide(num1, num2))
        
else:
    print("Invalid Input")