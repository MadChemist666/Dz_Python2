#Задача о кустах и комбайне
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = input(f'Укажите номер куста от 1 до {len(a)} ')
b = int(b)
if b == 1:
    c = a[0]+a[1]+a[-1]
    print(f'Макс. кол-во ягод для куста {b} равно {c}')
elif b == a[-1]:
    c = a[-2]+a[-1]+a[0]
    print(f'Макс. кол-во ягод для куста {b} равно {c}')
elif b in a:
    c = a[b]+a[b-1]+a[b-2]
    print(f'Макс. кол-во ягод для куста {b} равно {c}')
else:
    print('Неверно указан куст')
