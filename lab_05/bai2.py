s=input("nhap chuoi ky tu:")
count=0

for char in s:
    if not char.isdigit():
        count+=1

print("so ki tu khong phai so trong chuoi: ",count)
