Str1 = input("Nhập chuỗi thứ nhất: ")
Str2 = input("Nhập chuỗi thứ hai: ")
s = ""
chuoi_min =min(len(Str1),len(Str2))
for i in range(chuoi_min):
    s+=Str1[i]+Str2[i]
s += Str1[chuoi_min:]+Str2[chuoi_min:]
print("Chuỗi sau khi trộn: ",s)