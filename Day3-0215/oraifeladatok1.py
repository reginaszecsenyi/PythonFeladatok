print('************ 1. feladat ******************')
'''
Adottak a következő szavak: két, macska, van.
Jelenítsd meg őket egy mondatban! (Két macska van.)
Jelenítsd meg őket egy mondatban, de számot használj! (2 monitor van.)
'''


print('************ 2. feladat ******************')
'''
Kérj be a felhasználótól három számot!
Add meg a három szám összegét, kivéve ha a három szám azonos, akkor a szorzatukat add meg!
'''
a = int(input('Adj meg egy számot: '))
b = int(input('Adj meg még egy számot:'))
c = int(input('Adj meg egy harmadik számot: '))

if a == b == c:
    print(a * b * c)
else:
    print(a + b + c)

print('************ 3. feladat ******************')
'''
Add meg egy felhasználótól bekért szó páratlan helyen lévő betűjeit és írasd őket ki! (pl. alma esetén a megoldás a,m)
'''
szo = input('Adj meg egy szót: ')
print(szo[0::2])


print('************ 4. feladat ******************')
'''
Készíts egy öt elemű felhasználótól bekért törtszám listát! Jelenítsd meg a képernyőn a listát!
'''
tortszamok = []
darab = 0
while darab < 5:
    szam = float(input('Adj meg egy törtszámot: '))
    tortszamok.append(szam)
    darab += 1
print(tortszamok)


print('************ 5. feladat ******************')
'''
Ellenőrizd, hogy megegyezik-e egy lista első és utolsó eleme! Írasd ki a megfelelő boolean értéket a képernyőre!
A listát Te határozhatod meg.
'''
gyumolcs = ['alma', 'barack', 'körte', 'banán']
if gyumolcs[0] == gyumolcs[-1]:
    print(True)
else:
    print(False)

