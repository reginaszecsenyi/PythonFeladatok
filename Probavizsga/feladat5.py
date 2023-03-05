# 5. Feladat: Python függvény, ami számokat fodít egy listában.
# Készíts egy python függvényt (egy darab python file) ami bekér két egész számot és elkészít egy listát a két szám közötti egész számokból.
#
# def between(a, b):
#     pass # write your code here
#
# print(between(5, 10))
# # >>> [5,6,7,8,9,10]
#
# print(between(1,2))
# # >>> [1,2]


# Tanácsok a megoldáshoz:
# Fontos, hogy függvényt használj!
# Fontos, hogy legyen bekérés a felhasználótól a konzolon keresztül.
# Ne gondold túl!
# Bármilyen megoldás ami a fenti tesztadatokra (és hasonló tesztadatokra) a helyes megoldást adja tökéletesen megfelel.
# Nincs pontlevonás ha lehetne ezt egyszerűbben is.
# Nincs plusz pont ha kevesebb sorból oldod meg.




numberlist = []

def task4(a, b):

    for n in range(a, b + 1):
        numberlist.append(n)
    return numberlist


print('Adj meg két számot, egy számlista első és utolsó értékét!')
a = int(input('Az első szám: '))
b = int(input('A második szám: '))


print(task4(a, b))