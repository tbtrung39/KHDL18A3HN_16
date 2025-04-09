sinh_vien = int(input("Nhap so sinh vien: "))

C = set()
Java = set()
Python = set()

for i in range(1, sinh_vien + 1):
    if i % 1 == 0:
        C.add(i)
    elif i % 2 == 0:
        Java.add(i)
    elif i % 3 == 0:
        Python.add(i)

a = C.intersection(Java)
b = Java.intersection(Python)
c = Python.intersection(C)

print("1 ngôn ngữ lập trinh:")
print("2 ngôn ngữ lập trình:")
print("3 ngôn ngữ lập trinh:")