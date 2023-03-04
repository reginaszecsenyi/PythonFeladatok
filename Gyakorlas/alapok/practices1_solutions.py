"""
Ebben a fájlban találjátok a feladatok lehetséges megoldásait.
"""
# Feladat 0:
# Témakörök: írás kimenetre
# Írj egy függvényt, ami kiírja a kimenetre a következő szöveget: 'Csak minta szerepem van. :)'
def example_function():
    print('Csak minta szerepem van. :)')


# ----------------------------------------------------------------------------------------------------------------------
# A paraméterben kapott szövegből írassuk ki az összes n-ik karaktert. (szintén paraméter)
def task1(text: str, n: int):
    #[start, end, step]
    print(text[n-1::n])

# ----------------------------------------------------------------------------------------------------------------------
# A paraméterben található szövegben mi található az első 8, illetve az utolsó 3 helyen úgy, hogy nem vesszük
# figyelembe a space karaktereket?
def task2(text: str):
    new_text = text.replace(' ', '') # space karakterek helyettesítése üres string-el
    print(f'Eredeti szöveg: {text}')
    print(f'Space nélkül: {new_text}')
    print(f'Első 8 karakter: {new_text[:8]}') # 0 1 2 3 4 5 6 7
    print(f'Utolsó 3 karakter: {new_text[-3:]}') # start: hátulról a harmadik, end: végéig

    # Ez nem volt a feladat része, csak hallgatói kérdés miatt tettük bele:
    print(f'Utolsó 3 karakter nélkül: {new_text[:-3]}') # utolsó 3 karakter nélkül


# ----------------------------------------------------------------------------------------------------------------------
# A paraméterben kapott órák számát váltsuk át x nap y óra formátumba. Pl. 49 -> 2 nap 1 óra
def task3(hours: int):
    maradek = hours % 24 # fennmaradó órák száma. Pl: 26 % 24 -> 2
    egesz = hours // 24 # napok száma. Pl: 26 // 24 -> 1
    print(f'A {hours} óra megegyezik: {egesz} nap {maradek} óra')

# ----------------------------------------------------------------------------------------------------------------------
# Az alább megadott listában mely szavak lesznek JÓ szavak, ha a JÓ szavakról tudjuk, hogy 4 karakterből állnak?
# str_list = ['cherry', 'phone', 'more', 'agree', 'baby', 'daddy']
def task4():
    str_list = ['cherry', 'phone', 'more', 'agree', 'baby', 'daddy', 'pelda']

    # A lista elemeit számoltuk meg - nem része a feladatnak - hallgatói kérdés volt.
    # print(str_list)
    # print(f'A lista hossza: {len(str_list)}')

    for word in str_list:
        # Mi történik a háttérben:
        # 1. kör: word = 'cherry'
        # 2. kör: word = 'phone'
        # ...
        # n. kör: word = lista utolsó eleme
        print(f'{word} hossza: {len(word)}')
        if len(word) == 4:
            print('Ez egy JÓ szó')
        else:
            print('Ez egy ROSSZ szó')

# ----------------------------------------------------------------------------------------------------------------------
# Valósítsunk meg egy funkciót, ami egy növény magasságát várja (10 - 150 cm) és a különböző mérettartományok alapján
# különböző árakat mutat a felhasználónak
def task5(height: int):

    if 10 <= height <= 150:

        if height < 50:
            print(f'A {height} cm-es növény ára: 500 Ft')
        elif 50 <= height < 100:
            print(f'A {height} cm-es növény ára: 1000 Ft')
        elif 100 <= height < 120:
            print(f'A {height} cm-es növény ára: 2000 Ft')
        else:
            print(f'A {height} cm-es növény ára: 5000 Ft')

    else:
        print('Jelenleg nincs ilyen növényünk raktáron.')


# ----------------------------------------------------------------------------------------------------------------------
# Kapott számlista: pozitív/negatív-ok külön listákba. Legkisebb, legnagyobb, összeg mindkettőre
# [12, 322, -75, 23, -3, 11, 6, 8, -3, -100]
def task6():
    numbers = [12, 322, -75, 23, -3, 11, 6, 8, -3, -100]
    negative_numbers = []
    positive_numbers = []

    # A válogatás folyamatát ciklus és feltételek segítségével végezzük el.
    for number in numbers:
        if number < 0:
            negative_numbers.append(number)
        else:
            positive_numbers.append(number)

    # Így is lehet, de a beépített függvények miatt felesleges:
    # positive_numbers.sort() # alapértelmezetten legkisebbtől a legnagyobbig rendez
    # minimum = positive_numbers[0] # rendezett lista első eleme
    # maximum = positive_numbers[-1] # rendezett lista utolsó eleme

    print(f'Negatív számok minimuma: {min(negative_numbers)} maximuma: {max(negative_numbers)} összege: {sum(negative_numbers)}')
    print(f'Pozitív számok minimuma: {min(positive_numbers)} maximuma: {max(positive_numbers)} összege: {sum(positive_numbers)}')

# ----------------------------------------------------------------------------------------------------------------------
# Paraméterben kapott két szám közötti páratlan számokat gyűjtsük ki és rendezzük csökkenő sorrendbe őket
def task7(a, b):
    # range függvény segít abban, hogy könnyen létre tudjunk hozni szám intervallumokat!
    # szintén a [start, end, step] modellt használja
    # range(8) # 0,1,2,3,4,5,6,7
    # range(1,6) # 1,2,3,4,5
    # range(0,10,2) # 0,2,4,6,8

    odd_numbers_in_range = []

    for number in range(a, b):
        if number % 2 != 0:
            odd_numbers_in_range.append(number)

    print(odd_numbers_in_range)
    # odd_numbers_in_range.sort() # alapértelmezett működés: növekvő sorrend
    odd_numbers_in_range.sort(reverse=True) # csökkenő sorrend
    print(odd_numbers_in_range)


# ----------------------------------------------------------------------------------------------------------------------
# Tippelős program - Szabadság szobor hány méter magas? (93)
# simán, majd átalakítás while formába.
def task8_simple():
    print('Üdv! Ki tudod találni, hogy hány méter magas a New York-i Szabadság szobor?')
    guess = int(input('A tipped (m): '))

    if guess == 93:
        print('Gratulálok, eltaláltad!')
    elif guess > 93:
        print('Nem, ennél azért kisebb.')
    else:
        print('Ugyan, ennél nagyobb.')


def task8_while():
    print('Üdv! Ki tudod találni, hogy hány méter magas a New York-i Szabadság szobor?')

    while True:
        guess = int(input('A tipped (m): '))

        if guess == 93:
            print('Gratulálok, eltaláltad!')
            break # Hogy kilépjünk a - jelenleg - végtelen ciklusból
        elif guess > 93:
            print('Nem, ennél kisebb. Próbáld újra!')
        else:
            print('Ennél nagyobb. Próbáld újra!')

    print('Vége a játéknak. Viszlát!')

# ----------------------------------------------------------------------------------------------------------------------
# Kedvenc filmek bekérése (5). Rendezzük ABC sorrendbe őket. Adjuk meg az első 3-at, illetve az utolsó 3-at.
def task9():
    favorite_films = []
    print('Üdv! Add meg az 5 kedvenc filmed címét:')

    for count in range(5):
        actual_film_title = input(f'{count+1}. film címe: ')
        favorite_films.append(actual_film_title)

    # Bekérés után ABC sorrendbe rendezzük a film címeket:
    favorite_films.sort() # alapértelmezetten növekvő a sorrend. Stringek esetén ez a->z -t fog jelenteni
    print(f'A rendezett film lista: {favorite_films}')
    print(f'Első három film a rendezett listában: {favorite_films[:3]}')
    print(f'Utolsó három film a rendezett listában: {favorite_films[-3:]}')

# ----------------------------------------------------------------------------------------------------------------------
