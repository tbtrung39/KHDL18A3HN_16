# bài 11
# nhập ngày và tháng từ bàn phím 
ngay = int(input("nhập ngày: "))
thang = int(input("nhập tháng: "))
# kiểm tra tính hợp lệ của tháng 
if thang < 1 or thang > 12:
    print("tháng không hợp lệ! vui lòng nhập lại số tháng")
else:
    if thang ==1 or thang ==3 or thang ==5 or thang ==7 or thang ==8 or thang ==10 or thang ==12:
        ngay_cuoi_cung = 31 
    elif thang ==4 or thang ==6 or thang ==9 or thang ==11:
        ngay_cuoi_cung = 30 
    elif thang ==2:
        ngay_cuoi_cung = 28 
    if ngay < 1 or ngay > ngay_cuoi_cung:
        print("Ngày không hợp lệ")
    else:
        if ngay < ngay_cuoi_cung:
            ngay +=1
        else:
            ngay = 1
            if thang ==12:
                thang = 1
            else:
                thang += 1
        print(f"ngày tiếp theo là: {ngay}/{thang}")