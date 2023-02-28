
#Általános felépítés
# def fuggveny_neve(nev, nev2):
#     print()
#     #utasítás
#     while True:
#         pass
#     #....
#
#     return

'''-------------------------1. példa: átlag --------------------------'''
numbers = [12, 52, 23, 555, 232, 87, 23, 42, 15]
def atlag(lista):
    hossz = len(lista)
    osszeg = sum(lista)

    return osszeg/hossz

print(f'A számok lista átlaga: { atlag(numbers) }')


'''-------------------------2. példa: sorrend --------------------------'''
#sorrend fontossága
def add_dog(name, age, breed=None):
    print(f'Név: {name} ({age}).', end=' ')
    if breed == None:
        print('Fajta: ismeretlen')
    else:
        print(f'Fajta: {breed}')

add_dog('Bodri', 2)
add_dog('Foxi', 3, breed='Németjuhász')
add_dog('Józsi', 3, 'Bulldog')
add_dog(breed='Bulldog', age=3, name='Józsi')


'''-------------------------3. példa --------------------------'''

def banner(message, border_char='-'):
    print(border_char * (len(message)+4))
    print(f'| {message} |')
    print(border_char * (len(message)+4))

print()
banner('Üdvözöllek a rendszerben!')
banner('Ez egy hibás bevitel!', border_char='*')

'''-------------------------4. példa: páros/páratlan --------------------------'''
#páros vagy páratlan

def even_or_odd(number):
    if type(number) == int:
        if number % 2 == 0:
            return 'even'
        else:
            return 'odd'
    else:
        print('Int-et kell megadni')

print('Páros vagy páratlan')
print(even_or_odd(7))

'''-------------------------5. példa: n-ik gyök --------------------------'''
#N-ik gyök

def nth_root(number, n=2):
    # 9**(1/2) --> 9 gyöke
    return number**(1/n)

print(f'9 gyöke: {nth_root(9)}')
print(f'81 negyedik gyöke: {nth_root(81, n=4)}')

'''-------------------------6. példa: átlag szélsőérték nélkül--------------------------'''
#átlag

def average(numbers, cut=False):
    if cut:
        # Szélsőértékek nélkül
        numbers.sort()
        # print(numbers)
        temp = numbers[1:-1]
        # print(temp)
        return sum(temp) / len(temp)
    else:
        # Normál átlagot fogunk visszadni
        return sum(numbers) / len(numbers)

my_list = [10, 23, 232, 2, 7]
print(f'Sima átlag: {average(my_list)}')
print(f'Módosított átlag: {average(my_list, cut=True)}')

'''-------------------------7. példa: összeadás--------------------------'''

def add(*args):
    # https://realpython.com/python-kwargs-and-args/
    result = 0
    for number in args:
        result += number

    return result

print(f'Összeadás: { add(10, 15) }')
print(f'Összeadás: { add(10, 15, 1, 2, 3) }')