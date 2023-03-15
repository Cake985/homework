games = []
game = input('Ввелите название игры:')
while game in '0':
    if game in games:
        print('Эта игра уже в записана')
    else:
        games.append(game)
        print('Игра добавлена в список')
    game = input('Введите название игры')
games.sort()
print(games)