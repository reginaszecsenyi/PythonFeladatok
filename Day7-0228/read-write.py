# Szöveges fájlok megnyitása - régi megoldás (még gyakran látni)

my_tasks_file = open(r'files\tasks.txt', 'r', encoding='UTF-8')
content = my_tasks_file.read()
print(content)
print(type(content))
my_tasks_file.close()

file_path = r'files\task.txt'

try:
    my_tasks_file = open(file_path, 'r', encoding='UTF-8')
    content = my_tasks_file.read()
    print(content)
    print(type(content))
except FileNotFoundError as error:
    print(f'Nem találom a megadott fájlt: {file_path}')
finally:
    my_tasks_file.close()


#--------------------------------------------------------------------------------------

# Szöveges fájlok megnyitása - AJÁNLOTT megoldás
# https://realpython.com/python-with-statement/#the-with-statement-approach

# Teljes tartalom beolvasása
file_path = r'files\tasks.txt'

with open(file_path, 'r', encoding='UTF-8') as my_tasks_file:
    content = my_tasks_file.read()
    print(content)
    print(type(content))

# Soronkénti beolvasás
print()
with open(file_path, 'r', encoding='UTF-8') as my_tasks_file:
    content = my_tasks_file.readlines()
    print(content)
    print(f'Sorok száma: {len(content)}')

# Soronkénti beolvasás for ciklussal
print()
with open(file_path, 'r', encoding='UTF-8') as my_tasks_file:
    for line in my_tasks_file:
        print(line[:-1])
        # print(line, end='')

# Beolvasás while ciklussal
print()
with open(file_path, 'r', encoding='UTF-8') as my_tasks_file:
    counter = 1
    line = my_tasks_file.readline()
    while line:
        print(f'{counter}. sor: {line[:-1]}')
        counter += 1
        line = my_tasks_file.readline()

# Hibakezelés
print()
try:
    with open(r'files\tas.txt', 'r', encoding='UTF-8') as my_tasks_file:
        for line in my_tasks_file:
            print(line[:-1])
            # print(line, end='')
except FileNotFoundError as error:
    print(error)


#--------------------------------------------------------------------------------------------------
# Szöveges fájlok írása - Felülírás, hozzáfűzés

file_path = r'files\tasks.txt'
user_input = input("Új teendő: ")

#FELÜLÍRJA A MEGLÉVŐ FÁJLUNKAT
with open(file_path, 'w', encoding='UTF-8') as my_tasks_file:
    my_tasks_file.write(user_input+'\n')
    list_to_write = ['Lista elem1\n', 'Lista elem2\n']
    my_tasks_file.writelines(list_to_write)

#HOZZÁFŰZÜNK A FÁJLHOZ
with open(file_path, 'a', encoding='UTF-8') as my_tasks_file:
    line = 'Ezt még szeretném kiírni\n'
    my_tasks_file.write(line)
    #writelines() is ugyanúgy elérhető