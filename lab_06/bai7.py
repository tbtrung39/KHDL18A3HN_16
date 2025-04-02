list_=[
    ["mon",73],
    ["tue",89],
    ["wed",95],
    ["thu",103],
    ["fri",115],
    ["sat",128],
    ["sun",120],
]
print("Danh sach list_:")
for item in list_:
    print(item)

phan_tu_thu_hai_sublist_thu_ba=list_[2][1]
print("Phan tu thu hai cua sublist thu ba:",phan_tu_thu_hai_sublist_thu_ba)

do_dai_list=len(list_)
print("Do dai danh sach truoc khi them phan tu:",do_dai_list)
new_sublist=["extra_day",150]
list_.append(new_sublist)
print("Danh sach khi them phan tu moi:")
for item in list_:
    print(item)

tong_sale=list_[0][1]=list_[1][1]+list_[5][1]+list_[6][1]
print("Tong sale value cua thu hai, thua ba, thua bay, chua nhat:",tong_sale)