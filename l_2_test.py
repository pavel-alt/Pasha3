# a = 1
# b = 2
# print(a, b)
#
# a, b = b, a
# print(a, b)


# def ext_func(var_1):
#     def int_func(var_2):
#         return var_1 + var_2
#         print(var_1)
#         print(var_2)
#     return int_func
#
# f_obj = ext_func(200) # f_obj - функция
# print(f_obj(300))
#
#

l2 = [1, 2, 3, 4, 5]
c = map(lambda x: x * 10, l2)
print(c)
