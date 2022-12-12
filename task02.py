# Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)
tatami = list(range(1,10))

def print_tatami(tatami):
    print('-'*12)
    for i in range(3):
        print('|', tatami[0+i*3],'|', tatami[1+i*3], '|', tatami[2+i*3], '|')
        print('-'*12)

def step(marker):
    bo = False
    while not bo:
        player = input(f"Ваш ход, выберите ячейку для {marker} ")
        try:
            player =int(player)
        except:
            print('некорректный ввод')
            continue
        if player >= 1 and player <= 9:
            if(str(tatami[player-1]) not in 'XO'):
                tatami[player-1] = marker
                bo = True
            else:
                print('Ячейка занята')
        else:
            print('Повторите ввод')
def victory(tatami):
    victory = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in victory:
        if tatami[i[0]] == tatami[i[1]] == tatami[i[2]]:
            return tatami[i[0]]
    return False

def game(tatami):
    count =0
    bo = False
    while not bo:
        print_tatami(tatami)
        if count % 2 == 0:
            step('X')
        else:
            step('0')
        count +=1
        if count > 4:
            win = victory(tatami)
            if win:
                print_tatami(tatami)
                print(win,'Победа')
                bo = True
                break
            if count == 9:
                print_tatami(tatami)
                print('Победила, ДРУЖБА)')
        print_tatami(tatami)
game(tatami)
