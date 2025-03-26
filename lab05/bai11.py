# nhap chuoi ky tu str
str=input("nhap mot chuoi ky tu nhi phan: ")
# kiem tra chuoi str co phai chuoi nhi phan khong
binary=True
for char in str:
    if char != '0' and char != '1':
        binary=False
        break
# neu chuoi str la nhi phan, chuyen sang so thap phan va in ket qua ra man hinh
if binary:
    decimal=0
    for i in range(len(str)):
        decimal += int(str[i])*(2**(len(str)-i -1))
    print("so thap phan tuong ung la: ", decimal)
else:
    print("chuoi ky tu ban nhap khong phai chuoi nhi phan")