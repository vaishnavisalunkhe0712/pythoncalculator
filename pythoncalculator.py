#Menu

print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")



# This function adds two numbers
def addittion(num1, num2):
    return num1+ num2

# This function subtracts two numbers
def subtraction(num1, num2):
    return num1- num2


# This function multiplies two numbers
def multiplication(num1, num2):
    return num1* num2

# This function divides two numbers
def division(num1, num2):
    return num1/ num2

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", addittion(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtraction(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))

        next= input("Do you want to continue? (yes/no): ")
        if next == "no":
            break
    else:
        print("Invalid Input")