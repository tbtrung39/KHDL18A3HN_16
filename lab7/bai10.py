m=input("Nhap m: ")
n=input("Nhap n: ")

p=set(m)
q=set(n)
r=p.intersection(q)

a=0
for i in r:
    a+=int(i)
print(a)