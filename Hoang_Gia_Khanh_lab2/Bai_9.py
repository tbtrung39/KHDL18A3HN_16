kw = int(input("Nhập số điện tiêu thụ: "))
if 0 <= kw <= 100:
    print(f"Đơn giá 2000 đồng/KW, đã dùng {kw} KW, tổng = {(kw * 2000):_} đồng")
elif 101 <= kw <= 200:
    print(f"Đơn giá 2500 đồng/KW, đã dùng {kw} KW, tổng = {(kw * 2500):_} đồng")
elif 201 <= kw <= 300:
    print(f"Đơn giá 3000 đồng/KW, đã dùng {kw} KW, tổng = {(kw * 3000):_} đồng")
elif kw > 300:
    print(f"Đơn giá 5000 đồng/KW, đã dùng {kw} KW, tổng = {(kw * 5000):_} đồng")
else:
    print("Nhập lại")