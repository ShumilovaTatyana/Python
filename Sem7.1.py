# 1.напечатать сторку в одну линию - C:\WINDOWS\System32\drivers\etc\nst

# 4. Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

# list_input = [i * i for i in range(10, 100) if i % 9 == 0]
# print(list_input)
# list_input = [i for i in range(10, 100)]
# list_input = list(filter(lambda i: i % 9 == 0, list_input))
# list_input = list(map(lambda i: i*i, list_input))
# print(list_input)

l = [i for i in range(10, 100)]
l1 = list(filter(lambda x: x % 9 == 0, l))
l2 = sum(list(map(lambda x: x**2, l1)))
print(l2)

