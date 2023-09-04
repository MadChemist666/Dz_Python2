# Задача о сумасбродном Винни-Пухе. Если закомментить все строки с print, то функция молча вернёт либо True либо False.
def winny(s):
    def countVowels(string):
        vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
        total = 0
        for s in string:
            if s in vowels:
                total += 1
        return total
    s = s.lower()
    count = []
    lst = s.replace('.', '').split()
    for i in range (0, len(lst)):
        count.append(countVowels(lst[i]))
    print(f'Количество гласных в соответствующих строках: {count}')
    if len(set(count)) == 1:
        print('Есть ритм')
        return True    
    else:
        print('Нет ритма')
        return False

# Проверка работы функции winny:
if winny('пара-ра-рам рам-паоом-папам па-ра-па-дам'):
    print ('ТРУ')
else:
    print ('ФОЛЗ')
