s = ''
num = input('Please, enter a number:')
for i in range(len(num)):
    if num[i] == '6' or num[i] == '3':
        continue
    else:
        s = s + num[i]
print(int(s))
