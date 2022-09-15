
# НОД
# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". 
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.

# contains = lambda s, sample='ra': sample in s  
# s = input()
# print(contains(s))

#Наибольший общий делитель
# a = 123
# b = 23
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# print(a)

a = 123
b = 23
if a < b :
    a, b = b, a
while b!=0:
    a, b = b, a % b
print(a)
