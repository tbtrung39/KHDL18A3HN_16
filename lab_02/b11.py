
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

if thang == 1:
    so_ngay = 31
elif thang == 2:
    so_ngay = 28
elif thang == 3:
    so_ngay = 31
elif thang == 4:
    so_ngay = 30
elif thang == 5:
    so_ngay = 31
elif thang == 6:
    so_ngay = 30
elif thang == 7:
    so_ngay = 31
elif thang == 8:
    so_ngay = 31
elif thang == 9:
    so_ngay = 30
elif thang == 10:
    so_ngay = 31
elif thang == 11:
    so_ngay = 30
elif thang == 12:
    so_ngay = 31
else:
    so_ngay = 0
    
if so_ngay == 0:
    print("Tháng không hợp lệ!")
elif ngay < 1 or ngay > so_ngay:
    print("Ngày không hợp lệ!")
else:
    if ngay < so_ngay:
        ngay_tiep = ngay + 1
        thang_tiep = thang
    else:
        ngay_tiep = 1
        if thang == 12:
            thang_tiep = 1
        else:
            thang_tiep = thang + 1

    print("Ngày tiếp theo là:", ngay_tiep, "/", thang_tiep)
