a = [[1, 2, 3], 4, 5, 6, 7, 8, 9]

b = a
b.insert(0, [1, 2, 3])
print(b)

c = a
c.insert(8, [1, 2, 3])
print(c)

d = a
d.insert(5, [1, 2, 3])
print(d)

k = int(input("Nhập k = "))
for i in a:
    if a.index(i) == k:
        a.remove(k)
print(a)

e = [a, b, c, d]
print(sorted(e))