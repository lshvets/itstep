summa = 0

for i in range(100, 1000):
    a, b, c = str(i)
    if a != b and b != c and a != c:
        summa = summa + 1

print(summa)