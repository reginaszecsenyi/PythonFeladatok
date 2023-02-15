print('************ 6. feladat ******************')
'''
Adott egy lista, mely számokat tartalmaz. Jelenítsd meg a listából azokat a számokat a képernyőn, melyek oszthatók öttel. 
Viszont, ha a szám nagyobb mint 100, akkor, azt hagyd figyelmen kívül és lépj a következő számra.
Ha 250-nél is nagyobb a szám, fejezd be a kiíratást.
A számok: 8, 10, 75, 149, 64, 89, 225, 5, 145, 260, 1, 50
'''
# print("***Megoldás***")
# szamok = [8, 10, 75, 149, 64, 89, 225, 5, 145, 260, 1, 50]
#
# for sz in szamok:
#     if sz > 250:
#         break
#     if sz > 100 and sz <= 250:
#         continue
#     if sz % 5 == 0:
#         print(sz)
#

print('************ 7. feladat ******************')
'''
Adott egy szám. (Te választhatod ki.) Számold meg, hogy hány számjegyből áll!
Próbáld meg while ciklus segítségével is megoldani a feladatot!
'''
print("***Megoldás***")
# print('\n----A verzió----')
# nr = 8965
# print(len(str(nr)))

# print('\n----B verzió----')
# nr = 8965
# szamlalo = 0
# while nr != 0:
#     szamlalo += 1
#     nr = nr // 10
# print(szamlalo)



print('************ 8. feladat ******************')
'''
Írj egy szkriptet, ami bekér a felhasználótól egy egész számot, majd írasd ki ennek a számnak az egész osztóit!
'''
# print("***Megoldás***")
# user_szama = int(input('Írj egy egész számot : '))
# osztok = []
# for i in range(user_szama):
#     if user_szama % (i + 1) == 0:
#         osztok.append(i + 1)
# print(f'{user_szama} egész osztói:\n{osztok}')



print('************ 9. feladat ******************')
'''
Készíts egy szkriptet, ami kiírja a képrenyőre, hogy a felhasználótól bekért szám páros vagy páratlan?
'''
# print("***Megoldás***")
# print('\n----A verzió----')
# nr = input("Adj meg egy számot: ")
#
# if int(nr) % 2 == 0:
#     print(nr + ' -> páros szám')
# elif int(nr) % 2 == 1:
#     print(nr + " -> páratlan szám")
#
# print('\n----B verzió----')
# num = int(input("Adj meg egy számot: "))
# mod = num % 2
# if mod > 0:
#     print(f'A(z) {num} páratlan szám.')
# else:
#     print(f"A(z) {num} páros szám.")


print('************ 10. feladat ******************')
'''
Adott egy lista számokkal: 15, 56, 1, 89, 2, 78, 9, 40, 10, 32.
I. Írasd ki egyesével a képernyőre, egymás alá a 10-nél kisebb számokat!
II. Gyűjtsd egy listába a 20-nál nagyobb számokat! Jelenítsd meg a listaelemeket és hogy hány elemű ez a lista!
III. Növekvő sorrendben írasd ki a számokat egyesével, egy sorba!
'''
print("***Megoldás***")

sz_lista = [15, 56, 1, 89, 2, 78, 9, 40, 10, 32]

print('\n----I.----')
hatarszam = 10
print(f'A {hatarszam} alatti számok:')
for sz in sz_lista:
    if sz < hatarszam:
        print(sz)

print('\n----II.----')
hsz = 20
uj_lista = []
for le in sz_lista:
    if le > hsz:
        uj_lista.append(le)
print(uj_lista)
print(f'A fenti lista a {hsz} feletti számokat tartalmazza, összesen {len(uj_lista)} darab számot.')


print('\n----III.----')
sz_lista.sort()
print(sz_lista)

for e in sz_lista:
    print(e, end=" ")
print()