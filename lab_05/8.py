Str = input("Nhập chuỗi: ")
lst = Str.strip().split(" ")
count = 0
for i in lst:
     count += 1
print("Số từ đơn là:", count)