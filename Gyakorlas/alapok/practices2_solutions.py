"""
Ebben a fájlban találjátok a feladatok lehetséges megoldásait.
A futtatásukhoz a main.py-ban át kell írni az importot!
"""
# ----------------------------------------------------------------------------------------------------------------------

# Feladat 1:
# Témakörök: INPUT, SZÁMOK, STRINGEK
# Írj függvényt, ami bekér egy tetszőleges számot a felhasználótól.
# A kapott számon elvégzi a következő műveleteket:
# - Négyzetre emeli (**)
# - Elosztja 3-al és kiírja az osztás egész értékét (//)
# - Kiírja a 'cool' szöveget annyiszor, ahányas számot megadott a felhasználó
# Pl. 3 -> coolcoolcool (NEM kell ciklust használni, sima alapművelet elég!)

def task1():
    number = int(input('Adj meg egy számot: '))
    print(f'A szám négyzete: {number**2}')
    print(f'{number}/3 egész értéke: {number//3}')
    repeated_text = 'cool' * number
    print(f'Szöveg ismétlése: { repeated_text }')


# ----------------------------------------------------------------------------------------------------------------------

# Feladat 2:
# Témakörök: INPUT, STRINGEK, IF
# Írj függvényt, ami bekér egy tetszőleges szöveget a felhasználótól.
# A kapott szövegen elvégzi a következő műveleteket:
# - Teljes kisbetűssé alakítja (lower)
# - Ellenőrzi, hogy szerepel-e benne az 'egy' kifejezés ('egy' in szoveg)
# - Ellenőrzi, hogy 'A' betűvel kezdődik (startswith) és '.'-al végződik-e (endswith)
# - Minden második betűt írja csak ki a szövegből (slicing 3 értéke!)

def task2():
    user_input = input('Adj meg egy tetszőleges szöveget: ')

    print(user_input.lower())

    if "egy" in user_input:
        print('Benne van az "egy" kifejezés!')
    else:
        print('Nincs benne az "egy" kifejezés!')

    if user_input.startswith('A') and user_input.endswith('.'):
        print('A-val kezdődik ÉS .-al végződik!')
    else:
        print('Nem igaz, hogy A-val kezdődik ÉS .-al végződik!')

    print(f'Minden második betű: {user_input[::2]}')

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 3:
# Témakörök: INPUT, STRINGEK, LISTÁK
# Írj függvényt, ami bekér egy tetszőleges szöveget a felhasználótól.
# A kapott szövegen elvégzi a következő műveleteket:
# - A szövegben található szavakat külön listába teszi (split)
# - Megfordítja a szó lista elemeinek sorrendjét: ['Ez', 'egy', 'példa'] -> ['példa', 'egy', 'Ez']
#   Segítség: mint string kiíratása visszafelé slice technikával: lista[::-1]
# - A megfordított lista elemeit összefűzi space-ekkel, amit változóban tárol. ' '.join()
# - Kiírja a fordított szó sorrendben lévő stringet
# Példa: Ez egy szöveg -> szöveg egy Ez

def task3():
    user_input = input('Adj meg egy tetszőleges szöveget: ')

    word_list = user_input.split()
    word_list = word_list[::-1]
    new_order_string = ' '.join(word_list)
    print(new_order_string)

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 4:
# Témakörök: Ciklusok - while
# Írj függvényt, ami addig kér be tetszőleges szöveget a felhasználótól, amíg 'exit'-et nem ír be.
# Minden felhasználói inputot írj ki a terminálra visszafelé, csupa nagybetűvel.  string[::-1], upper()

def task4():

    while True:
        user_input = input('Adj meg egy tetszőleges szöveget: ')
        if user_input == 'exit':
            break

        print(user_input[::-1].upper())

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 5:
# Témakörök: Ciklusok - while, Listák
# Írj függvényt, ami addig kér be tetszőleges szöveget a felhasználótól, amíg az 'end'-et nem ír be.
# Gyűjtsd a beírt szövegeket egy listába.
# A bevitel után írd ki a kapott szövegeket abc ill. fordított sorrendben is. sort(), sort(reverse=True)

def task5():

    inputs = []

    while True:
        user_input = input('Adj meg egy tetszőleges szöveget: ')
        if user_input == 'end':
            break

        inputs.append(user_input)

    print('Kapott értékek ABC sorrendben:')
    inputs.sort()
    print(inputs)
    print('Kapott értékek fordított ABC sorrendben:')
    inputs.sort(reverse=True)
    print(inputs)

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 6:
# Témakörök: IF-ELSE, Ciklusok - For
# Írj függvényt, ami bekér egy 50-nél nagyobb számot a felhasználótól.
# Ha 50-nél kisebb a szám, akkor jelzi ezt a problémát egy üzenetben.
# Ha nagyobb, akkor for ciklussal végighalad a lenn megadott szám listán, és minden számmal megpróbálja elosztani a kapott számot.
# Az eredménynek megfelelően kiírja, hogy a kapott szám osztható-e maradék nélkül az aktuális lista számmal.
# Nem kell try-except-et használni, csak ha szeretnél. :)

def task6():
    number = int(input('Adj meg egy 50-nél nagyobb számot: '))

    if number < 50:
        print('Nem 50-nél nagyobb számot adtál meg!')
    else:
        osztok = [2, 3, 5, 10]
        for oszto in osztok:
            if number % oszto == 0:
                print(f'A kapott szám ({number}) osztható {oszto} -el maradék nélkül.')
            else:
                print(f'A kapott szám ({number}) nem osztható {oszto} -el maradék nélkül.')

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 7:
# Témakörök: Beépített függvények, Ciklusok - For, Listák, Függvények
# Írj függvényt, ami a paraméterben kapott számlistára
# - Kiírja, hogy hány elemet tartalmaz. len
# - kiszámolja a teljes összegét. sum
# - Kiszámolja az átlagát, miután kiegészítetted a következő listával: [324, 23, 525] extend
# Hívd meg a függvényt a main-ből különböző listákra!

def task7(numbers: list = [1, 2, 3, 4, 5]):

    print(f'A számlista {len(numbers)} elemet tartalmaz')
    total = sum(numbers)
    print(f'A listában található számok összege: {total}')

    numbers.extend([324, 23, 525])
    average = sum(numbers) / len(numbers)
    print(f'A kiegészített lista átlaga: {average}')


# ----------------------------------------------------------------------------------------------------------------------

# Feladat 8:
# Témakörök: Ciklusok - For, Dictionary
# Írj függvényt, ami az alábbi dictionary-ből kiírja a kulcsokat a következő formában:
    # mappa1
    # ---> fajl1 fajl2 ...
    # mappa2
    # ---> fajl3, fajl4
    # Mintha mappa szerkezetet jelenítenél meg. Kulcsok = mappák, értékek = fájlok
    # Segítség: for kulcs, ertek in pelda.items()

def task8():
    directories = {
        'temp': ['01.txt', 'sun.jpg'],
        'fun': ['idezetek.txt', 'mrbean.gif']
    }

    for key, value in directories.items():
        print(key)
        files_in_string = ', '.join(value)
        print(f'---> {files_in_string}')

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 9:
# Témakörök: Fájl kezelés
# Írj függvényt, ami soronként beolvassa a files\books.txt fájlt és
# kiírja az aktuális sor tartalmát és az adott sor hosszát
# Például: A programozás alapjai --> A programozás alapjai (Sor hossza: 21)

def task9():

    with open(r'files\books.txt', 'r', encoding='UTF-8') as books_file:
        for line in books_file:
            print(f'{line[:-1]} (Sor hossza: {len(line)})')

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 10:
# Témakörök: Input, Fájl kezelés
# Írj függvényt, ami bekér 3 adatot a felhasználótól (név, életkor, kedvenc étel)
# Majd hozzáfűzi a files\users.txt-hez ezeket az adatokat 1 új sorként. Pl: Anna 12 palacsinta
# Segítség: hozzáfűzés/append --> open(path, 'a', encoding='UTF-8')

def task10():
    name = input('Kérlek, add meg a neved: ')
    age = input('Add meg az életkorod: ')
    favorite_meal = input('Add meg a kedvenc ételed: ')

    new_line = f'{name} {age} {favorite_meal}\n'

    with open(r'files\users.txt', 'a', encoding='UTF-8') as users_file:
        users_file.write(new_line)

