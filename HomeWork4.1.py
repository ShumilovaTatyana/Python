# 1. Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math
# d = input('Введите число d указывающее степень округления числа pi ')
# d = d[2:len(d)]
# print(round(math.pi,len(d)))

a = int(input('введите нужную точность 1#= '))
pi_target = 0
for i in range(1, 1000000):
     pi_target += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
print(str(pi_target)[:a + 2])


# d = int(input('Введите d: '))
# res = 10**{-1} <= d <= 10**{-10}
# print(res)

# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи: "))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# import math
# from math import pi

# n = pi
# print(round(n,3))

# Формула Бэйли — Боруэйна — Плаффа

# n = 100
# my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))

# print(my_pi)