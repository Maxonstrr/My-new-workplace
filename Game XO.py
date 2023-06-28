def begin():
    print("     |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("     |        Приветсвуем вас в нашей лучшей в мире игре 'Крестики-Нолики!!!'        |")
    print("     |-------------------------------------------------------------------------------|")
    print("     |            В этой игре вы играете либо за крестик,либо за нолик               |")
    print("     |       Побеждает тот, кто первый собрал комбинацию из трех подряд знаков       |")
    print("     |-------------------------------------------------------------------------------|")
    print("     |Игра производится посредством ввода координат поля, начиная от 0 и заканчивая 2|")
    print("     |-------------------------------------------------------------------------------|")
    print("     |            Желаем вам приятной игры и пусть победит крутейший!!               |")
    print("     |_______________________________________________________________________________|")


field = [[" "] *3 for i in range(3)]
player_1=input("Игрок 1. Введите ваше имя:")
player_2=input("Игрок 2. Введите ваше имя:")

def battle():
    print ("  | 0 | 1 | 2 ")
    for i in range(len(field)):
        print ("-" * 15)
        print (i, *field[i],sep=' | ')

def step():
    while True:
        ask= input("Введите две координаты через пробел:").split()
        if len(ask) != 2:
            print("Введите две координаты!")
            continue
        if not(ask[0].isdigit() and ask[1].isdigit()):
            print("Введите числа!")
            continue
        x,y=map(int,ask)
        if not(0 <= x <= 2 and 0 <= y <= 2):
            print("Вы вышли с поля!")
            continue
        if field[x][y]!= " ":
            print("Клетка занята!")
            continue
        return x,y


def winner():
    check_winner= (((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),
                   ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                   ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
    for i in (check_winner):
        symbols=[]
        for j in (i):
            symbols.append(field[j[0]][j[1]])
        if symbols == ["X", "X", "X"]:
            print(f"{player_1} победил!!")
            return True
        if symbols == ["0", "0", "0"]:
            print(f"{player_2} победил!!")
            return True
    return False



begin()
count = 0
while True:
    count += 1
    battle()
    if count % 2 == 0:
        print(f"        {player_2}, ваш ход.")
    else:
        print(f"        {player_1}, ваш ход.")
    x, y = step()
    if count % 2 == 0:
        field[x][y] = "0"
    else:
        field[x][y] = "X"
    if winner():
        break
    if count == 9:
        print(f"        У нас два победителя!!{player_1} и {player_2}!!")
        break