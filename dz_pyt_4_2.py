# Функция хеш словарь
def strange_func(*args):
    temp_dict = args
    #print(temp_dict)
    res = {}
    for i in range(len(temp_dict)):
        if temp_dict[i].__hash__ is not None:               # Не работает с нехешируемым объектом. Не знаю почему. В сети искал 4 часа - ничего не нашёл =( Сдаюсь крч.
            res[temp_dict[i]] = hash(temp_dict[i])
        else:
            res[temp_dict[i]] = (temp_dict[i])
    
    return(res)


print(strange_func(5,6,7, 'a', 'b', [4,3]))

