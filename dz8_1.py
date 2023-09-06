# Программа "Телефонный справочник"
import os
import csv

def get_userdata() -> list:
    name = input('Введите фамилию: ')
    sur_name = input('Введите имя: ')
    phone_num = input('Введите номер телефона: ')
    desc = input('Введите описание: ')
    return [name, sur_name, phone_num, desc]

def get_file_name() -> str:
    return input('Введите имя файла: ')

def create_from_data(gb_phone_book: list, file_name:str, delimetr:str) -> list:
    path_sourse= os.path.join('.',file_name)
    with open(path_sourse,'r', encoding='utf-8') as sourse:
        for line in sourse:
            gb_phone_book=create_record(gb_phone_book, line.strip().split(delimetr))
    return gb_phone_book

def create_record(gb_phone_book: list, user_data: list) -> list:
    gb_phone_book.append(user_data)
    return gb_phone_book

def print_phone_book(gb_phone_book: list) ->None:
    if len(gb_phone_book)==0: 
        print('Список пуст')
    else:
        for record in gb_phone_book:
            print(record)

def search(gb_phone_book:list) -> None:
    name = (input('Введите фамилию(можно не полностью): '))
    for record in gb_phone_book:
        if (''.join(record)).lower().startswith(name.lower()):
            print(record)
        
def export_to_file(phone_book:list, file_name:str) -> None:
    file = os.path.join('.',file_name)  
    with open(file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(phone_book) 

def delete_from_list(gb_phone_book:list)-> None:    
    name = (input('Введите фамилию(можно не полностью): '))
    for record in gb_phone_book:
        if (''.join(record)).lower().startswith(name.lower()):
           gb_phone_book.remove(record)
           print (f'{record} - удалено.')

def update_record(gb_phone_book:list)-> None:
    name = (input('Введите фамилию(можно не полностью): '))
    for record in gb_phone_book:
        if (''.join(record)).lower().startswith(name.lower()):
            print(f'Внесите изменения для записи {record}')
            #record[0]= input('Введите фамилию: ')  #Раскомментить, если надо менять и фамилию (здесь не ясно поставлена задача, или я её не понял)
            record[1]= input('Введите имя: ')
            record[2]= input('Введите номер телефона: ')
            record[3]= input('Введите описание: ')
        
    
def menu():
    print('Вас приветствует программа "MS-ЁЖИК" - самый надёжный телефонный справочник! ver. 0.5C2H5OH')
    phone_book = list()
    while True:
        print('1 - создание новой записи.')
        print('2 - вывод справочника на экран')
        print('3 - импорт справочника из файла')
        print('4 - поиск записи')
        print('5 - экспорт справочника в файл')
        print('6 - удаление записи из справочника')
        print('7 - редактирование записи справочника')
        print('8 - выход из программы.')
        choise = int(input('Выберите действие: '))       
        if choise == 1:
            phone_book = create_record(phone_book, get_userdata())
        if choise == 2:
            print_phone_book(phone_book)
        if choise == 3:
           phone_book= create_from_data(phone_book, get_file_name(), ',')
           print('Данные из файла импортированы')
        if choise == 4:
            search(phone_book)
        if choise == 5:
            print('ВНИМАНИЕ! При экспорте в уже существующий файл, все данные в нём будут перезаписаны!')
            export_to_file(phone_book, get_file_name())
            print('Данные успешно экспортированы в файл')
        if choise == 6:
            print('ВНИМАНИЕ! Все соответствующие записи будут удалены!')
            delete_from_list(phone_book)
        if choise == 7:
            update_record(phone_book)
        if choise == 8:
            print('Работа программы завершена.')
            return    

menu()

 

