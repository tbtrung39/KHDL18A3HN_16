str=input("nhap chuoi ky tu: ")
max_char=''
max_count=0
for char in str:
    count=str.count(char)
    if count > max_count:
        max_count = count
        max_char = char
result = max_char * max_count
print("chuoi con dai nhat gom cac ky tu giong nhau la: ", result)
