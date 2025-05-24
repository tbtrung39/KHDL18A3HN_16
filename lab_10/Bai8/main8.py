import my_list

lst = list(map(int, input("Nhập danh sách số nguyên cách nhau bởi dấu cách: ").split()))

print("Tổng:", my_list.tong(lst))
print("Trung bình:", my_list.trung_binh(lst))
print("Lớn nhất:", my_list.lon_nhat(lst))
print("Nhỏ nhất:", my_list.nho_nhat(lst))
