import random
number = random.randint(1, 100)

while True:
    user_number = int(input('введите число: '))
    if number == user_number:
        print('Победа! Вы угадали!')
        break
    elif number > user_number:
        print('Ваше число больше загадоного')
    else:
        print('Ваше число меньше загадоного')
