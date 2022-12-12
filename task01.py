# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие задачи: На столе лежит 117 конфета. Играют два игрока делая
#  ход друг после друга. Первый ход определяется жеребьёвкой. За один ход
# можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота
from random import randint


def p_vs_P():
    all = 217
    max = 28
    player = randint(1, 2)
    print(f"Игрок {player} ходит первым, вводите цифры и жмите Enter")
    while all > 0:
        print(f"Осталось конфет - {all} шт.")
        temp = int(input(f"Игрок {player} - "))
        if temp > 28:
            print("Можно брать не больше 28 конфет за раз")
        else:
            if all >= temp:
                all -= temp
                if all != 0:
                    if player == 1:
                        player = 2
                    else:
                        player = 1
            else:
                print(f"Можно брать не больше оставшихся{all} конфет")
    print(f"Игрок {player} победил")

def p_vs_b():
    print(f"Игрок 2 - бот")
    all = 217
    max = 28
    player = randint(1, 2)
    print(f"Игрок {player} ходит первым, вводите цифры и жмите Enter")
    while all > 0:
        print(f"Осталось конфет - {all} шт.")
        if player==2:
            if all<=28:
                temp = all
            elif all>56:
                temp=randint(1,28)
            elif 29<all<57:
                temp=all-29
            print((f"Игрок {player} бот - {temp}"))
        else:
            temp = int(input(f"Игрок {player} - "))
        if temp > 28:
            print("Можно брать не больше 28 конфет за раз")
        else:
            if all >= temp:
                all -= temp
                if all != 0:
                    if player == 1:
                        player = 2
                    else:
                        player = 1
            else:
                print(f"Можно брать не больше оставшихся{all} конфет")
    print(f"Игрок {player} победил")

game = int(input("На столе лежит 117 конфет игроки делают ход друг после друга.\nЗа один ход  можно \
забрать не более чем 28 конфет\n1 - игрок против игорока\n2 - игрок против бота\n "))

if game == 1:
    p_vs_P()
elif game == 2:
    p_vs_b()
else:
    print("Можно ввести только 1 или 2")
