# Egészítsük ki a print_(animal) függvényt úgy, hogy a leírásában megfogalmazott
# kimenetet adja.

animal_types = {
    0: 'emlős',
    1: 'madár',
    2: 'hal',
    3: 'kétéltű'
}

animals = {
    'ID-01': { 'name': 'Elefánt', 'type': 0},
    'ID-02': { 'name': 'Béka', 'type': 3},
    'ID-03': { 'name': 'Sas', 'type': 1},
    'ID-04': { 'name': 'Keszeg', 'type': 2},
}


def print_(animal_id: str, animal: dict) -> None:
    '''Elvárt kimenet: Az [ID] azonosítójú [ÁLLATNÉV] egy [ÁLLATÍPUS - olvasható formában]'''
    animal_type_code = animal[type]
    animal_type = animal_types[animal_type_code]
    print(f'Az {animal_id} azonosítójú {animal["name"]} egy {animal_type}')

if __name__ == '__main__':
    '''Iteráljunk végig minden tárolt állaton és hívjuk meg rájuk a print_ függvényt'''
    for animal_id, animal, in animals.items():
        print_(animal_id, animal)