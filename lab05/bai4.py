Str1 = input("Nhap chuoi mot: ")
Str2 = input("Nhap chuoi hai: ")
kq = ""
max_len = max(len(Str1), len(Str2))
for i in range(max_len):
    if i < len(Str1):  
        kq += Str1[i]
    if i < len(Str2):  
        kq += Str2[i]
print("Hai chuoi tron la:", kq)