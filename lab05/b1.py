# cau 1
str = input("Nhập chuỗi ký tự: ")
count = 0
for i in str:
    if i.isdigit():  
        count += 1
print("Số lượng ký tự là số trong chuỗi:", count)