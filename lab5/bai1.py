#cach 1
str=input("Nhap vao mot chuoi ky tu: ")
print("Chuoi ky tu vua nhap: ",str)
dem=0
for c in str:
    if '0'<=c<="9":
        dem+=1
print("So cac ky tu la so trong chuoi da nhap = ",dem)

#cach 2
str=input("Nhap mot chuoi ky tu: ")
c=0
for char in str:
    if char.isdigit():
        c+=1
print("So ky tu trong chuoi la: ",c)