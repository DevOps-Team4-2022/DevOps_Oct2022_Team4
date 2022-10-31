
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Please select the type of operations: \n")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("3. Divide")

while True:
    option = int(input("Enter number of choice: "))

    if option in (1,2,3,4):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if option == 1:
            print(num1, "+", num2, "=", add(num1, num2))

        elif option == 2:
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif option == 3:
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif option == 4:
            print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Invalid input, please try again.")
