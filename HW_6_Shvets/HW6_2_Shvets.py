# Задание 2.1

a = 1
b = 5
while a <= b:
    print(a)
    a = a + 1

# Задание 2.2

a = 1
b = 5
while b >= a:
    print(b)
    b = b -1

# Задание 2.3

a = 1
b = 10
if a > b:
    c = a
    a = b
    b = c
while a <= b:
    if a % 7 == 0:
        print(a)
    a = a + 1

# Задание 2.4

a = 0
b = 6
count = 0
while a <= b:
    if a % 5 == 0:
        count = count + 1
    a = a + 1
print(count)
