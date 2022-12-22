import phone_book as pb
import view

path = r'phone_base.txt'

def load_contacts() -> list:
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    book = pb.set_phone_book(str_to_list(data))
    print('Телефонная книга загружена\n')
    return book


def save_contacts():
    global path
    ready_book = list_to_str(pb.get_phone_book())
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(ready_book)
    print('Телефонная книга сохранена\n')

def list_to_str(phone_book: list) -> str:
    str_phone_book = ''
    for contact in phone_book:
        new_contact = ';'.join(contact)
        str_phone_book += new_contact +'\n'
    return str_phone_book[:-1]

def str_to_list(phone_book: list) -> list:
    new_list = []
    for contact in phone_book:
        new_contact = contact.strip().split(';')
        new_list.append(new_contact)
    return new_list

def res_program():
    print('Что делаем дальше?')
    return view.main_menu()
