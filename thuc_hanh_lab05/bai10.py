s1 = input("Nhập chuỗi s1: ")
s2 = input("NHập chuỗi s2: ")
chuoi_max=""
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        sub =s1[i:j]
        if sub in s2 and len(sub) > len(chuoi_max):
            chuoi_max =sub
print("Chuỗi ký tự con chung của cả 2: ",chuoi_max)