import random
List_ = [ ["mon", 73], ["tue", 89], ["wed", 95], 
    ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120] ]
for i in List_:
    print("Danh sách List_: ", i)
value = List_[2][1]
print(" Giá trị thứ 2 của sublist thứ 3:", value)
length = len(List_)
print(" Độ dài của List_:", length)
sublist = ["new_day", random.randint(50, 150)]
List_.append(sublist)
print(" Đã thêm sublist mới:", sublist)
print(" Độ dài sau khi thêm:", len(List_))
target_days = ["mon", "tue", "sat", "sun"]
total_sales = sum(sublist[1] for sublist in List_ if sublist[0] in target_days)
print(" Tổng sale value các ngày thứ 2, 3, 7, chủ nhật: ", total_sales)