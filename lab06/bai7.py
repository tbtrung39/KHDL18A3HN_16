list = [
    ["Mon",73],
    ["Tue",89],
    ["Wed",95],
    ["Thu",103],
    ["Fri",115],
    ["Sat",128],
    ["Sun",120],
]
print("Danh_sach_list: ")
for item in list:
    print(item)
pt_thu_hai_sublist_pt_thu_ba = list[2][1]
print("Phần tử thứ 2 của sublist thứ 3: ",pt_thu_hai_sublist_pt_thu_ba)
do_dai_list=len(list)
print("Độ dài danh sách trước khi thêm phần tử: ",do_dai_list)
sublist_moi = ["Extra_day",150]
list.append(sublist_moi)
print("Danh sách khi thêm phần tử mới: ")
for item in list:
    print(item)
tong_sale = list[0][1]=list[1][1]+list[5][1]+list[6][1]
print("Tong sale value của thứ2,3,7,cn là: ",tong_sale)