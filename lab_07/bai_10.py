m = input("Nhập m = ")
n = input("Nhập n = ")

p = set(m)
q = set(n)

r = p.intersection(q)

a = 0
for i in r:
    a += int(i)

print(a)