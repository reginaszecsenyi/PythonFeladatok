# PYTHON DAY2 HOMEWORK SOLUTIONS
import random

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

# print('1. feladat megoldása')
# while True:
#     user_input = input('Bevitel (szöveg/exit): ')
#     if user_input.lower() == 'exit':
#         break
#     print(f'{user_input} ---> {user_input[::-1]}')
# print('Viszlát!')

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

# print('2. feladat megoldása:')
#
# number = int(input('Add meg, hogy hány számot szeretnél felvenni a listába: '))
# numbers = []
# for x in range(number):
#     actual_number = int(input(f'Add meg a(z) {x + 1}. számot: '))
#     numbers.append(actual_number)
#
# print(f'A kapott lista: {numbers}')
# print(f'Minden második elem: {numbers[::2]}')
# numbers.sort(reverse=True)
# print(f'Csökkenő sorrend: {numbers}')

"""---------------------------------------------------------------------------------------------------------------------
3. feladat 
Kérjünk be neveket a felhasználótól és tároljuk őket egy listában.
Minden név felvétel után kérdezzük meg, hogy akar-e még nevet felvenni.
Ha igen --> ismételjük az előzőeket
Ha nem --> kérdezzük meg, hogy csökkenő vagy növekvő sorrendben szeretné-e látni a névsort.
Írassuk ki a névsort a kért módon.
"""

# print('3. feladat megoldása')
#
# names = []
# while True:
#     print(f'Jelenleg {len(names)} név van a listában.')
#     actual_name = input('Adj meg egy nevet: ')
#     names.append(actual_name)
#
#     users_choice = input('Szeretnél még egy nevet hozzáadni? (yes/no) ')
#     if users_choice.lower() != 'yes':
#         break
#
# users_choice = input('Csökkenő vagy növekvő sorrendben jelenítsem meg az adatokat? (cs/n)')
#
# #
# if users_choice.lower() == 'cs':
#     names.sort(reverse=True)
# else:
#     if users_choice != 'n':
#         print('Ez nem volt valid opció. Növekvőben fogod kapni az eredményt.')
#     names.sort()
#
# print(names)


"""---------------------------------------------------------------------------------------------------------------------
4. feladat
Szimuláljunk le egy kocka dobás játékot.
Minden körben a gép és a játékos is kap egy véletlenszerű értéket 1 és 6 között.
Az nyeri az adott fordulót, aki nagyobbat dobott.
Ha ugyanakkorát dobtunk, akkor újra dobunk.
A játék 5 győzelemig tart. Aki előbb eléri az 5 körgyőzelmet, az lesz a nyertes.
"""

# points_to_win = 5
# points_of_player = 0
# points_of_computer = 0
#
# round = 0
#
# while points_of_computer != points_to_win and points_of_player != points_to_win:
#     round += 1
#     computer_roll = random.randint(1, 6)
#     player_roll = random.randint(1, 6)
#     print(f'{round}. forduló!')
#     print(f'Aktuális állás: C = {points_of_computer}, P = {points_of_player}')
#     print()
#     print(f'Computer --> {computer_roll} Player --> {player_roll}')
#
#     if player_roll == computer_roll:
#         print('Döntetlen! Új dobás!')
#     elif player_roll > computer_roll:
#         print('Ezt a fordulót a JÁTÉKOS nyerte.')
#         points_of_player += 1
#     else:
#         print('Ezt a fordulót a COMPUTER nyerte.')
#         points_of_computer += 1
#
#     print('-' * 50) # Csak hogy átláthatóbb legyen a kiíratás majd
#
# if points_of_player > points_of_computer:
#     print('Éljen, a JÁTÉKOS nyert!')
# else:
#     print('Hát most a COMPUTER nyert.')



"""---------------------------------------------------------------------------------------------------------------------
SZORGALMI
A megadott stringben keressük meg az összes 'sör' előfordulást és tároljuk el az indexüket egy listában
"""

sentence = 'Egy sör nem sör. 2 sör fél sör. 4 sör 1 sör. 1 sör meg nem sör...'
substring = 'sör'   # Meg lehet próbálni más értékkel is: '1', 'nem', 'nem sör'
length = len(substring)
indeces = []

# Megoldási ötlet: karakterenként végigmegyek a stringen
# és a keresett szövegrészt próbálom illeszteni.
# Ha találok illeszkedést, akkor felveszem a listába az aktuális indexet.
# Ha nem, akkor megyek eggyel tovább.

for index in range(len(sentence) - length):
    # range: a teljes szöveg hosszából kivonom a keresett szöveg hosszát,
    # hogy ne fussak túl a végén.
    if sentence[index:index+length] == substring:
        # az adott indexről indulva megnézem, hogy a következő karaktersorozat megegyezik-e a keresett értékkel
        # ha igen, akkor felveszem az indexet a listámba.
        indeces.append(index)

print(indeces)

# Csak ellenőrzés: valóban a megfelelő szövegeket találtam meg?
for i in indeces:
    print(sentence[i:i+length])