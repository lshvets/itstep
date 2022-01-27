a = 1
b = 15

if a > b:
    c = a
    a = b
    b = c

while a <= b:
    if a % 3 == 0 and a % 5 == 0:
        print('Fizz Buzz')
    elif a % 3 == 0:
        print('Fizz')
    elif a % 5 == 0:
        print('Buzz')
    else:
        print(a)

    a = a + 1
