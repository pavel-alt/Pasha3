from random import randint


def my_f(i):
    i = i ** 2
    return i


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_t_list = [("x", 1), ("z", 3), ("y", 4)]
name_list = ["Паша", "Катя", "Настя", "Игорь"]

j = [(name, i) for i, name in enumerate(name_list, 5)]
print(j)

k = {name: i for i, name in enumerate(name_list)}
print(k)

a = [i + 1 for i in my_list]
print(a)
a1 = list(map(lambda x: x + 1, my_list))
print(a1)
a2 = list(map(my_f, my_list))
print(a2)

b = [i for i in my_list if i % 2 == 0]
print(b)

c = [str(i) for i in my_list]
c1 = list(map(str, my_t_list))
print(type(c1[0]))

d = {i for i in (0, 1, 2, 3, 1, 5, 6, 1, 8, 9)}
print(d)

e = {k: v for k, v in my_t_list}
print(e)

f = [i + 1 if i % 2 == 0 else i / 2 for i in my_list]
print(f)

g = [i.upper() for i in "Hello World"]
print(g)

h = [randint(0, 100) for _ in range(100)]   # = h = [randint(0, 100) for i in range(100)]
print(h)


