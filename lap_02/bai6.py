n = int(input("Nhập một số nguyên có ba chữ số: "))
if n < 100 or n > 999:
    print("Vui lòng nhập số nguyên có đúng ba chữ số.")
else:
    tram = n // 100
    chuc = (n // 10) % 10
    don_vi = n % 10
    if tram == 1:
        doc_tram = "Một trăm"
    elif tram == 2:
        doc_tram = "Hai trăm"
    elif tram == 3:
        doc_tram = "Ba trăm"
    elif tram == 4:
        doc_tram = "Bốn trăm"
    elif tram == 5:
        doc_tram = "Năm trăm"
    elif tram == 6:
        doc_tram = "Sáu trăm"
    elif tram == 7:
        doc_tram = "Bảy trăm"
    elif tram == 8:
        doc_tram = "Tám trăm"
    else:
        doc_tram = "Chín trăm"

    if chuc == 0 and don_vi != 0:
        doc_chuc = "Lẻ"
    elif chuc == 1:
        doc_chuc = "Mười"
    elif chuc == 2:
        doc_chuc = "Hai mươi"
    elif chuc == 3:
        doc_chuc = "Ba mươi"
    elif chuc == 4:
        doc_chuc = "Bốn mươi"
    elif chuc == 5:
        doc_chuc = "Năm mươi"
    elif chuc == 6:
        doc_chuc = "Sáu mươi"
    elif chuc == 7:
        doc_chuc = "Bảy mươi"
    elif chuc == 8:
        doc_chuc = "Tám mươi"
    elif chuc == 9:
        doc_chuc = "Chín mươi"
    else:
        doc_chuc = ""
        
    if don_vi == 1 and chuc > 1:
        doc_don_vi = "Mốt"
    elif don_vi == 1:
        doc_don_vi = "Một"
    elif don_vi == 2:
        doc_don_vi = "Hai"
    elif don_vi == 3:
        doc_don_vi = "Ba"
    elif don_vi == 4:
        doc_don_vi = "Bốn"
    elif don_vi == 5 and chuc != 0:
        doc_don_vi = "Lăm"
    elif don_vi == 5:
        doc_don_vi = "Năm"
    elif don_vi == 6:
        doc_don_vi = "Sáu"
    elif don_vi == 7:
        doc_don_vi = "Bảy"
    elif don_vi == 8:
        doc_don_vi = "Tám"
    elif don_vi == 9:
        doc_don_vi = "Chín"
    else:
        doc_don_vi = ""
    print(doc_tram, doc_chuc, doc_don_vi)