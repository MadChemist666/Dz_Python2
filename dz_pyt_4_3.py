# Программа "Банкомат" Разделение на функции + список всех операций.
def banko() -> None:
    print('Программа "Банкомат"')
    s = 0
    flag = 0
    while True:
        print('1 - Пополнить')
        print('2 - Снять')
        print('3 - Выход')
        print('4 - Вывод списка всех операций')
        choise = int(input('Выберите действие: '))
        if choise == 1:
            s += cash_up(s)
            flag += 1
            if flag % 3 == 0:
                print(f'Вам начислен бонус в сумме {s/100*bonus_procent}')
                operations_list.append(s/100*bonus_procent)
                operations_list.append('- Бонусное начисление')   
                s += s/100*bonus_procent
        if choise == 2:
            s -= cash_down(s)
            flag += 1
            if flag % 3 == 0:
                print(f'Вам начислен бонус в сумме {s/100*bonus_procent}')
                operations_list.append(s/100*bonus_procent)
                operations_list.append('- Бонусное начисление')   
                s += s/100*bonus_procent
        if choise == 3:
            exit_x(s)
            return
        if choise == 4:
             for count in range(len(operations_list)):
                  print(operations_list[count], end=" ")
                  if count % 2 != 0:
                       print()
            
def cash_up(s):
    if s > rich_max:
                print(f'Налог на роскошь {s/100*rich_tax_procent}')
                operations_list.append(s/100*rich_tax_procent)
                operations_list.append('- Налог на роскошь')  
                s -= s/100*rich_tax_procent                            
    num = int(input('Введите сумму для пополнения, кратную 50: '))
    if num % 50 !=0 or num <=0:
        print('Неверная сумма')
    else:
        s += num
        operations_list.append(num) 
        operations_list.append('- Пополнение')                                             
        print(f'Остаток на счете: {s}')
        return s

def cash_down(s):
    if s > rich_max:
                print(f'Налог на роскошь {s/100*rich_tax_procent} ')
                operations_list.append(s/100*rich_tax_procent)
                operations_list.append('- Налог на роскошь')  
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
            operations_list.append(num + x) 
            operations_list.append('- Снятие')   
    print(f'Остаток на счете: {s}')
    return s

def exit_x(s):
    if s > rich_max:
                print(f'Налог на роскошь {s/100*rich_tax_procent} ')
                operations_list.append(s/100*rich_tax_procent)
                operations_list.append('- Налог на роскошь')   
                s -= s/100*rich_tax_procent               
    print(f'Остаток на счете: {s}')
    print('Работа программы завершена.')
    return


operations_list = []
windtraw_procent = 1.5
bonus_procent = 3
min_comission = 30
max_comission = 600
rich_tax_procent = 10
rich_max = 5000000
banko()
            