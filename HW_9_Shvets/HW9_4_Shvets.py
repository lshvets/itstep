while True:

    a = int(input("Enter number1 : "))
    b = int(input("Enter number2 : "))

    summa = a + b
    print('Summa =', summa)
    print('Max =', max(a, b))
    print('Min =', min(a, b))

    if b == 7 or a == 7:
        print("Good bye!")
        break
