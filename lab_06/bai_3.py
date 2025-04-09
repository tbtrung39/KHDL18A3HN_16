a = []

for i in range(-11,11):
    a.append(i)

print(a)

b = a[::-1]
print(b)

print(sorted(b))

m = int(input("Nhập m = "))
p = a
p.insert(0, m)
print(p)

q = a
q.insert(-1, m)
print(q)

r = a
r.insert(5, m)
print(r)