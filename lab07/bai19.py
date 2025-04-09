nhanvien = {}
n = int(input("Nhập số lượng nhân viên: "))
#b nhập tt nv
for i in range(n):
    print(f"\nNhập thông tin nhân viên thứ {i+1}:")
    ma = input("Mã nhân viên (4 chữ số): ")
    hoten = input("Họ tên (tối đa 20 ký tự): ")[:20]
    namsinh = int(input("Năm sinh: "))
    luong = float(input("Lương: "))
    nhanvien[ma] = {"hoten": hoten, "namsinh": namsinh, "luong": luong}
#c tìm nv theo mã 
x = input("\nNhập mã nhân viên cần tìm: ")
if x in nhanvien:
    print("Tìm thấy nhân viên:")
    print("Họ tên:", nhanvien[x]["hoten"])
    print("Năm sinh:", nhanvien[x]["namsinh"])
    print("Lương:", nhanvien[x]["luong"])
else:
    print("Không tìm thấy nhân viên có mã", x)
#d Tăng lương nv
y = input("\nNhập mã nhân viên cần tăng lương: ")
if y in nhanvien:
    nhanvien[y]["luong"] += 1_000_000
    print("Đã tăng lương cho nhân viên", y)
else:
    print("Không tìm thấy nhân viên có mã", y)
#e xoa mãa nv 
z = input("\nNhập mã nhân viên cần xóa: ")
if z in nhanvien:
    del nhanvien[z]
    print("Đã xóa nhân viên có mã", z)
else:
    print("Không tìm thấy nhân viên có mã", z)
#f sap xep
print("\nDanh sách nhân viên sắp xếp theo năm sinh giảm dần:")
sapxep = sorted(nhanvien.items(), key=lambda item: item[1]["namsinh"], reverse=True)
for ma, info in sapxep:
    print(f"Mã: {ma}, Họ tên: {info['hoten']}, Năm sinh: {info['namsinh']}, Lương: {info['luong']}")
