a = input()
if a == 'game':
    card = int(input('Угадай число'))
    while card != 5:
        print('Неверный ответ')
        card = int(input('Введите число'))
    print('Вы выйграли')