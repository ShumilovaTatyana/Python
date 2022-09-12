# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения
    
#     2) с помощью дополнительных библиотек Python\


def discriminant(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c


def solve_quadratic(a: float, b: float, c: float) -> str:
    if a == 0:
        raise ValueError("Not quadratic equation")

    d = discriminant(a, b, c)
    if d < 0:
        return "No roots"
    elif d == 0:
        return f"One root x = {-b / (2 * a)}"
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return f"Two roots: x1 = {x1}, x2 = {x2}"

if __name__ == "__main__":
    print(solve_quadratic(5, -9, -2))
    print(solve_quadratic(1, -4, 4))
    print(solve_quadratic(1, -5, 9))
    print(solve_quadratic(0, 1, 2))

# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# c = int(input('Введите c: '))
# res = Ax² + Bx + C 

# import math
# a = int(input("Введите значение a= "))
# b = int(input("Введите значение b= "))
# c = int(input("Введите значение c= "))
# D = b ** 2 - 4 * a * c
# print(D)
# if D < 0:
#   print("Корней нет")
# elif D == 0:
#   x = -b / 2 * a
#   print (x)
# else:
#   x1 = (-b + math.sqrt(D)) / (2 * a)
#   x2 = (-b - math.sqrt(D)) / (2 * a)
#   print(x1)
#   print(x2)

