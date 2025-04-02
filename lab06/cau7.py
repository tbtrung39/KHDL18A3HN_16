list_=[["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
print("danh sach list_: ")
for item in list_:
    print(item)

phan_tu_thu_hai_sublist_thu_ba=[2][1]
print("phan tu thu hai sublist thu 3 la: ",phan_tu_thu_hai_sublist_thu_ba)

do_dai_list=len(list_)
print("do dai danh sach truoc khi them phan tu: ",do_dai_list)

new_sublist=["extra_day",150]
list_.append(new_sublist)
print("danh sach khi them phan tu moi: ")
for item in list_:
    print(item)

tong_sale=list_[0][1]=list_[1][1]+list_[5][1]+list_[6][1]
print("tong sale vulue cua thu hai, thu ba, thu bay, chu nhat la: ", tong_sale)