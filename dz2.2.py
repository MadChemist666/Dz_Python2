# Задача "Отгадай числа"
import math
b=int(input('Введите сумму: '))
c=int(input('Введите произведение: '))
d=(b*b - 4*c)
x1= int((b+int(math.sqrt(d)))/2)
x2= int((b-int(math.sqrt(d)))/2)

print(x1,x2)

#P.S Если Катя ещё не проходила в школе квадратные уравнения - то Петя ублюдок!=)