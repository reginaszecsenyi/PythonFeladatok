'''
1. feladat: Enumerate
Kösd össze az alábbi két listát úgy, hogy minden állathoz kiírásra kerüljön a természetes ellensége.
(Lehet, hogy eltolást is kell használnod!)

Kimenet -> {állat} természetes ellensége: {ellenség}
'''

print('Természetes ellenségek')

animals = ['béka', 'tyúk', 'macska', 'légy', 'kis hal']
opponents = ['oroszlán', 'elefánt', 'gólya', 'sas', 'kutya', 'pók', 'nagy hal']

# Megoldás helye

for index, animal in enumerate(animals):
    print(f'{animal} természetes ellensége: {opponents[index+2]}')

# -------------------------------------------------------------------------------------------------------

'''
2. feladat: Dictionaries
Az alábbi dict típus None értékei helyett vegyél fel új értékeket, majd
írasd ki a teljes struktúrát a következő módon:

Cím: {irányítószám} {város} - {utca} {házszám} ({ország})

Szorgalmi: vegyél fel egy gyűjtőlistát, ami ilyen cím dictionary-ket tartalmaz,
és írass ki minden címet az előbbi módon.

'''

address = {
    'city': 'Budapest',
    'street': None,
    'number': None,
    'zipcode': 1111,
    'country': None
}

print('Cím kiírás')
# Megoldás helye

new_addresses ={
    'street': 'Kossuth Lajos utca',
    'number': 12,
    'country': 'Magyarország'
}
address.update(new_addresses)
print(address)
print('Cím:', end=' ')
for x in address.values():
    print(x, end= ' ')
print()

# -------------------------------------------------------------------------------------------------------

'''
3. feladat: Set
Egy hotel oldalon a felhasználók lehetnek Tulajdonosok is, illetve Vendégek is.
Add meg az alábbi felhasználó listákra a következő halmaz értékeket:
- Tulajdonos és Vendég szerepkörrel egyaránt rendelkező felhasználók
- Minden olyan felhasználó, aki csak tulajdonos
- Azok a felhasználók, akik csak egyféle szerepkörrel rendelkeznek
'''

guests = {'adam', 'barbie', 'cecil', 'daniel', 'elmo', 'frank', 'hugo', 'ivan', 'jekyll'}
owners = {'nancy', 'zoe', 'adam', 'hugo', 'bobby', 'ivan', 'anastasia', 'harry'}

print('Hotel felhasználók')
# Megoldások helye

print(guests.intersection(owners))
print(owners.difference(guests))
print(guests.symmetric_difference(owners))

intersection = guests & owners
print(f'Tulajdonos és vendég is: {intersection}')
difference = owners - guests
print(f'Csak tulajdonosok: {difference}')
symmetric = guests ^ owners
print(f'Csak egyféle szerepkör: {symmetric}')
# -------------------------------------------------------------------------------------------------------

'''
4. feladat: Tuple
Írjunk függvényt, ami 1-10 között vár számokat.
- A kapott számot megfelelteti olvasható verziójával. Pl.: 1 -> 'egy'
Ezt NE If-Else-el oldjuk meg! Használjunk hozzá Dictionary-t!
- Két értéket ad vissza: az olvasható verziót először, majd a paraméterként kapott számot
- Használjuk fel a kapott értékeket egy kiírásban. 
Pl.: A megadott {n} szám átírása: {atirt_szam}

Szorgalmi: a függvény dobjon ValueErrort, ha nem 1-10 között kap számot, illetve TypeError-t, ha nem integer-t kap
'''

print('Szám megfeleltetés')
# Megoldás helye

