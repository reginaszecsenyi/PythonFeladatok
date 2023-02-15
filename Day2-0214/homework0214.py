"""
1. feladat
Kérjünk be a felhasználótól folyamatosan szövegeket, amíg 'exit' utasítást nem ad meg.
- Írassuk ki egy sorban az aktuálisan megkapott szöveget, egy nyilat és a szöveget visszafelé.
  Pl.: toyota --> atoyot
- Az 'exit' parancs érkezhet bármilyen formában. Pl.
  eXit, EXIT, EXiT stb.
  Oldjuk meg ezt a problémát.
- Kilépéskor köszönjön el a program.
"""

#1. feladat megoldása jöhet ide
while True:
    szoveg = input('Adj meg egy szöveget: ')
    if szoveg.lower() != 'exit':
        print(szoveg + ' --> '+ szoveg[::-1])
    else:
        print('Bye')
        break

# exit = False
# while not exit:
#     szoveg = input('Adj meg egy szöveget: ')
#     if szoveg.lower() != 'exit':
#         print(szoveg + ' --> '+ szoveg[::-1])
#     else:
#         exit = True
#         print('Bye')


"""---------------------------------------------------------------------------------------------------------------------
2. feladat
Kérdezzük meg a felhasználót, hogy hány számot szeretne megadni.
For ciklus segítségével kérjünk be annyi db számot, amennyit a felhasználó előzőleg meghatározott
és tároljuk őket egy listában.

Kimenetként
- Írassuk ki a teljes listát
- Írassuk ki a listát úgy, hogy csak minden 2. elemet tartalmazza.
- Rendezzük csökkenő sorrendbe a listát
"""

# 2. feladat megoldása jöhet ide

szam = int(input('Hány számot szeretne megadni? '))
lista = []
for x in range(szam):
    lista.append(x)
print(lista)
print(lista[::2])
lista.sort(reverse=True)
print(lista)

"""---------------------------------------------------------------------------------------------------------------------
3. feladat 
Kérjünk be neveket a felhasználótól és tároljuk őket egy listában.
Minden név felvétel után kérdezzük meg, hogy akar-e még nevet felvenni.
Ha igen --> ismételjük az előzőeket
Ha nem --> kérdezzük meg, hogy csökkenő vagy növekvő sorrendben szeretné-e látni a névsort.
Írassuk ki a névsort a kért módon.
"""

# 3. feladat megoldása jöhet ide
# nev = input('Adjon meg egy nevet: ')
nevlista = []
while True:
    nev = input('Adjon meg egy nevet: ')
    nevlista.append(nev)
    valasztas = input('Akar-e még nevet felvenni? ')
    if valasztas == 'igen':
        continue
    else:
        sorrend = input('Növekvő vagy csökkenő sorrendet szeretne? ')
        if sorrend == 'növekvő':
            nevlista.sort()
            print(nevlista)
        else:
            nevlista.sort(reverse=True)
            print(nevlista)
        break




"""---------------------------------------------------------------------------------------------------------------------
4. feladat
Szimuláljunk le egy kocka dobás játékot.
Minden körben a gép és a játékos is kap egy véletlenszerű értéket 1 és 6 között.
Az nyeri az adott fordulót, aki nagyobbat dobott.
Ha ugyanakkorát dobtunk, akkor újra dobunk.
A játék 5 győzelemig tart. Aki előbb eléri az 5 körgyőzelmet, az lesz a nyertes.
"""

# 4. feladat megoldása jöhet ide

"""---------------------------------------------------------------------------------------------------------------------
SZORGALMI
A megadott stringben keressük meg az összes 'sör' előfordulást és tároljuk el az indexüket egy listában
"""

sentence = 'Egy sör nem sör. 2 sör fél sör. 4 sör 1 sör. 1 sör meg nem sör...'
