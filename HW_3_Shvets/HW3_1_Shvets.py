# Read input string and convert it into integer
number1 = int(input("enter number1:"))
number2 = int(input("enter number2:"))
number3 = int(input("enter number3:"))

#  Read an operation from input
command = input("enter command + or *:")

if command == '+':
    sum_result = number1 + number2 + number3
    print(number1, command, number2, command, number3, '=', sum_result)
elif command == '*':
    mult_result = number1 * number2 * number3
    print(number1, command, number2, command, number3, '=', mult_result)
