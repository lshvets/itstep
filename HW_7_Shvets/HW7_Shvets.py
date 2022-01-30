# Guess my number

import random

play = True

while play:
    secret_number = random.randint(1, 20)
    guess_number = 0

    attempts = 5
    current_attempt = 0

    while secret_number != guess_number and attempts > 0:
        guess_number = int(input("Enter number : "))

        attempts = attempts - 1
        current_attempt = current_attempt + 1

        if secret_number < guess_number:
            print('Your number is more than expected')
            print(f'It is attempt {current_attempt} ')
            print(f'You have {attempts} more attempts')
        elif secret_number > guess_number:
            print('Your number is less than expected')
            print(f'It is attempt {current_attempt} ')
            print(f'You have {attempts} more attempts')

    if attempts > 0:
        print('YOU WIN!!!')
    else:
        print('YOU LOSE')

    is_try_again = str(input('Do you want to try again? '))

    if is_try_again != 'yes':
        play = False
