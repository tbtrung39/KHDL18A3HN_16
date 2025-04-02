a=[]
while True:
    num=int(input("nhap vao mot so tu nhien: "))
    if num==0:
        break
    a.append(num)
print("danh sach ban dau: ",a)

duong=[]
khong_duong=[]
for x in a:
    if x>0:
        duong.append(x)
    else:
        khong_duong.append(x)
a=duong+khong_duong
print("danh sach sau khi dua so duong len dau la: ",a)

m=int(input("nhap so m can chen: "))
a.insert(0,m)
a.append(m)
if len(a)>=5:
    a.insert(5,m)
else:
    a.append(m)
print("danh sach sau khi chen m: ",a)
