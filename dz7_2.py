#Задача о функции и таблицах.
def print_operation_table(oper,x=6, y=6):
      for i in range(1, x+1):
            for j in range(1, y+1):   
                print("%4d" % (oper(i,j)), end='')
            print()

# Проверка функции.
print (print_operation_table(lambda x, y: x**y, 4,4))

# P.S. Не смог найти информацию как сделать форматированную таблицу с номерами строк и столбцов. :(

