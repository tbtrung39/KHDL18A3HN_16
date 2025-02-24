print('\n\n\t\t=====TÍNH SỐ KW TIÊU THỤ=====')
don_gia1 = 2000
don_gia2 = 2500
don_gia3 = 3000
don_gia4 = 5000
KW = float(input("Nhập số KW: "))
if 0 <= KW <= 100:
    tien_dien1 = KW*don_gia1
    print("Số điện tiêu thụ: ",tien_dien1)
elif 101 <= KW <= 200:
    tien_dien2 = KW*don_gia2
    print("Số điện tiêu thụ: ",tien_dien2)
elif 201<= KW <= 300:
    tien_dien3 = KW*don_gia3
    print("Số điện tiêu thụ: ",tien_dien3)
elif KW >= 300:
    tien_dien4 = KW*don_gia4
    print("Số điện tiêu thụ: ",don_gia4)
