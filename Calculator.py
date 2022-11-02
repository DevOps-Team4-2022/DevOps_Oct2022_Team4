import math

#functions############################################################
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a,b):
    return a**b


def main():
    print("Please select the type of operations")
    print("1. Standard Arithmetic")
    print("2. Trigonometry ")
    print("3. Exponent")
#print("4. ")
######################################################################

while True:
    main()
    option = int(input("Enter type of operations: "))
    if option in (1,2,3,4):
        #Option 1: Arithmetic
        if option == 1:
            print("Please select the type of Arithmetic")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("3. Divide")
            choice = int(input("Enter type of Arithmetic: "))
            if choice in (1,2,3,4):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == 1:
                    print(num1, "+", num2, "=", add(num1, num2))

                elif choice == 2:
                    print(num1, "-", num2, "=", subtract(num1, num2))

                elif choice == 3:
                    print(num1, "*", num2, "=", multiply(num1, num2))

                elif choice == 4:
                #produce error when 0/0
                    if num1 == 0.0 and num2 ==0.0:
                        print("Error")
                    else:
                        print(num1, "/", num2, "=", divide(num1, num2))
                    
        #Option 2: Trigonometry        
        elif option == 2:
            print("Please select the type of Trigonometry")
            print("1. Sin")
            print("2. Cos")
            print("3. Tan")
            print("4. Inversed Sin")
            print("5. Inversed Cos")
            print("6. Inversed Tan")
            choice = int(input("Enter type of Trigonometry: "))
            if choice == 1:
                num = float(input("Enter radians number: ")) 
                print(math.sin(num))
            if choice == 2:
                num = float(input("Enter radians number: ")) 
                print(math.tan(num))
            if choice == 3:
                num = float(input("Enter radians number: ")) 
                print(math.cos(num))
            if choice == 4:
                num = float(input("Enter radians number: ")) 
                print(math.asin(num))
            if choice == 5:
                num = float(input("Enter radians number: ")) 
                print(math.acos(num))
            if choice == 6:
                num = float(input("Enter radians number: ")) 
                print(math.atan(num))

        #Option 3: 
        elif option == 3:
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the power number: "))
        #checking whether the function produces error
            if power(num1,num2)>0 :
                print(power(num1,num2))
            else:
                print("Error")

        #Option 4:  
    else:
        print("Invalid input, please try again.")
        
    


