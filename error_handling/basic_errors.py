# EAFP - Easier to ask forgivness than permission

# import os
#
# def process_file(path):
#     pass
#
# p = '/path/to/datafile'
#
# try:
#     process_file(p)
# except OSError as e:
#     print(f'Error: {e}')

#--------------------ZeroDivisionError-----------------

try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('Denominator can not be 0!')

print('Megyünk tovább...')

#-----------------------NameError----------------------

try:
    num1 = 10
    num2 = 0
    result = num1 / dum2
    print(result)
except ZeroDivisionError:
    print('Denominator can not be 0!')
except NameError as e:
    print(f'There is an unknown variable. Message: {e}')

print('Megyünk tovább...')

#-----------------------TypeError----------------------

try:
    num1 = 10
    num2 = '10'
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('Denominator can not be 0!')
except NameError as e:
    print(f'There is an unknown variable. Message: {e}')
except BaseException as be:
    print('Unknown error:')
    print(be)
finally:
    # Bármi történt menet közben, ez lefut. Takarítási feladatok (fájl lezárás, memória felszabadítás stb.)
    print('Üdv a finally blokkból')

print('Megyünk tovább...')