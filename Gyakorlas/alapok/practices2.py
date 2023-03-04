"""
Ebben a fájlban találjátok a feladat megfogalmazásokat.
Javaslat: az adott feladatot oldjátok meg függvényben.
Így a main.py fájlból tudjátok meghívni, ami segíti majd az átláthatóságot.
Példa:
"""


# Feladat 0:
# Témakörök: írás kimenetre
# Írj egy függvényt, ami kiírja a kimenetre a következő szöveget: 'Csak minta szerepem van. :)'
def example_function():
    print('Csak minta szerepem van. :)')


# ----------------------------------------------------------------------------------------------------------------------

# Feladat 1:
# Témakörök: INPUT, SZÁMOK, STRINGEK
# Írj függvényt, ami bekér egy tetszőleges számot a felhasználótól.
# A kapott számon elvégzi a következő műveleteket:
# - Négyzetre emeli (**)
# - Elosztja 3-al és kiírja az osztás egész értékét (//)
# - Kiírja a 'cool' szöveget annyiszor, ahányas számot megadott a felhasználó
# Pl. 3 -> coolcoolcool (NEM kell ciklust használni, sima alapművelet elég!)

def task10():
    number = int(input('Adj meg egy tetszőleges számot:'))

    print(number ** 2)
    print(number // 3)
    print(number * 'cool')


# ----------------------------------------------------------------------------------------------------------------------

# Feladat 2:
# Témakörök: INPUT, STRINGEK, IF
# Írj függvényt, ami bekér egy tetszőleges szöveget a felhasználótól.
# A kapott szövegen elvégzi a következő műveleteket:
# - Teljes kisbetűssé alakítja (lower)
# - Ellenőrzi, hogy szerepel-e benne az 'egy' kifejezés ('egy' in szoveg)
# - Ellenőrzi, hogy 'A' betűvel kezdődik (startswith) és '.'-al végződik-e (endswith)
# - Minden második betűt írja csak ki a szövegből (slicing 3 értéke!)

def task11():
    szoveg = input('Adj meg egy tetszőleges szöveget:')

    print(szoveg.lower())
    print('egy' in szoveg)
    print(szoveg.startswith('A'))
    print(szoveg.endswith('.'))
    print(szoveg[1::2])


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

def task12():
    szoveg1 = input('Adj meg egy tetszőleges szöveget:')

    szavak = szoveg1.split()
    print(szavak)
    print(szavak[::-1])

    joined_szavak = ' '.join(szavak[::-1])
    print(joined_szavak)


# ----------------------------------------------------------------------------------------------------------------------

# Feladat 4:
# Témakörök: Ciklusok - while
# Írj függvényt, ami addig kér be tetszőleges szöveget a felhasználótól, amíg 'exit'-et nem ír be.
# Minden felhasználói inputot írj ki a terminálra visszafelé, csupa nagybetűvel.  string[::-1], upper()

def task13():
    while True:
        user_input = input('Adj meg egy tetszőleges szöveget:')
        if user_input.lower() == 'exit':
            break

        print(user_input[::-1].upper())


# ----------------------------------------------------------------------------------------------------------------------

# Feladat 5:
# Témakörök: Ciklusok - while, Listák
# Írj függvényt, ami addig kér be tetszőleges szöveget a felhasználótól, amíg az 'end'-et nem ír be.
# Gyűjtsd a beírt szövegeket egy listába.
# A bevitel után írd ki a kapott szövegeket abc ill. fordított sorrendben is. sort(), sort(reversed=True)

def task14():
    list = []

    while True:
        user_input = input('Adj meg egy tetszőleges szöveget:')

        if user_input.lower() == 'end':
            break
        else:
            list.append(user_input)

    print(list)

    list.sort()
    print(list)

    list.sort(reverse=True)
    print(list)


# ----------------------------------------------------------------------------------------------------------------------

# Feladat 6:
# Témakörök: IF-ELSE, Ciklusok - For
# Írj függvényt, ami bekér egy 50-nél nagyobb számot a felhasználótól.
# Ha 50-nél kisebb a szám, akkor jelzi ezt a problémát egy üzenetben.
# Ha nagyobb, akkor for ciklussal végighalad a lenn megadott szám listán, és minden számmal megpróbálja elosztani a kapott számot.
# Az eredménynek megfelelően kiírja, hogy a kapott szám osztható-e maradék nélkül az aktuális lista számmal.
# Nem kell try-except-et használni, csak ha szeretnél. :)

def task15():
    osztok = [2, 3, 5, 10]

    szam = int(input('Adj meg egy 50-nél nagyobb számot:'))

    if szam < 50:
        print('Ez a szám nem megfelelő, mert kisebb, mint 50.')
    else:
        for n in osztok:
            if szam % n == 0:
                print(f'A {szam} maradék nélkül osztható {n}-el.')
            else:
                print(f'A {szam} maradék nélkül nem osztható {n}-el.')


# ----------------------------------------------------------------------------------------------------------------------

# Feladat 7:
# Témakörök: Beépített függvények, Ciklusok - For, Listák, Függvények
# Írj függvényt, ami a paraméterben kapott számlistára
# - Kiírja, hogy hány elemet tartalmaz. len
# - kiszámolja a teljes összegét. sum
# - Kiszámolja az átlagát, miután kiegészítetted a következő listával: [324, 23, 525] extend
# Hívd meg a függvényt a main-ből különböző listákra!

def task16(list = [1, 2, 3, 4, 5]):

    print(len(list))
    print(sum(list))

    list.extend([324, 23, 525])
    print(list)

    print(sum(list) / len(list))

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

def task17():
    directories = {
        'temp': ['01.txt', 'sun.jpg'],
        'fun': ['idezetek.txt', 'mrbean.gif']
    }
    for kulcs, ertek in directories.items():
        print(kulcs)
        files = ', '.join(ertek)
        print(f'--->{files}')



# ----------------------------------------------------------------------------------------------------------------------

# Feladat 9:
# Témakörök: Fájl kezelés
# Írj függvényt, ami soronként beolvassa a files\books.txt fájlt és
# kiírja az aktuális sor tartalmát és az adott sor hosszát
# Például: A programozás alapjai --> A programozás alapjai (Sor hossza: 21)

def task18():
    # Megoldás ide
    pass


# ----------------------------------------------------------------------------------------------------------------------

# Feladat 10:
# Témakörök: Input, Fájl kezelés
# Írj függvényt, ami bekér 3 adatot a felhasználótól (név, életkor, kedvenc étel)
# Majd hozzáfűzi a files\users.txt-hez ezeket az adatokat 1 új sorként. Pl: Anna 12 palacsinta
# Segítség: hozzáfűzés/append --> open(path, 'a', encoding='UTF-8')

def task19():
    # Megoldás ide
    pass
