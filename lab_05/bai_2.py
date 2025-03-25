Str = input("Nhập từ bàn phím chuỗi ký tự: ")
count = 0
con = 0
for i in Str:
    if i.isdigit():
        count += 1
    elif i.isalpha():
        con += 1
print("Số chữ cái tiếng Anh là:", con)
print("Số trong chuỗi là:", count)