s = 'доход'
rs = ''
for i in range(len(s)):
    rs = s[i] + rs
b = rs
if s == b:
    print('Палиндром')
else:
    print('Не является палиндромом')

