"""
This module contains the required functions of the shop
"""
from Gyakorlas.összetett import database

CART = []

# GENERAL FUNCTIONS ----------------------------------------------------------------------------------------------------


def get_shared_menu_items() -> list:
    items = [
        'Szerepkör cseréje',
        'Kilépés'
    ]

    return items

def list_items():
    acutal_items = database.get_all_item()

    for item in acutal_items:
        print(f'   {item[0]}. {item[1]} - Ár: {item[2]} Ft')


# CUSTOMER FUNCTIONS ---------------------------------------------------------------------------------------------------

def print_customer_menu():
    menu_items = [
        'Termékek listázása',
        'Termékek keresése',
        'Termékek kosárba helyezése',
        'Kosár listázása',
        'Fizetés'
    ]
    menu_items.extend(get_shared_menu_items())
    #menu_items + get_shared_menu_items()

    counter = 1

    for menu_item in menu_items:
        print(f'{counter}. {menu_item}')
        counter += 1

def search_item():
    search_value = input('Mit keresel: ')
    actual_items = database.get_all_item()

    for item in actual_items:
        name = item[1]

# OWNER FUNCTIONS -----------------------------------------------------------------------------------------------------