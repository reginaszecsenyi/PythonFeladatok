#4. Feladat: Speciális számok kiválasztása.
# Nevezzük speciálisnak azokat a számokat, amelyek 11 többszörösei (másként fogalmazva oszthatók 11-el) vagy pont 1-el nagyobbak, mint 11 valamelyik többszöröse.
#
# írj egy olyan Python függvényt, ami megkapja a tesztelendő számot paraméterként és visszaadja, hogy a kérdéses szám az speciális-e vagy nem. Ezt igaz/hamis formájában várjuk!
#
# def special_eleven(x):
#     pass # write your code here
#
# special_eleven(22)
# # >>> True
# special_eleven(23)
# # >>> True
# special_eleven(24)
# # >>> False
# Hívd meg a függvényed az alábbi számokra:
#
# 23, 24, 122, 96


# Tanácsok a megoldáshoz:
# Fontos, hogy függvényt használj!
# Fontos, hogy legyen bekérés a felhasználótól a konzolon keresztül.
# Ne gondold túl!
# Nem kell ellenőrizni, hogy a bemenet csak egész szám legyen!
# Bármilyen megoldás ami a fenti tesztadatokra (és hasonló tesztadatokra) a helyes megoldást adja tökéletesen megfelel.
# Nincs pontlevonás ha lehetne ezt egyszerűbben is.
# Nincs plusz pont ha kevesebb sorból oldod meg.


'''
Bekérünk egy számot, a program ellenőrzi, hogy
    ha a bekért számot 11-el osztva a maradék nulla -->speciális szám
    ha a bekért szám 11-el osztva a maradék 1 --> speciális szám
    minden más esetben pedig nem speciális szám.
'''


#number = input('Adj meg egy számot:')
def special_eleven(number):

    if number % 11 == 0:
        print(True)
        # print(f'{number} is a special number.')
    elif number % 11 == 1:
        print(True)
        # print(f'{number} is a special number.')
    else:
        print(False)
        # print(f'{number} is not a special number.')


special_eleven(22)

special_eleven(23)

special_eleven(24)

special_eleven(122)

special_eleven(96)