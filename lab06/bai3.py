#1
list = []
while True:
    cac_phan_tu = int(input("Nhập các số tự nhiên(Nhập '0'để kết thúc): ")) 
    if cac_phan_tu == 0:
        break
    list. append(cac_phan_tu)
print("danh sach cac gia tri: ", list)
#2

26
pt_duong = []
khong_duong = []
for i in list:
    if i>0:
        pt_duong.append(i)
    else:
        khong_duong.append(i)
list = pt_duong + khong_duong
m = int(input("Nhập số m cần chèn : "))
list.insert(0,m)
list.append(m)
if len(list)>=5:
    list.insert(5,m)
else:
    list.append(m)
print("Danh sách sau khi chèn m: ",list)