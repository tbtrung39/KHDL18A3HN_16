# cach 1
str=input("nhap vao mot chuoi ky tu: ")
print("chuoi ky tu vua nhap: ",str)
dem=0
for c in str:
    if '0'<=c<='9':
        dem+=1
print("so cac ky tu la so trong chuoi chuoi da nhap = ",dem)

# cach 2
str = input("nhap mpt chuoi ky tu: ")
c=0
for char in str:
    if char.isdigit():
        c+=1
print("so ky tu trong choui la: ",c)
