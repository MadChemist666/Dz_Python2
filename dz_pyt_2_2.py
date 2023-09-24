# Преобразование HEX
num = int(input('Введите число для преобразования: '))
#print(hex(num))
s = ''
h = '0123456789ABCDEF'
while num > 0:
    s = h[num % 16] + s
    num = num // 16
print(s)

