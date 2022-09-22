# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

numbers = [1, 2, 3, 5, 1, 5, 3, 10] 
result = []
for number in numbers:
    if numbers.count(number) == 1:  
        result.append(number)
print(result)   





