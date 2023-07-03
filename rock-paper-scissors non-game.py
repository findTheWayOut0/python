-- Через списки, сперва просто, в идеале когда нибудь запилить игру

print('Welcome to the rock-paper-scissors')

optionals = ['камень', 'ножницы', 'бумага']
results = ['ничья', 'выиграл первый игрок', 'выиграл второй игрок']


# Вводить только "камень"/"ножницы"/"бумага"
firstPlayerMove = input()
secondPlayerMove = input()


res = optionals.index(secondPlayerMove) - optionals.index(firstPlayerMove)

print(results[res])
