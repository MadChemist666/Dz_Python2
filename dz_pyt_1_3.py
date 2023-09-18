# Задача о проверке числа на простоту =)
def check_number():
    while True:
        num = int(input('Введите число от 0 до 100000: '))
        if not(0 <= num <= 100000 ):
            print('Неверное число')
        else:
            if num == 0 or num == 1:
                print(f'Число {num} не является ни простым ни составным')
                return
            else:
                k = 0
                for i in range(2, num // 2+1):
                    if (num % i == 0):
                        k = k+1
                if (k <= 0):
                    print(f'Число {num} простое')
                    return
                else:
                    print(f'Число {num} составное')
                    return

check_number()
