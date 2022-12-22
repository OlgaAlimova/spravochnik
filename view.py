import phone_book as pb

def main_menu():
    print('Выберите команду меню:')
    print('1. Показать телефонную книгу')
    print('2. Загрузить телефонную книгу')
    print('3. Сохранить телефонную книгу')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выйти из приложения\n')
    return input_menu()

def input_menu():
    while True:
        try:
            choice = int(input('Введите пункт меню: '))
            if choice in range(1, 8) or choice == 0:
                return choice
            else:
                print('Такого пункта меню нет. Внимательнее, пожалуйста')
        except:
            print('Ошибка ввода. Введите корректный пункт меню')

def print_phone_book():
    phone_book = pb.get_phone_book()
    print()
    if len(phone_book) < 1:
        print('Телефонная книга пуста или не загружена\n')
    else:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    print()

def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий контакта: ')
    new_contact = [name, phone, comment]
    return new_contact

def input_remove_contact():
    print()
    print_phone_book()
    id = int(input('Введите ID контакта, который стоит удалить: '))
    return id

def data_search():
    print('Выберите поле, по которому будем искать контакт:')
    print('1. Name')
    print('2. Phone')
    print('3. Comment')
    print('0. Выйти в основное меню')
    return input_search_menu()

def input_search_menu():
    while True:
        try:
            choice = int(input('Введите пункт меню: '))
            if choice in range(1, 4) or choice == 0:
                return choice
            else:
                print('Такого пункта меню нет. Внимательнее, пожалуйста')
        except:
            print('Ошибка ввода. Введите корректный пункт меню')

def data_collection():

    field_search = input(f'Отлично! Введите значение, которое необходимо найти: ')
    return field_search


def data_change_collection():

    field_change = input(f'Хорошо! Введите значение, на которое будем менять: ')
    return field_change
