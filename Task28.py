# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input("Введите деcятичное число: "))
# print(f'Десятичное число - {n}')
# b = ""
# while n > 0:
#     b = str(n%2) + b
#     n = n//2
# print(f'В двоичном представлении - {b}')

# a=int(input('Введите число: '))
# b=bin(a)
# print(b[2:])

s = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)


