list1 = []
while True:
    n = int(input("Nhập số: "))
    if n== 0:
        break
    list1.append(n)
print(" Danh sách ban đầu: ", list1)
so_duong= [] 
for x in list1:
    if x> 0:
        so_duong.append(x)
so_am= []
for i in list1:
    if i< 0:
        so_am.append(i)
list2 = so_duong + so_am
print(" Danh sách sau khi chuyển số dương lên đầu: ", list2)
m = int(input(" Nhập số cần chèn: "))
list2.insert(0, m)
list2.append(m)
if len(list2) >= 5:
    list2.insert(5, m)
print(f" Danh sách sau khi chèn số {m}: {list2}")