operator1 = (input("Enter from_operator (mtc, life or star): "))
operator2 = (input("Enter to_operator (mtc, life or star): "))

call_duration = int(input("Enter call_duration in min: "))

mtc_price_per_minute = 1
life_price_per_minute = 2
star_price_per_minute = 1.5

if operator1 == operator2 and (operator1 == 'mtc' or operator1 == 'life' or operator1 == 'star'):
    print('call cost=', 0 * call_duration, '$')
else:
    if operator1 == 'mtc':
        print('call cost=', mtc_price_per_minute * call_duration, '$')
    if operator1 == 'life':
        print('call cost=', life_price_per_minute * call_duration, '$')
    if operator1 == 'star':
        print('call cost=', star_price_per_minute * call_duration, '$')



