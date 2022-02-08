a = 1
b = 5
summa_1 = 0
count_1 = 0
summa_2 = 0
count_2 = 0
summa_3 = 0
count_3 = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        summa_1 = summa_1 + i
        count_1 = count_1 + 1
    elif i % 9 == 0:
        summa_2 = summa_2 + i
        count_2 = count_2 + 1
    elif i % 2 != 0:
        summa_3 = summa_3 + i
        count_3 = count_3 + 1

if count_1 != 0:
    print("сумма четных чисел (группа 1) =", summa_1, ";",  "среднеарифметическое (группа 1) =", summa_1 / count_1)

if count_2 != 0:
    print("сумма  чисел, кратных 9 (группа 2) =", summa_2, ";",  "среднеарифметическое (группа 2) =", summa_2 / count_2)

if count_3 != 0:
    print("сумма нечетных чисел (группа 3) =", summa_3, ";",  "среднеарифметическое (группа 3) =", summa_3 / count_3)
