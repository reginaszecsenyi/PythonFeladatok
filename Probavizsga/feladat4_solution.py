'''Python
def special_eleven(x):
    pass # write your code here

special_eleven(22)
# >>> True
special_eleven(23)
# >>> True
special_eleven(24)
# >>> False


Hívd meg a függvényed az alábbi számokra:
23, 24, 122, 96
'''


def special_eleven(x):
    if x % 11 == 0:
        print(True)
    elif x % 11 == 1:
        print(True)
    else:
        print(False)

# 1. verzió
special_eleven(23)
special_eleven(24)
special_eleven(122)
special_eleven(96)


# 2. verzió
# list_of_nr = [23, 24, 122, 96]
# for nr in list_of_nr:
#     special_eleven(nr)


# 3. verzió
# for i in range(4):
#     special_eleven(int(input("Give me a number: ")))


# 4. verzió
# number_list = []
# for i in range(4):
#     number_list.append(int(input("Give me a number: ")))
# for nr in number_list:
#     special_eleven(nr)