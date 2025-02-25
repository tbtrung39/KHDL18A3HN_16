so = int(input("nhập số nguyên có ba chữ số:"))
if 100 <= so <= 999:
    hang_tram = so // 100
    hang_chuc = (so // 10) % 10
    hang_dv = so % 10

    if hang_tram == 1:
        doc_tram = "một trăm"
    elif hang_tram == 2:
        doc_tram = "hai trăm"
    elif hang_tram == 3:
        doc_tram = "ba trăm"
    elif hang_tram == 4:
        doc_tram = "bốn trăm"
    elif hang_tram == 5:
        doc_tram = "năm trăm"
    elif hang_tram == 6:
        doc_tram = "sáu trăm"
    elif hang_tram == 7:
        doc_tram = "bảy trăm"
    elif hang_tram == 8:
        doc_tram = "tám trăm"
    else:
        doc_tram = "chín trăm"

    if hang_chuc == 0:
        if hang_dv == 0:
            doc_chuc = ""
        else:
            doc_chuc = "lẻ"
    elif hang_chuc == 1:
        doc_chuc = "mười"
    elif hang_chuc == 2:
        doc_chuc = "hai mươi"
    elif hang_chuc == 3:
        doc_chuc = "ba mươi"
    elif hang_chuc == 4:
        doc_chuc = "bốn mươi"
    elif hang_chuc == 5:
        doc_chuc = "năm mươi"
    elif hang_chuc == 6:
        doc_chuc = "sáu mươi"
    elif hang_chuc == 7:
        doc_chuc = "bảy mươi"
    elif hang_chuc == 8:
        doc_chuc = "tám mươi"
    elif hang_chuc ==9:
        doc_chuc = "chín mươi"
   

    if hang_dv == 0:
        doc_dv = ""
    elif hang_dv == 1:
        doc_dv = "một"
    elif hang_dv == 2:
        doc_chuc = "hai"
    elif hang_dv == 3:
        doc_dv = "ba"
    elif hang_dv == 4:
        doc_dv = "bốn"
    elif hang_dv == 5:
        doc_dv = "năm"
    elif hang_dv == 6:
        doc_dv = "sáu"
    elif hang_dv == 7:
        doc_dv = "bảy"
    elif hang_dv == 8:
        doc_dv = "tám"
    elif hang_dv == 9:
        doc_dv = "chín"
    # kq
    print(f"{doc_tram} {doc_chuc} {doc_dv}")
else:
    print("số không hợp lệ! vui lòng nhập lại")
    