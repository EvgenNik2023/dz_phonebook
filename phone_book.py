def output(list1: list) -> None:
    print()
    count = 1
    for i in list1:
        print(str(count) + '. ' + i, end='')
        count+=1
    print()
    

def show_all(file_name: str) -> None:
       
    with open(file_name, 'r', encoding='utf-8') as fd:
        data = fd.readlines()
        return data


def find_human(file_name: str) -> str:
    with open(file_name, 'r', encoding='utf-8') as fd:
        date = fd.readlines()        
        i = int(input('Введите 0 для поиска по фамилии или 1 для поиска по имени: '))
        marker = input('Введите имя(фамилию): ')
        res = list(filter(lambda x: x.split(', ')[i] == marker, date))
        
    while len(res) == 0:
        q = input('  Нет данных. Нажмите 1 для продолжения поиска или 2 для выхода в основное меню ')
        if q == '1':
            i = int(input('Введите 0 для поиска по фамилии или 1 для поиска по имени: '))
            marker = input('Введите имя(фамилию): ')
            res = list(filter(lambda x: x.split(', ')[i] == marker, date))
        else:
            return res
            
    output(res)

    if len(res) > 1:
        q = int(input('Для уточнения введите порядковый номер контакта: ')) - 1
        res = [res[q]]

    print()
    return res


def copy_from_other_list(file_name: str) -> None:
    file = input('Введите имя файла для поиска: ')
    data = find_human(file)
    copy_data = ''.join(data)

    with open(file_name, 'a', encoding='utf-8') as fd:
        fd.write (copy_data)
                

def remove(file_name: str) -> None:
    
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    
    with open(file_name, 'r', encoding='utf-8') as fd:
        date = fd.readlines()
        print(date)
        s = f'{last_name}, {first_name}, {patronymic}, {phone_number}\n'
        date.remove(s)
        
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(date)


def add_new(file_name: str) -> None:
    
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')

    with open(file_name, 'a', encoding='utf-8') as fd:
        fd.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')


def replace(file_name: str) -> None:
    print('Введите данные для поиска')
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    print('Введите новые данные')
    new_last_name = input('Введите фамилию: ')
    new_first_name = input('Введите имя: ')
    new_patronymic = input('Введите отчество: ')
    new_phone_number = input('Введите номер телефона: ')
    
    with open(file_name, 'r+', encoding='utf-8') as fd:
        date = fd.readlines()

        s = f'{last_name}, {first_name}, {patronymic}, {phone_number}\n'
        i = date.index(s)
        new_s = f'{new_last_name}, {new_first_name}, {new_patronymic}, {new_phone_number}\n'
        date.remove(s)
        date.insert(i, new_s)

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(date)


def main():
    file_name = 'phonebook.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - показать все записи')
        print('2 - добавить запись')
        print('3 - удалить запись')
        print('4 - изменить запись')
        print('5 - поиск абонента')
        print('6 - копирование контакта')

        answer = input('Введите операцию или x для выхода: ')
        if answer == '1':
            output(show_all(file_name))
        elif answer == '2':
            add_new(file_name)
        elif answer == '3':
            remove(file_name)
        elif answer == '4':
            replace(file_name)
        elif answer == '5':
            output(find_human(file_name))
        elif answer == '6':
            copy_from_other_list(file_name)
        elif answer == 'x':
            flag_exit = True


if __name__ == '__main__':
    main()