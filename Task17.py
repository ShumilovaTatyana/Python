# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# (1+1/n)**n

n = int(input("Введите число : "))
sum = 0
for i in range (1, n + 1):
    a = (1 + 1 / i)**i 
    sum += a
    print(a, end=" ")
print(f"Сумма равна:  {sum}")


# n = int(input('Введите число: ')) 

# def sequence(n):

#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
# print(sequence(n))
# print('Сумма последовательности =', round(sum(sequence(n)),2))


# n = int(input('Введите число: '))
# sum = 0
# for n in range(1, n+1):
#     sum = sum + round((1 + 1 / n)**n, 2)
# print(sum)


# num = int(input("Введите число N для последовательности $(1+1/n)^n$: "))
# res_list = list((1+1/i)**i for i in range(1, num + 1))
# print(f'sum for 3 = {round(sum(res_list), 3)}')





