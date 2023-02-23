# Feladat
# 1. Egészítsd ki az alábbi függvényt úgy, hogy a megadott esetekben kivételt dobjon.
#
# 2. Iterálj végig a lenn található user_ids listán és hívd meg mindegyikre a friendly_form_of függvényt
# 2.1 Ha megfelelő az id, akkor írasd ki a függvény visszatérítési értékét a képernyőre ÉS tedd bele a kezdetben üres,
# friendly_ids gyűjtőlistába
# 2.2 Kezeld le a két várható kivételtípust: írasd ki az üzenetüket. Ezeket az id-kat NE tárold el
#
# 3 A ciklus lefutása után
# 3.1 töröld a user_ids listát
# 3.2 írasd ki a képernyőre a friendly_ids listát

def friendly_form_of(id: int) -> str:
    """
    :param id: Az átalakítani kívánt felhasználói azonosító
    :return: 'USER-' prefixel ellátott felhasználói azonosító
    :raises TypeError: ha az id nem integer
    :raises ValueError: ha az id < 0 vagy id > 150
    """

    if type(id) is not int:
        raise TypeError(f'Nem megfelelő trípusú id: {id} - {type(id)}')

    if not 0 <= id <= 150:
        raise ValueError(f'Tartományon kívüli id (0-150): {id}')

    return f'USER-{id}'


user_ids = [1, 200, -3, 240, 100, 50, 'száz', 149.5]
friendly_ids = []

for user_id in user_ids:
    try:
        print(friendly_form_of(user_id))
        friendly_ids.append(user_id)
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)

del user_ids
print(friendly_ids)