max_number = int(input('Введите максимально возможное загаданное число: '))
import random
number = random.randint(1, max_number)
print('Вы угадываете число от 1 до ' + str(max_number))
user_number = None
count = 0
levels = {
    1: 10,
    2: 5,
    3: 3
}
level = int(input('выберите уровень сложности (от 1 до 3): '))
max_count = levels[level]

while number != user_number:
    count += 1
    if count > max_count:
        print('Вы проиграли')
        break
    print(f'Попытка № {count}')
    user_number = int(input('введите число: '))
    if number < user_number:
        print('Ваше число больше загадоного')
    elif number > user_number:
        print('Ваше число меньше загадоного')
else:
    print('Победа! Вы угадали!')