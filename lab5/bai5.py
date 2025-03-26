str=str(input("Nhap vao cac so ky tu: "))
print("Chuoi ky tu vua nhap lai:",str)
str1=""
for char in str:
    if char.isdigit():
        str1+=char
print(str1)
if str1:
    number=int(char)
    tong=0
    for i in range(1, number):
        if number%1==0:
            tong+=1
    if number==tong:
        print("Day la so hoan hao")
    else:
        print("Day khong phai la so hoan hao")
        