import database
import view

phone_book = []

def get_phone_book() -> list:
    global phone_book
    return phone_book

def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book

def add_contact():
    global phone_book
    contact = view.input_new_contact()
    phone_book.append(contact)

def change_contact():

    global phone_book
    database.load_contacts()
    view.print_phone_book()
    temp_phone_book = phone_book
    print(temp_phone_book)
    field_contact = view.data_search()
    print(f'field_contact = {field_contact}')
    field_change = view.data_change_collection()
    print(f'field_change = {field_change}')
    variant = view.data_collection()
    print(f'variant = {variant}')
    nov_book = []
    for string_contact in temp_phone_book:
        print(f'string_contact = {string_contact}')
        for item in range(len(string_contact)):
            print(f'item = {item}')
            if string_contact[item] == variant:
                string_contact[item] = field_change
                print(f'item = {item}')
                print(f'string_contact = {string_contact}')
                nov_book.append(str(string_contact))
                print(f'new_phone_book = {nov_book}')
            else:
                print('Этот контакт не подходит. Идем дальше')
                continue
    if len(list(nov_book)) > 0:
        print(f'Посмотрите найденные контакты: ')
        # for word in nov_book:
        #     if word == variant:
        #         word = field_change
        #         print(f'word = {word}')
        print(f'nov_book = {nov_book}')
    else:
        print('Такого контакта в базе нет')

def remove_contact():
    global phone_book
    id = view.input_remove_contact()
    confirm = input(f'Вы точно хотите удалить контакт {phone_book[id-1][0]}? (y/n)')
    if confirm.lower() == 'y':
        del_contact = phone_book.pop(id-1)
    return phone_book


def search_contact():
    global phone_book
    database.load_contacts()
    view.print_phone_book()
    temp_phone_book = phone_book
    print(temp_phone_book)
    field_contact = view.data_search()
    print(f'field_contact = {field_contact}')
    variant = view.data_collection()
    print(f'variant = {variant}')
    nov_book = []
    for string_contact in temp_phone_book:
        print(f'string_contact = {string_contact}')
        for item in string_contact:
            print(f'item = {item}')
            if item == variant:
                nov_book.append(str(string_contact) + '\n')
                print(f'new_phone_book = {nov_book}')
            else:
                print('Этот контакт не подходит. Идем дальше')
                continue
    if len(nov_book) > 0:
        print(f'Посмотрите найденные контакты: ')
        print(f'nov_book = {nov_book}')
    else:
        print('Такого контакта в базе нет')
    return nov_book


def change_element(my_list):
    for itemc in my_list:
        print(itemc)
        temp = itemc[0]
        itemc[0] = itemc[1]
        itemc[1] = itemc[2]
        itemc[2] = temp
        print(itemc)
        break

def row_change_selection(variant, field_change, temp_phone_book):
    global phone_book
    new_phone_book = []
    while len(temp_phone_book) > 0:
        for i in range(3):
            if variant == temp_phone_book[i]:
                temp_phone_book[i] = field_change
                for j in range(3):
                    new_phone_book.append(i + '. ' + temp_phone_book[j] + ';')
                new_phone_book.append('\n')
                for m in range(3):
                    temp_phone_book.remove(temp_phone_book[0])
            else:
                continue
        return temp_phone_book
    return new_phone_book
