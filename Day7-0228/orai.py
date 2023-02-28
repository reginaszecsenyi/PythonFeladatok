# Állatok dictionary felépítése fájlból + új csoport hozzáadása
# animals[FAJ] = [ állat1, állat2, stb. ]

ANIMALS = dict()

path = r'files\animals.txt'

with open(path, 'r', encoding='UTF-8') as animals_file:
    for line in animals_file:
        words = line[:-1].split()
        #print(words)
        key = words[0]
        values = words[1:]
        print(f'Key: {key} --> {values}')

        ANIMALS[key] = values
        print(ANIMALS)

print(ANIMALS['Kutya'][2])