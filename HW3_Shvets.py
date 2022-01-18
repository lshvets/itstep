# Задание1
#  Read input string and convert it into integer
number1 = int(input("enter number1:"))
number2 = int(input("enter number2:"))
number3 = int(input("enter number3:"))

# Read an operation from input
command = input("enter command + or *:")

if command == '+':
     sum_result = number1 + number2 + number3
     print(number1, command, number2, command, number3, '=', sum_result)
elif command == '*':
     mult_result = number1 * number2 * number3
     print(number1, command, number2, command, number3, '=', mult_result)

# Задание2
#  Read input string and convert it into integer
number1 = int(input("enter number1:"))
number2 = int(input("enter number2:"))
number3 = int(input("enter number3:"))

# Read an operation from input
command = input("enter command max, min or mean:")
if command == 'max':
    max_result = max(number1, number2, number3)
    print(max_result)
if command == 'min':
    min_result = min(number1, number2, number3)
    print(min_result)
if command == 'mean':
    mean_result = (number1 + number2 + number3)//3
    print(mean_result)




# Задание3

m = int(input("Enter your length in metr:"))
inch = 0.0254 * m
ft = 0.3048 * m
mile = 1609.34 * m
print("" + str(m) + "m it's equal " + str(inch) + "inch")
print("" + str(m) + "m it's equal " + str(ft) + "ft")
print("" + str(m) + "m it's equal " + str(mile) + "mile")

