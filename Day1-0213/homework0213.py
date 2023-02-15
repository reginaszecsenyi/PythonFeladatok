"""
1. Feladat
Kérj be a felhasználótól 2 db számot és írasd ki a következő képletek eredményét
-  (a + b) * (a - b)
-  (a hatvány b) - (a és b szorzata)
-  a / b maradéka és egész értéke
"""

# 1. feladat megoldása ide jöhet

a = int(input('Add meg a értékét:'))
b = int(input('Add meg b értékét:'))
print((a + b) * (a - b))
print((a**b) - (a * b))
print(a % b)
print(a // b)


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

alma = (fruits[0:5])
narancs = (fruits[6:12])
banán = (fruits[13:])

print((alma.upper()), 'hossz: ', len(alma))
print((narancs.lower()), 'hossz: ', len(narancs))
print((banán[::-1]), 'hossz: ', len(banán))

"""---------------------------------------------------------------------------------------------------------------------
3. feladat
Az alábbi változó tartalmaz egy rejtjelezett szöveget.
Ha csak minden 3. karaktert olvasol össze, akkor kapod meg az eredeti, értelmes üzenetet.
Írasd ki a képernyőre a megfejtést!
"""

secret_message = 'QmRgFeusjbetUlőGKzkCkSYöxKdMXőuK GsPYiywTtBehewoNIn'
# 3. feladat megoldása jöhet ide

print(secret_message[2::3])


"""---------------------------------------------------------------------------------------------------------------------
4. feladat
Menüpont választás. Írasd ki a képernyőre az alábbi szöveget:

Üdvözöllek!
1. Kirándulás
2. TV nézés
3. Tanulás

Kérj be a felhasználótól egy menüpontot (1-3) 
és a választásnak megfelelően írj ki egy szöveget a képernyőre.
"""

print('''Üdvözöllek!
1. Kirándulás
2. Tv nézés
3. Tanulás''')

choice = int(input('Válassz egy menüpontot (1-3): '))

if choice == 1:
    print('A választott menüpont: Kirándulás')
elif choice == 2:
    print('A választott menüpont: Tv nézés')
elif choice == 3:
    print('A választott menüpont: Tanulás')
else:
    print('Ilyen menüpont nem létezik.')
