import hashlib

# # Список всех алгоритмов доступных в системе
# print(hashlib.algorithms_available)
#
# # Список всех существующих алгоритмов
# print(hashlib.algorithms_guaranteed)

b = "test"
a = hashlib.sha224(b.encode())
c = hashlib.sha224(b'test')
print(a)
print(c)
res = a.hexdigest()
print(res)
res_2 = c.hexdigest()
print(res_2)
print(res == res_2)
