import Module1 
print("Giải phương trình:")
print("1. Bậc nhất (ax + b = 0)")
print("2. Bậc hai  (ax^2 + bx + c = 0)")
lua_chon = input("Chọn loại phương trình (1 hoặc 2): ")
if lua_chon == "1":
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    Module1.ptrinh_bac_nhat(a, b)
elif lua_chon == "2":
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    Module1.ptrinh_bac_hai(a, b, c)
else:
    print("Lựa chọn không hợp lệ.")