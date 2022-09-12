# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

s = '0.56'
summ = 0
for i in s:
    if i.isdigit():
        summ += int(i)
print(summ)

# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))


# numb = float(input('Введите вещественное число: '))
# summ = 0
# for el in str(numb):
#     if el != '.':
#         summ += int(el)
# print(summ)


# num = input('Введите вещественное число: ')
# sum = 0
# for i in num:
#     if i != '.' and i !='-':
#         sum += int(i)
# print(sum)

# num = int(input("Введите число:"))
# print(num)
# s = str(num)
# sum = 0
# for i in range(len(s)):
#     sum = sum + int(s[i])
# print('Сумма цифр числа', num,' = ', sum)   


# float_num = input('Введите число: ')
# sum = 0
# for i in float_num:
#     if i != '.':
#         sum = sum + int(i)
# print('Сумма цифр числа', float_num,' = ', sum)


