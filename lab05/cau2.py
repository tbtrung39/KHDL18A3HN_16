# cach 1
Str = input("Nhập chuỗi ký tự: ")
count = 0  
for i in Str:
    if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9'):
        count += 1  
print("Số ký tự không phải là chữ cái tiếng Anh và không phải là số:", count)
# cach 2
Str = input("Nhập chuỗi: ")
count = 0  
for i in Str:
    if not i.isalnum(): 
        count += 1
print("Số ký tự không phải là chữ cái tiếng Anh và không phải là số:", count)