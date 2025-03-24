#Bài 2:
#Cách 1
chuoi = input('nhâp chuỗi: ')
ky_tu = 0
for k in chuoi:
    if not (k.isalpha() or k.isdigit()):
        ky_tu += 1
print("Số ký tự không phải chữ cái và không phải số là:", ky_tu)

#Cách 2
chuoi = input('nhập chuỗi: ')
ky_tu = 0
for k in chuoi:
    ma = ord(k)
    if not (48 <= ma <= 57 or 65 <= ma <= 90 or 97 <= ma <= 122):
        ky_tu += 1
print("Số ký tự không phải chữ cái và không phải la số:", ky_tu)