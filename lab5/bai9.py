#Cach 1
str=input("Nhap chuoi ky tu: ")
chuoi_dai_nhat=''
chuoi_hien_tai=''
for i in range(len(str)):
    if i==0 or str[i]==str[i-1]:
        chuoi_hien_tai+=str[i]
    else:
        if len(chuoi_hien_tai)>len(chuoi_dai_nhat):
            chuoi_dai_nhat=chuoi_hien_tai
        chuoi_hien_tai=str[i]
if len(chuoi_hien_tai)>len(chuoi_dai_nhat):
    chuoi_dai_nhat=chuoi_hien_tai
print("Chuoi con dai nhat gom cac ky tu giong nhau la:",chuoi_dai_nhat)

#Cach 2
str=input("Nhap chuoi ky tu: ")
max_char=''
max_count=0
for char in str:
    count=str.count(char)
    if count > max_count:
        max_count=count
        max_char=char
result=max_char*max_count
print("Chuoi con dai nhat gom cac ky tu giong nhua la:",result)