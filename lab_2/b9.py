# bài 9 
so_kw = float(input("nhập số kw điện: "))
if 0 <= so_kw <= 100:
    gia = 2000
    tien_dien = so_kw * gia 
    print("Tổng tiền điện: ", tien_dien)
elif 101 <= so_kw <= 200:
    gia = 2500 
    tien_dien = so_kw * gia 
    print("Tổng tiền điện: ", tien_dien)
elif 201 <= so_kw <= 300:
    gia = 3000
    tien_dien = so_kw * gia
    print("Tổng tiền điện: ", tien_dien)
elif so_kw <= 300:
    gia = 5000
    tien_dien = so_kw * gia 
    print("Tổng tiền điện: ", tien_dien)
else:
    print("số nhập không hợp lệ! vui lòng nhập lại")