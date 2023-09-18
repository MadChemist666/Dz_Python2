# Задача о треугольниках.
list_1 = input('Введите через пробел длины сторон треугольника: ')
list_2 = (list_1.replace('.', '').split())
list_2 = [int(item) for item in list_2]

def triangle(x, y, z) -> None: 
    if x + y <= z or x + z <= y or y + z <= x:
        print(f'Треугольник со сторонами {x}, {y}, {z} не существует')
    else:
        if x**2 == y**2 + z**2 or y**2 == x**2 + z**2 or z**2 == y**2 + x**2:
            print(f'Треугольник со сторонами {x}, {y}, {z} прямоугольный')
        if x == y == z:
            print(f'Треугольник со сторонами {x}, {y}, {z} равносторонний')
        elif x == y or x ==z or z == y:
            print(f'Треугольник со сторонами {x}, {y}, {z} равнобедренный')
        else:
            print(f'Треугольник со сторонами {x}, {y}, {z} разносторонний')
    return

triangle(list_2[0], list_2[1] ,list_2[2])