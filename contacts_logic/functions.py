import pathlib
from typing import Callable
current_dir = pathlib.Path(__file__).parent.absolute()
def read_contacts_from_file(): # Читає файл порядково, видаляючи непотрібні пробіли, як роздільник є ','
    contacts = {}
    try:
        with open(current_dir/ 'contacts.txt', 'r', encoding='utf-8') as file:
            for line in file:
                name, phone = line.strip().split(',')
                contacts[name.lower()] = phone

        return contacts
    except FileNotFoundError:
        print('File dose not exist or damaged.')

def file_writer(contacts: dict): # Відкриває файл та записує в нього надану інформацію
    try:
        with open(current_dir/ 'contacts.txt', 'w', encoding='utf-8') as file:
                for name, phone in contacts.items():
                    file.write(f'{name},{phone}\n')
    except FileNotFoundError:
        print('File Not Found.')

def input_error(func: Callable) -> Callable: # Decorator for catching errors in functions

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return 'Please enter a command followed by arguments.'
        except AttributeError:
            return 'Invalid input. Please enter a string.'
        except ValueError:
            return 'Please enter a command followed by arguments.'
    return inner
@input_error
def phone_username(args, contacts): # Функція для виведення вже створеного контакту, command == 'phone'
    name = args[0].lower()
    if name in contacts:
        return f'{name} phone is {contacts[name]}'
    else:
        return f'{name} does not exist.'


@input_error
def add_contact(args, contacts): # Функція для додавання нового контакту, command == 'add'
    name, phone = args
    contacts[name.lower()] = phone
    file_writer(contacts)
    return "Contact added."

@input_error
def change_contact(args, contacts): # Функція для зміни номера телефону, command == 'change'
    name, new_phone = args
    if name.lower() in contacts:
        contacts[name] = new_phone
        file_writer(contacts)
        return f'Contact {name} has been changed.'
    else:
        return f"Contact {name} not found."
