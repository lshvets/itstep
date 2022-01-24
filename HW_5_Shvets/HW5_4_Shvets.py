realization_manager1 = int(input("Enter amount for manager1 in $:"))
realization_manager2 = int(input("Enter amount for manager2 in $:"))
realization_manager3 = int(input("Enter amount for manager3 in $:"))
rm1 = realization_manager1
rm2 = realization_manager2
rm3 = realization_manager3

if 0 < rm1 < 500:
    salary1 = 200 + rm1*0.03
    print('salary1=', salary1, '$')
elif 500 <= rm1 <= 1000:
    salary1 = 200 + rm1 * 0.05
    print('salary1=', salary1, '$')
elif rm1 > 1000:
    salary1 = 200 + rm1 * 0.08
    print('salary1=', salary1, '$')
elif rm1 < 0:
    print('error')
if 0 < rm2 < 500:
    salary2 = 200 + rm2*0.03
    print('salary2=', salary2, '$')
elif 500 <= rm2 <= 1000:
    salary2 = 200 + rm2 * 0.05
    print('salary2=', salary2, '$')
elif rm2 > 1000:
    salary2 = 200 + rm2 * 0.08
    print('salary1=', salary2, '$')
elif rm2 < 0:
    print('error')
if 0 < rm3 < 500:
    salary3 = 200 + rm3*0.03
    print('salary3=', salary3, '$')
elif 500 <= rm3 <= 1000:
    salary3 = 200 + rm3 * 0.05
    print('salary3=', salary3, '$')
elif rm3 > 1000:
    salary3 = 200 + rm3 * 0.08
    print('salary3=', salary3, '$')
elif rm3 < 0:
    print('error')

x = salary1

y = salary2

z = salary3

if x > y and x > z:
    print('best manager is manager1')
    print("his bonus is 200$, so his total monthly salary is", salary1 + 200, '$')
elif y > x and y > z:
    print('best manager is manager2')
    print("his bonus is 200$, so his total monthly salary is", salary2 + 200, '$')
elif z > x and z > y:
    print('best manager is manager3')
    print("his bonus is 200$, so his total monthly salary is", salary3 + 200, '$')
else:
    print('all manager are the best')
    print("bonus is 200$, so total monthly salary for each manager is", salary1 + 200, '$')


