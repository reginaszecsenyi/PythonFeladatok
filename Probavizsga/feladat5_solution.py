'''
Feladat:
def between(a, b):
    pass # write your code here

print(between(5, 10))
# >>> [5,6,7,8,9,10]

print(between(1,2))
# >>> [1,2]
'''

# # 1. verzió
def rev_num1(a_nr, b_nr):
    nr_list = []
    for i in range(a_nr, b_nr + 1):
        nr_list.append(i)
    return nr_list

user_input_a = int(input('Give an integer number : '))
user_input_b = int(input('Give an integer number : '))

print(rev_num1(user_input_a, user_input_b))

# # 2. verzió
# def rev_num2(x_nr, y_nr):
#     return list(range(x_nr, y_nr + 1))
#
# user_input_x = int(input('Give an integer number : '))
# user_input_y = int(input('Give an integer number : '))
#
# print(rev_num2(user_input_x, user_input_y))