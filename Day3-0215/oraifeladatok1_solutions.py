print('************ 1. feladat ******************')
'''
Adottak a következő szavak: két, macska, van.
Jelenítsd meg őket egy mondatban! (Két macska van.)
Jelenítsd meg őket egy mondatban, de számot használj! (2 monitor van.)
'''
print("***Megoldás***")
# str_1 = "két"
# str_2 = "macska"
# str_3 = "van"
#
# print(str_1.capitalize(), str_2, str_3 + ".")
# print(str_1.capitalize() + " " + str_2 + " " + str_3 + ".")
# print(f'{str_1.capitalize()} {str_2} {str_3}.')
#
# w_1 = 2
# w_2 = "monitor"
# w_3 = "van"
#
# print(str(w_1), w_2, w_3 + ".")
# print(str(w_1) + " " + w_2 + " " + w_3 + ".")
# print(f'{w_1} {w_2} {w_3}.')



print('************ 2. feladat ******************')
'''
Kérj be a felhasználótól három számot!
Add meg a három szám összegét, kivéve ha a három szám azonos, akkor a szorzatukat add meg!
'''
print("***Megoldás***")
# a = int(input("Első szám: "))
# b = int(input("Második szám: "))
# c = int(input("Harmadik szám: "))
# if a == b== c:
#   print(f'A három megadott szám: {a}, {b}, {c}; szorzatuk {a*b*c}.')
# else:
#   print(f'A három megadott szám: {a}, {b}, {c}; összegük {a+b+c}.')


print('************ 3. feladat ******************')
'''
Add meg egy felhasználótól bekért szó páratlan helyen lévő betűjeit és írasd őket ki! (pl. alma esetén a megoldás a,m)
'''
print("***Megoldás***")
#user_string = input("Adj meg egy szót! : ")
#
# print('\n----A verzió----')
# print(user_string[0::2])
#print(type(user_string[0::2]))
#
# print('\n----B verzió----')
# for s in user_string[0::2]:
#     print(s)
#
# print('\n----C verzió----')
# for s in user_string[0::2]:
#     print(s, end=' ')
# print('\n')
#
# print('----D verzió----')
# odd_chs = []
# for i in range(len(user_string)):
#     if i % 2 == 0:
#         odd_chs.append(user_string[i])
# print(odd_chs)
# print(type(odd_chs))


print('************ 4. feladat ******************')
'''
Készíts egy öt elemű felhasználótól bekért törtszám listát! 
Jelenítsd meg a képernyőn a listát!
'''
# print("***Megoldás***")
# user_list = []
# print("Make a 5 element list!")
# for i in range(1, 6):
#     user_input = input(f'Give the {i}. number! : ')
#     user_list.append(float(user_input))
# print(user_list)

print('************ 5. feladat ******************')
'''
Ellenőrizd, hogy megegyezik-e egy lista első és utolsó eleme! Írasd ki a megfelelő boolean értéket a képernyőre!
A listát Te határozhatod meg.
'''
print("***Megoldás***")
# print('----A verzió----')
# lista_a = [15, 43, 35, 40, 15]
# lista_b = [80, 40, 20, 10, 5]
#
# if lista_a[0] == lista_a[-1]:
#     print(True)
# else:
#     print(False)
#
# if lista_b[0] == lista_b[-1]:
#     print(True)
# else:
#     print(False)
# print('----B verzió----')
# lista_c = [25, 43, 35, 40, 25]
# print(lista_c[0] == lista_c[-1])