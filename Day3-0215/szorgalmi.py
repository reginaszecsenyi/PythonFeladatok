print('************ 11. feladat ******************')
'''
I. Készíts egy szkriptet, ami kijelzi, hogy a felhasználótól bekért szó palindróma-e?
II. Készíts egy szkriptet, ami kijelzi, hogy a felhasználótól bekért mondat palindróma-e?
Palindróma az, ami visszafele olvasva is ugyanazt adja, mint az eredeti. Pl. szó esetén: kék, mondat esetén: Indul a görög aludni.
'''
# word = input('Adj meg egy szót:')
# if word.lower() == word.lower()[::-1]:
#     print(f'A(z) {word} szó palindróma.')
# else:
#     print(f'A(z) {word} szó nem palindróma.')
# print(word.lower(), word.lower()[::-1])
#
#
# sentence = input('Adj meg egy mondatot: ')
# sentence_1 = sentence.replace(' ','')
#
# # print(sentence_1[0:-1].lower())
#
# if sentence_1[0:-1].lower() == sentence_1[0:-1].lower()[::-1]:
#     print(f'A(z) {sentence} mondat palindróma.')
# else:
#     print(f'A(z) {sentence} mondat nem palindróma.')
#
# print('************ 12. feladat ******************')
'''
A szkripted számolja és írja ki, hogy hány év múlva lesz egy apa kétszer olyan idős, mint a fia.
Az adatokat a felhasználótól kérd be!
A szkripted kezelje azt is, ha ez a duplázódás a múltban volt.
'''


print('************ 13. feladat ******************')
'''
Írj egy kő - papír - olló játékot!
Két játékos egymás után választhat, a szokásos szabályok mentén.
Írd ki, hogy melyik játékos nyert, illetve, hogy szeretnék-e tovább folytatni a játékot?
'''
# k = 'kő'
# p = 'papír'
# o = 'olló'
#
# while True:
#     player1 = input('Első játékos, válassz: kő, papír, olló? ')
#     player2 = input('Második játékos, válassz: kő, papír, olló? ')
#     if player1 == player2:
#         print('Döntetlen')
#     elif (player1 == k and player2 == o) or (player1 == p and player2 == k) or (player1 == o and player2 == p):
#         print('Első játékos nyert.')
#     elif (player2 == k and player1 == o) or (player2 == p and player1 == k) or (player2 == o and player1 == p):
#         print('Második játékos nyert.')
#
#     another = input('Akartok-e még játszani? Y/N ')
#     if another.lower() == 'y':
#         continue
#     else:
#         print('Köszi a játékot.')
#         break

print('************ 14. feladat ******************')
'''
Írd ki a Fibonacci sor első tíz elemét!
A sor kezdődjön 0-val és 1-gyel.
(Fibonacci sor: két egymást követő elem összege egyenlő a követő elemmel. 0,1,1,2,3,5,8,13,21,34
'''
#nemjó
# f0 = 0
# f1 = 1
# print(f0)
# print(f1)
# sorszam = 1
# while sorszam < 9:
#     print((f1-1) + (f1-2))
#     f1 += 1
#     sorszam += 1
#------------------------------

n1 = 0
n2 = 1

szamlalo = 0

while szamlalo < 9:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth

    szamlalo += 1

#------------------------------
fibonacci = [0,1]
for x in range(10):
    if x == 0:
    continue

fibonacci.append(fibonacci[x-1] + fibonacci[x])

print('************ 15. feladat ******************')
'''
Rajzold ki az alábbi ábrát egy szkript segítségével!
+
++
+++
++++
+++++
'''

