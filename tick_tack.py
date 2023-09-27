import os

os.system('clear')
def print_game():
    print(f' {list_game[0]} | {list_game[1]} | {list_game[2]}\n'
          f'--- --- ---\n'
          f' {list_game[3]} | {list_game[4]} | {list_game[5]}\n'
          f'--- --- ---\n'
          f' {list_game[6]} | {list_game[7]} | {list_game[8]}')


def input_(name):
    inp = input(f'Введите номер ячейки для {name}:')
    while True:
        try:
            inp = int(inp)
        except ValueError:
            inp = input('Некорректный ввод! Попробуйте еще раз:')
            continue
        if inp < 1 or inp > 9:
            inp = input('Ввод за пределами диапазона! Попробуйте еще раз:')
            continue
        if not(str(list_game[inp - 1]) in list_numbers):
            inp = input('Место уже занято! Попробуйте еще раз:')
            continue
        return inp


def set_xo(symbol, name):
    global list_game
    print_game()
    inp = input_(name.lower() + 'а')
    list_game[inp - 1] = symbol
    os.system('clear')
    check_win(name)


def check_win(name):
    for i in list_combination:
        if list_game[int(i[0])] == list_game[int(i[1])] == list_game[int(i[2])]:
            if list_game[int(i[0])] == 'x':
                win('x', name)
            elif list_game[int(i[0])] == 'o':
                win('o', name)
    if moves == 8:
        print_game()
        print('Ничья!')
        exit()


def win(symbol, name):
    print_game()
    print(f'{name}и выиграли!!!')
    print(f'  {symbol}   {symbol}')
    print(f'')
    print(f'{symbol}       {symbol}')
    print(f' {symbol * 7}')
    exit()


list_combination = ['012', '345', '678', '048', '246', '036', '147', '258']
list_numbers = '123456789'
list_game = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

moves = 0
while True:
    if moves % 2 == 0:
        set_xo('x', 'Крестик')
    else:
        set_xo('o', 'Нолик')
    moves += 1