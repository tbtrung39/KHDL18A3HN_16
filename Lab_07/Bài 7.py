import random 
so_phan_tu_A = int(input(" Nhập số phần tử của tập hợp A: "))
so_phan_tu_B = int(input(" Nhập số phần tử của tập hợp B: "))
danh_sach_ky_tu = input(" Nhập các ký tự chữ và số( cách nhau bằng dấu cách) : ").split()
A = set(random.sample(danh_sach_ky_tu, min(so_phan_tu_A, len(danh_sach_ky_tu))))
B = set(random.sample(danh_sach_ky_tu, min(so_phan_tu_B, len(danh_sach_ky_tu))))
phan_tu_chung = A& B
print(" Tập hợp A: ", A)
print(" Tập hợp B: ", B)
print(" Các phần tử chung của A và B: ", phan_tu_chung)