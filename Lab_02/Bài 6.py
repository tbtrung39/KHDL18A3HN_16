n = int(input("Nhập số nguyên có ba chữ số: "))
if 100 <= n <= 999:
    tram= n// 100
    chuc = (n % 100) // 10
    don_vi = n % 10
    if tram == 1:
        doc_so = "Một trăm"
    elif tram == 2:
        doc_so = "Hai trăm"
    elif tram == 3:
        doc_so = "Ba trăm"
    elif tram == 4:
        doc_so = "Bốn trăm"
    elif tram == 5:
        doc_so = "Năm trăm"
    elif tram == 6:
        doc_so = "Sáu trăm"
    elif tram == 7:
        doc_so = "Bảy trăm"
    elif tram == 8:
        doc_so = "Tám trăm"
    else:
        doc_so = "Chín trăm"
    if chuc == 0 and don_vi != 0:
        doc_so = doc_so+ " linh"
    elif chuc == 1:
        doc_so = doc_so+ " mười"
    elif chuc == 2:
        doc_so = doc_so+ " hai mươi"
    elif chuc == 3:
        doc_so = doc_so+ " ba mươi"
    elif chuc == 4:
        doc_so = doc_so+ " bốn mươi"
    elif chuc == 5:
        doc_so = doc_so+ " năm mươi"
    elif chuc == 6:
        doc_so = doc_so+ " sáu mươi"
    elif chuc == 7:
        doc_so = doc_so+ " bảy mươi"
    elif chuc == 8:
        doc_so = doc_so+ " tám mươi"
    elif chuc == 9:
        doc_so = doc_so+ " chín mươi"
    if don_vi == 1:
        doc_so = doc_so+ " một"
    elif don_vi == 2:
        doc_so = doc_so+ " hai"
    elif don_vi == 3:
        doc_so = doc_so+ " ba"
    elif don_vi == 4:
        doc_so = doc_so+ " bốn"
    elif don_vi == 5 and chuc != 0:
        doc_so = doc_so+ " lăm"
    elif don_vi == 5:
        doc_so = doc_so+ " năm"
    elif don_vi == 6:
        doc_so = doc_so+ " sáu"
    elif don_vi == 7:
        doc_so = doc_so+ " bảy"
    elif don_vi == 8:
        doc_so = doc_so+ " tám"
    elif don_vi == 9:
        doc_so = doc_so+ " chín"
    print("Cách đọc: ", doc_so.strip())
else:
    print("Vui lòng nhập số nguyên có ba chữ số!")