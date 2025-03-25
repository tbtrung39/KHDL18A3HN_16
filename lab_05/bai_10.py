Str1 = input("Nhập chuỗi 1: ")
Str2 = input("Nhập chuỗi 2: ")
count = ''
start = 0
while True:
    start = Str1.find(Str2, start)
    if start == -1:
        break
    count += start
    start += 1
print("Ký tự con chung của 2 chuỗi là: ", count)