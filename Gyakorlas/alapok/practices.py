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

def task1():
    number = int(input('Adj meg egy tetszőleges számot: '))
    print(f'A szám négyzete: {number ** 2}')
    print(f'Hárommal osztva: {number//3}')
    print('cool' * number)

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
    szoveg = input('Adj meg egy tetszőleges szöveget: ')
    print(szoveg.lower())
    print('egy' in szoveg)
    print(szoveg.startswith('A') or szoveg.endswith('.'))
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

def task3():
    # Megoldás ide
    pass

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 4:
# Témakörök: Ciklusok - while
# Írj függvényt, ami addig kér be tetszőleges szöveget a felhasználótól, amíg 'exit'-et nem ír be.
# Minden felhasználói inputot írj ki a terminálra visszafelé, csupa nagybetűvel.  string[::-1], upper()

def task4():
    # Megoldás ide
    pass

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 5:
# Témakörök: Ciklusok - while, Listák
# Írj függvényt, ami addig kér be tetszőleges szöveget a felhasználótól, amíg az 'end'-et nem ír be.
# Gyűjtsd a beírt szövegeket egy listába.
# A bevitel után írd ki a kapott szövegeket abc ill. fordított sorrendben is. sort(), sort(reversed=True)

def task5():
    # Megoldás ide
    pass

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 6:
# Témakörök: IF-ELSE, Ciklusok - For
# Írj függvényt, ami bekér egy 50-nél nagyobb számot a felhasználótól.
# Ha 50-nél kisebb a szám, akkor jelzi ezt a problémát egy üzenetben.
# Ha nagyobb, akkor for ciklussal végighalad a lenn megadott szám listán, és minden számmal megpróbálja elosztani a kapott számot.
# Az eredménynek megfelelően kiírja, hogy a kapott szám osztható-e maradék nélkül az aktuális lista számmal.
# Nem kell try-except-et használni, csak ha szeretnél. :)

def task6():
    osztok = [2, 3, 5, 10]
    pass

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 7:
# Témakörök: Beépített függvények, Ciklusok - For, Listák, Függvények
# Írj függvényt, ami a paraméterben kapott számlistára
# - Kiírja, hogy hány elemet tartalmaz. len
# - kiszámolja a teljes összegét. sum
# - Kiszámolja az átlagát, miután kiegészítetted a következő listával: [324, 23, 525] extend
# Hívd meg a függvényt a main-ből különböző listákra!

def task7(numbers: list = [1, 2, 3, 4, 5]):
    # Megoldás ide
    pass


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
    pass

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 9:
# Témakörök: Fájl kezelés
# Írj függvényt, ami soronként beolvassa a files\books.txt fájlt és
# kiírja az aktuális sor tartalmát és az adott sor hosszát
# Például: A programozás alapjai --> A programozás alapjai (Sor hossza: 21)

def task9():
    # Megoldás ide
    pass

# ----------------------------------------------------------------------------------------------------------------------

# Feladat 10:
# Témakörök: Input, Fájl kezelés
# Írj függvényt, ami bekér 3 adatot a felhasználótól (név, életkor, kedvenc étel)
# Majd hozzáfűzi a files\users.txt-hez ezeket az adatokat 1 új sorként. Pl: Anna 12 palacsinta
# Segítség: hozzáfűzés/append --> open(path, 'a', encoding='UTF-8')

def task10():
    # Megoldás ide
    pass
