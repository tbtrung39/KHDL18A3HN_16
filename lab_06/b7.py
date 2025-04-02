import random

# 1. Tạo và in danh sách
List_ = [
    ["mon", 73], ["tue", 89], ["wed", 95], 
    ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]
]
print("Danh sách gốc:")
for sublist in List_:
    print(sublist)

# 2. Chọn phần tử thứ 2 của sublist thứ 3
selected_value = List_[2][1]
print("\nGiá trị thứ 2 của sublist thứ 3:", selected_value)

# 3. Kiểm tra độ dài và thêm sublist ngẫu nhiên
length = len(List_)
print("\nĐộ dài ban đầu của List_:", length)
new_sublist = ["new_day", random.randint(50, 150)]
List_.append(new_sublist)
print("Đã thêm sublist mới:", new_sublist)
print("Độ dài sau khi thêm:", len(List_))

# 4. Tính tổng sale value các ngày chỉ định
target_days = ["mon", "tue", "sat", "sun"]
total_sales = sum(sublist[1] for sublist in List_ if sublist[0] in target_days)
print("\nTổng sale value các ngày thứ 2, 3, 7, CN:", total_sales)
