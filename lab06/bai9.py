ds = list(map(int, input("Nhập danh sách số nguyên, cách nhau bởi dấu cách: ").split()))
assert all(so % 2 == 0 for so in ds), "Danh sách chứa số lẻ!"
print("Danh sách hợp lệ, tất cả số đều là số chẵn:", ds)
