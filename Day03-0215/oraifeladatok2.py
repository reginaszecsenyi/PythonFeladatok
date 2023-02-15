print('************ 6. feladat ******************')
'''
Adott egy lista, mely számokat tartalmaz. Jelenítsd meg a listából azokat a számokat a képernyőn, melyek oszthatók öttel. 
Viszont, ha a szám nagyobb mint 100, akkor, azt hagyd figyelmen kívül és lépj a következő számra.
Ha 250-nél is nagyobb a szám, fejezd be a kiíratást.
A számok: 8, 10, 75, 149, 64, 89, 225, 5, 145, 260, 1, 50
'''
szamlista = [8, 10, 75, 149, 64, 89, 225, 5, 145, 260, 1, 50]

for szam in szamlista:
    if szam > 250:
        break
    elif szam > 100:
        continue
    elif szam % 5 == 0:
        print(szam)

print('************ 7. feladat ******************')
'''
Adott egy szám. (Te választhatod ki.) Számold meg, hogy hány számjegyből áll!
Próbáld meg while ciklus segítségével is megoldani a feladatot!
'''
number = 10254
print(len(str(number)))


print('************ 8. feladat ******************')
'''
Írj egy szkriptet, ami bekér a felhasználótól egy számot, majd írasd ki ennek a számnak az egész osztóit!
'''
num = int(input('Adj meg egy számot: '))
for x in range(1, num+1):
    if num % x == 0:
        print(x)



print('************ 9. feladat ******************')
'''
Készíts egy szkriptet, ami kiírja a képrenyőre, hogy a felhasználótól bekért szám páros vagy páratlan?
'''

number1 = int(input('Adj meg egy számot: '))
if number1 % 2 == 0:
    print('A szám páros')
else:
    print('A szám páratlan')


print('************ 10. feladat ******************')
'''
Adott egy lista számokkal: 15, 56, 1, 89, 2, 78, 9, 40, 10, 32.
I. Írasd ki egyesével a képernyőre, egymás alá a 10-nél kisebb számokat!
II. Gyűjtsd egy listába a 20-nál nagyobb számokat! Jelenítsd meg a listaelemeket és hogy hány elemű ez a lista!
III. Növekvő sorrendben írasd ki a számokat egyesével, egy sorba!
'''
