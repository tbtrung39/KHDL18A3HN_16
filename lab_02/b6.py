
n = int(input("Nhập vào một số nguyên có ba chữ số: "))

tram = n // 100
chuc = (n // 10) % 10
don_vi = n % 10

if tram == 1:
    tram_str = "một trăm"
elif tram == 2:
    tram_str = "hai trăm"
elif tram == 3:
    tram_str = "ba trăm"
elif tram == 4:
    tram_str = "bốn trăm"
elif tram == 5:
    tram_str = "năm trăm"
elif tram == 6:
    tram_str = "sáu trăm"
elif tram == 7:
    tram_str = "bảy trăm"
elif tram == 8:
    tram_str = "tám trăm"
elif tram == 9:
    tram_str = "chín trăm"

if chuc == 0:
    chuc_str = "linh"
elif chuc == 1:
    chuc_str = "mười"
elif chuc == 2:
    chuc_str = "hai mươi"
elif chuc == 3:
    chuc_str = "ba mươi"
elif chuc == 4:
    chuc_str = "bốn mươi"
elif chuc == 5:
    chuc_str = "năm mươi"
elif chuc == 6:
    chuc_str = "sáu mươi"
elif chuc == 7:
    chuc_str = "bảy mươi"
elif chuc == 8:
    chuc_str = "tám mươi"
elif chuc == 9:
    chuc_str = "chín mươi"

if don_vi == 0:
    don_vi_str = ""
elif don_vi == 1:
    if chuc == 1:
        don_vi_str = "một"
    else:
        don_vi_str = "mốt"
elif don_vi == 2:
    don_vi_str = "hai"
elif don_vi == 3:
    don_vi_str = "ba"
elif don_vi == 4:
    don_vi_str = "bốn"
elif don_vi == 5:
    don_vi_str = "năm"
elif don_vi == 6:
    don_vi_str = "sáu"
elif don_vi == 7:
    don_vi_str = "bảy"
elif don_vi == 8:
    don_vi_str = "tám"
elif don_vi == 9:
    don_vi_str = "chín"
    
if chuc == 0 and don_vi == 0:
    print(tram_str)
elif chuc == 0:
    print(tram_str, chuc_str, don_vi_str)
elif don_vi == 0:
    print(tram_str, chuc_str)
else:
    print(tram_str, chuc_str, don_vi_str)
