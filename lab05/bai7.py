str=int(input("nhap vao cac so ky tu: "))
print("chuoi ky tu vua nhap la: ", str)
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
        print("day la so hoan hao")
    else:
        print("day khong phai la so hoan hao")