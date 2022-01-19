number1 = int(input("enter number1:"))
number2 = int(input("enter number2:"))
number3 = int(input("enter number3:"))

# Read an operation from input
command = input("enter command max, min or mean:")

if command == 'max':
    if number1 >= number2 and number1 >= number3:
        print(number1)
    elif number2 >= number1 and number2 >= number3:
        print(number2)
    else:
        print(number3)
elif command == 'min':
    if number1 <= number2 and number1 <= number3:
        print(number1)
    elif number2 <= number1 and number2 <= number3:
        print(number2)
    else:
        print(number3)

elif command == 'mean':
    mean_result = (number1 + number2 + number3) / 3
    print(mean_result)
