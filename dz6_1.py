# Задача о прогрессии.
# Усложнение. Присвоение значений переменным запишите, используя только один input, в одну строку.
def progres(x,y,z):
    lst = []
    lst.append(x)
    for i in range(1, z):
        x += y
        lst.append(x)
    return(lst)

list_1 = input('Введите через пробел начальное знанчение, шаг и кол-во элементов: ')
list_2 = (list_1.replace('.', '').split())
list_2 = [int(i) for i in list_2]
print(progres(list_2[0], list_2[1], list_2[2]))