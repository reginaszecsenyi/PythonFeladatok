import random
# https://docs.python.org/3/library/random.html

print('''Üdvözöllek!
Gondoltam egy számot 1 és 100 között.
Mit tippelsz, melyik az?''')

number = random.randint(1, 100)
win = False
tries = 0

while not win:
    guess = int(input('Tipp: '))
    tries += 1

    if guess > number:
        print('Nem, én kisebb számra gondoltam.')
    elif guess < number:
        print('Nem, én nagyobb számra gondoltam.')
    else:
        print(f'Gratulálok, {tries} próbálkozásból találtad el.')
        win = True

print('Viszlát!')