#Задача о дробях
from math import lcm, gcd
num_1 = input('Введите 1-ю дробь в виде x/y: ')
lst = num_1.replace('.', '').split('/')
num_2 = input('Введите 2-ю дробь в виде x/y: ')
lst_2 = num_2.replace('.', '').split('/')
a = int(lst[0])
b = int(lst[1])
c = int(lst_2[0])
d = int(lst_2[1])
bd = lcm(b, d)
rn = bd//b * a + bd//d * c
g2 = gcd(rn, bd)
n = rn//g2
d = bd//g2
e = a*c
f = b*d
k = gcd(e,f)
e = e//k
f = f//k
print(f'Сумма дробей = {n}/{d}')
print(f'Произведение дробей = {e}/{f}')