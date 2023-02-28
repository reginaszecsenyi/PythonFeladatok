"""
This is the main module of the practice. Use this for running the application.
"""
import shop

# SETTINGS -------------------------------------------------------------------------------------------------------------
CURRENT_ROLE = 'customer'

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':


    print('Üdvözöllek a boltban!\n')

    while True:
        shop.print_customer_menu()

        selected_menu_item = input('Adj meg egy menüpontot:')

        if selected_menu_item == '1':
            shop.list_items()
        elif selected_menu_item == '2':
            print('Keresés')
        elif selected_menu_item == '3':
            print('Kosárba tevés')
        elif selected_menu_item == '4':
            print('Kosár listázása')
        elif selected_menu_item == '5':
            print('Fizetés')
        elif selected_menu_item == '6':
            print('Szerepkör csere')
        elif selected_menu_item == '7':
            print('Kilépés')
        else:
            print('Ilyen menüpont nincs.')

        print('-' *60)

        break
