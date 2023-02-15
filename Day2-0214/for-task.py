# SZÁMOK ÖSSZEGZÉSE
# Csak a páros számokat adjuk össze

numbers = [2, 43, 54, 65, 22, 86, 91, 2, 1, 1213, 13, 74]

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number
print(total)

'''Solution
numbers = [2, 43, 54, 65, 22, 86, 91, 2, 1, 1213, 13, 74]

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number
        print(f'{number}-t hozzáadtam.')

print(f'Kapott összeg: {total}')
'''