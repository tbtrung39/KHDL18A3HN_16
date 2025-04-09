list1 = list(map(int, input("Nhập danh sách các số (cách nhau bằng khoảng trắng): ").split()))
list2 = input("Nhập danh sách các tên (cách nhau bằng khoảng trắng): ").split()

if len(list1) != len(list2):
    print("Lỗi: Số lượng phần tử của hai danh sách không khớp!")
else:
    tu_dien = {list1[i]: list2[i] for i in range(len(list1))}
    print("Từ điển tạo được:", tu_dien)
