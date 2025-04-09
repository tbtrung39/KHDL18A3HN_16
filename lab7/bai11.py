sv=int(input("Nhap so sinh vien: "))
C=set()
Java=set()
Python=set()
for i in range(1, sv+1):
    if i%1==0:
        C.add(i)
    elif i%2==0:
        Java.add(i)
    elif i%3==0:
        Python.add(i)

a=C.intersection(Java)
b=Java.intersection(Python)
d=Python.intersection(C)

print("1 Ngon ngu lap trinh:", C)
print("2 Ngon ngu lap trinh:")
print("3 Ngon ngu lap trinh:")