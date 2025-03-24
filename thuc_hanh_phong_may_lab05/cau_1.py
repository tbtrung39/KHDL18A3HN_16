#Bài 1:
#Cách 1
chuoi = input("Nhập chuỗi: ")
ky_tu = 0
for k in chuoi:
    if k.isdigit():
        ky_tu += 1
print("Số chữ số có trong chuỗi là:", ky_tu)

#Cách 2
chuoi = input("nhập chuỗi: ")
ky_tu = 0
for k in chuoi:
    ky_tu += 1 if '0' <= k <= '9' else 0
print("Số chữ số có trong chuỗi là:", ky_tu)