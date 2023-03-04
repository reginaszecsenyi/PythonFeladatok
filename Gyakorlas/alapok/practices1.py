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
# 1. A paraméterben kapott szövegből írassuk ki az összes n-ik karaktert. (szintén paraméter)

def task1(szoveg, n):
    print(szoveg[n-1::n])

# ----------------------------------------------------------------------------------------------------------------------
# 2. A paraméterben található szövegben mi található az első 8, illetve az utolsó 3 helyen úgy, hogy nem vesszük
# figyelembe a space karaktereket?

def task2(szoveg: str):
    replaced_szoveg = szoveg.replace(' ', '')
    print(replaced_szoveg[0:8])
    print(replaced_szoveg[-3:])

# ----------------------------------------------------------------------------------------------------------------------
# 3. A paraméterben kapott órák számát váltsuk át x nap y óra formátumba. Pl. 49 -> 2 nap 1 óra

def task3(h):
    print(f'{h} óra egyenlő {h // 24} nappal és {h % 24} órával.')

# ----------------------------------------------------------------------------------------------------------------------
# 4. Az alább megadott listában mely szavak lesznek JÓ szavak, ha a JÓ szavakról tudjuk, hogy 4 karakterből állnak?
# str_list = ['cherry', 'phone', 'more', 'agree', 'baby', 'daddy']

def task4():
    str_list = ['cherry', 'phone', 'more', 'agree', 'baby', 'daddy']

    for word in str_list:
        if len(word) == 4:
            print(f'{word}: ez egy jó szó')
        else:
            print(f'{word}: ez egy rossz jó')

# ----------------------------------------------------------------------------------------------------------------------
# 5. Valósítsunk meg egy funkciót, ami egy növény magasságát várja (10 - 150 cm) és a különböző mérettartományok alapján
# különböző árakat mutat a felhasználónak

def task5(height):
    if height < 50:
        print('A növény ára: 500 ft.')
    elif 50 <= height < 100:
        print('A növény ára: 1000 Ft')
    else:
        print('A növény ára: 1500 Ft')

# ----------------------------------------------------------------------------------------------------------------------
# 6. Kapott számlista: pozitív/negatív-ok külön listákba. Legkisebb, legnagyobb, összeg mindkettőre
# [12, 322, -75, 23, -3, 11, 6, 8, -3, -100]

nr_list =[12, 322, -75, 23, -3, 11, 6, 8, -3, -100]
pos_list = []
neg_list = []

def task6():
    for n in nr_list:
        if n > 0:
            pos_list.append(n)
        else:
            neg_list.append(n)

    print(f'A pozitív számok listája: {pos_list}, Min:{min(pos_list)}, Max:{max(pos_list)}, Átlag:{sum(pos_list)}')
    print(f'A negítv számok listája: {neg_list}, Min:{min(neg_list)}, Max:{max(neg_list)}, Átlag:{sum(neg_list)}')



# ----------------------------------------------------------------------------------------------------------------------
# 7. Paraméterben kapott két szám közötti páratlan számokat gyűjtsük ki és rendezzük csökkenő sorrendbe őket

odd_numbers = []

def task7(a, b):
    for n in range(a, b):
        if n % 2 != 0:
            odd_numbers.append(n)

    odd_numbers.sort(reverse=True)
    print(odd_numbers)


# ----------------------------------------------------------------------------------------------------------------------
# 8. Tippelős program - Szabadság szobor hány méter magas? (93)
# simán, majd átalakítás while formába.

def task8():
    quit = False

    while not quit:

        guess = int(input('Tippelj, hány méter magas a szabadság szobor?'))
        if guess > 93:
            print('Nem, ennél kisebb')
        elif guess < 93:
            print('Nem, ennél nagyobb')
        else:
            print('Eltaláltad!')
            quit = True
# ----------------------------------------------------------------------------------------------------------------------
# 9.  Kedvenc filmek bekérése (5). Rendezzük ABC sorrendbe őket. Adjuk meg az első 3-at, illetve az utolsó 3-at.

films = []

def task9():
    for f in range(5):
        film = input('Add meg a kedvenc filmed:')
        films.append(film)

    films.sort()
    print(films)
    print(films[:3])
    print(films[-3:])

# ----------------------------------------------------------------------------------------------------------------------
