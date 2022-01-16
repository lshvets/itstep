# gender = 'male'#female
# age = 13
# if gender == 'male':
#     if age < 18:
#         print('A boy')
#     else:
#         print('A man')
# elif gender == 'female':
#     if age < 18:
#         print('A girl')
#     else:
#         print('A woman')
# else:
#     if age < 18:
#         print('A child')
#     else:
#         print('An adult')
# number1 = 1
# command='+'
# number2=0
# if command=='+':
#     print(number1,command,number2,'=',number1 + number2)
# elif command=='-':
#     print(number1, command, number2, '=', number1 - number2)
# elif command=='*':
#     print(number1, command, number2, '=', number1 * number2)
# elif command=='/':
#     if number2!= 0:
#         print(number1, command, number2, '=', number1 / number2)
#     else:
#         print('zero division')
# else:
#     print('incorrect command')
number1 = input("enter number1:")
command = input("enter command:")
number2 = input("enter number2:")
if type(number1) == type(1):
    if type(number2) == type(1):
        if command == '+':
            print(number1, command, number2, '=', number1 + number2)
        elif command == '-':
            print(number1, command, number2, '=', number1 - number2)
        elif command == '*':
            print(number1, command, number2, '=', number1 * number2)
        elif command == '/':
            if number2 != 0:
                print(number1, command, number2, '=', number1 / number2)  # PEP 8 Ctrl + Alt + L
            else:
                print('Zero division')
        else:
            print('Incorrect command')