#Bài 1
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Bạn đã nhập số âm. Vui lòng nhập lại!")
    n = int(input("Nhập số nguyên dương n:"))

#a)
S4 = 0 
i = 0
while i <= n:
    S4 += i * i
    i += 1
print("S4=", S4)

#b)
S5 = 0 
i = 1
while i <= 2 * n:
    S5 += i * i * i 
    i += 1
print("S5=", S5)

#c)
S6 = 0
i = 2
while i <= 2 * n + 1:
    S6 += i * i * i * i
    i += 1
print("S6=", S6)
