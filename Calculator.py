print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Division")
print("5 - Exponentation")

option = int(input("Choose an operation: "))
result = 0

if(option in [1,2,3,4,5]):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        if num2 != 0:
           result = num1 / num2
        else:
            print("Error! Division by zero is not allowed")

    elif(option == 5):
        result = num1 ** num2

else:
    print("Invalid operation entered!")

print("The result of the operation is {}".format(result))