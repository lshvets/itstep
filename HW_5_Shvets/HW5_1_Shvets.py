number = int(input("Enter number from 1 to 100 : "))
if number < 1 or number > 100:
    print('error')
elif number % 3 == 0 and number % 5 == 0:
    print('Fizz Buzz')
elif number % 3 != 0 and number % 5 != 0:
    print(number)
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
