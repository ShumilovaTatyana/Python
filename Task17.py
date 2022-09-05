# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# (1+1/n)**n

num = int(input("Введите число N:"))
def posledovat(num):
    return[round((1 + 1 / n)**n, 2) for n in range(1, num + 1)]
print(posledovat(num))



