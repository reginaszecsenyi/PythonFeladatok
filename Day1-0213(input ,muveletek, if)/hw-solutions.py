"""
1. Feladat
Kérj be a felhasználótól 2 db számot és írasd ki a következő képletek eredményét
-  (a + b) * (a - b)
-  (a hatvány b) - (a és b szorzata)
-  a / b maradéka és egész értéke
"""

# 1. feladat megoldása ide jöhet
a = int(input('Add meg az "a" számot: '))
b = int(input('Add meg a "b" számot: '))

print(f'({a} + {b}) * ({a} - {b}) = { (a + b) * (a - b)}')
print(f'({a}^{b}) - ({a} * {b}) = { a**b - a*b }')
print(f'{a}/{b} = { a/b }. Egész érték: {a//b}, maradék: {a%b}')


"""---------------------------------------------------------------------------------------------------------------------
2. feladat
Az alábbi változó tartalmaz 3 gyümölcsöt.
Slice-olással mentsd ki a gyümölcsöket külön változókba,
majd végezz el rajtuk műveleteket úgy, hogy a következő kimenetet kapd:

OUTPUT:
APPLE (hossz: 5)
orange (hossz: 6)
ananab (hossz: 6)

"""

fruits = 'apple OrAnGe banana'
# 2. feladat megoldása ide jöhet
# apple = fruits[0:6]
# orange = fruits[6:12]
# banana = fruits[13:]
# print(f'{apple.upper()}, (hossz: {len(apple)})')
# print(f'{orange.lower()}, (hossz: {len(orange)})')
# print(f'{banana[::-1]}, (hossz: {len(banana)})')


"""---------------------------------------------------------------------------------------------------------------------
3. feladat
Az alábbi változó tartalmaz egy rejtjelezett szöveget.
Ha csak minden 3. karaktert olvasol össze, akkor kapod meg az eredeti, értelmes üzenetet.
Írasd ki a képernyőre a megfejtést!
"""

secret_message = 'QmRgFeusjbetUlőGKzkCkSYöxKdMXőuK GsPYiywTtBehewoNIn'
# 3. feladat megoldása jöhet ide
# print(secret_message[2::3]) # a 2. indexen található az első értelmes szöveghez tartozó karakter


"""---------------------------------------------------------------------------------------------------------------------
4. feladat
Menüpont választás. Írasd ki a képernyőre az alábbi szöveget:

Üdvözöllek!
1. Kirándulás
2. TV nézés
3. Tanulás

Kérj be a felhasználótól egy menüpontot (1-3) és a választásnak megfelelően írj ki egy szöveget a képernyőre.
"""

# print('''Üdvözöllek!
#
# 1. Kirándulás
# 2. TV nézés
# 3. Tanulás
# ''')
#
# selected_menu = int(input('Kérlek, válassz egy menüpontot (1-3): '))
#
# if selected_menu == 1:
#     print('Kirándulni megyünk!')
# elif selected_menu == 2:
#     print('Jöhet egy jó kis film!')
# elif selected_menu == 3:
#     print('Hajrá-hajrá :)')
# else:
#     print('Ilyen menüpont nincsen is.')