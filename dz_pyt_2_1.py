# Программа "Банкомат".
def banko() -> None:
    windtraw_procent = 1.5
    bonus_procent = 3
    min_comission = 30
    max_comission = 600
    rich_tax_procent = 10
    rich_max = 5000000
    print('Программа "Банкомат"')
    s = 0
    flag = 0
    while True:
        print('1 - Пополнить')
        print('2 - Снять')
        print('3 - Выход')
        choise = int(input('Выберите действие: '))
        if choise == 1:
            if s > rich_max:
                print(f'Налог на роскошь {s/100*rich_tax_procent} ахахаха, буржуй поганый!')
                s -= s/100*rich_tax_procent                
            num = int(input('Введите сумму для пополнения, кратную 50: '))
            if num % 50 !=0 or num <=0:
                print('Неверная сумма')
            else:
                s += num
                flag += 1
                if flag % 3 == 0:
                    print(f'Вам начислен бонус в сумме {s/100*bonus_procent}')
                    s += s/100*bonus_procent
                print(f'Остаток на счете: {s}')
        if choise == 2:
            if s > rich_max:
                print(f'Налог на роскошь {s/100*rich_tax_procent} ахахаха, буржуй поганый!')
                s -= s/100*rich_tax_procent     
            num = int(input('Введите сумму для снятия, кратную 50: ')) 
            if num % 50 !=0 or num <=0 or num > s:                
                print('Неверная сумма')
                print(f'Остаток на счете: {s}')
            else:
                if num/100*windtraw_procent < min_comission:
                    x = min_comission
                elif num/100*windtraw_procent > max_comission:
                    x = max_comission
                else:
                    x = num/100*windtraw_procent
                if (num > x + s):
                    print('Недостаточно средств')
                    print(f'Остаток на счете: {s}')
                else:
                    s -= (num + x)
                    flag += 1
                    if flag % 3 == 0:
                        print(f'Вам начислен бонус в сумме{s/100*bonus_procent}')
                        s += s/100*bonus_procent
                print(f'Остаток на счете: {s}')
        if choise == 3:
            if s > rich_max:
                print(f'Налог на роскошь {s/100*rich_tax_procent} ахахаха, буржуй поганый!')
                s -= s/100*rich_tax_procent     
            print(f'Остаток на счете: {s}')
            print('Работа программы завершена.')
            return

banko()
            
            




