import database
import view
import phone_book as pb

def choice_menu(choice):
    match choice:
        case 1:
            view.print_phone_book()
        case 2:
            database.load_contacts()
        case 3:
            database.save_contacts()
        case 4:
            pb.add_contact()
        case 5:
            pb.change_contact()
        case 6:
            pb.remove_contact()
        case 7:
            pb.search_contact()
            # view.print_book()
        case 0:
            return True

while True:
    choice = view.main_menu()
    if choice_menu(choice):
        break
