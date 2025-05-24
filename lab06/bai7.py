import random
#1
list_ = [['mon', 73], ['tue', 89], ['wed', 95], ['thu', 103], 
         ['fri', 115], ['sat', 128], ['sun', 120]]
#2
print('Danh sách list:')
for item in list_:
    print(item)
#3
print('Phần tử thứ 2 của sublist vị trí 3:', list_[2][1])
#4 
random_sublist = random.choice(list_)[:]
random_sublist[1] = random.randint(50, 150)
list_.append(random_sublist)
print('Danh sách list sau khi thêm phần tử ngẫu nhiên:', list_)
#5
tong_gia_tri = sum(list_[i][1] for i in [1, 2, 5, 6])
print('Tổng giá trị của thứ hai, ba, bảy, chủ nhật:', tong_gia_tri)