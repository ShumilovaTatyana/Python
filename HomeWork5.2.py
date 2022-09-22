# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# igrok1 = input("Игрок 1, введите ваше имя: ")
# igrok2 = input("Игрок 2, введите ваше имя: ")
# while True:
#     number = int(input('Игрок, введите количество конфет, которое возьмете: '))
#     if number > 1 and number < 28:
#         print(f'На столе - {2021 - number} конфет')
#         break
#     else:
#         print('Число должно быть больше 1, но меньше 28: ')

from random import randint

a = int(input('Введите количество конфет'))
hod = 0
wins = {0: 'Игрок', 1: 'Бот'}
while a > 0:
    if a <= 28:
        print(f'Выиграл {wins[hod]}')
        break
    if hod % 2 == 0:
        print('Ход Игрока')
        d = int(input('Введите количество конфет, которое хотите взять'))
        a -= d
        print(f'Осталось конфет: {a}')
    else:
        print('Ход Бота')
        d = a % 29
        a -= d
        print(f'Осталось конфет: {a}')
    hod = (hod + 1) % 2




# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")