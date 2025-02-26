
n = int(input("Nhập một số nguyên có ba chữ số: "))

if 100 <= n <= 999:
    tram = n // 100
    chuc = (n % 100) // 10
    dv = n % 10

   
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

    # Xử lý phần chục
    if chuc == 1:
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
    else:
        chuc_str = ""

    if dv == 1 and chuc != 1:
        dv_str = "một"
    elif dv == 2:
        dv_str = "hai"
    elif dv == 3:
        dv_str = "ba"
    elif dv == 4:
        dv_str = "bốn"
    elif dv == 5:
        dv_str = "năm"
    elif dv == 6:
        dv_str = "sáu"
    elif dv == 7:
        dv_str = "bảy"
    elif dv == 8:
        dv_str = "tám"
    elif dv == 9:
        dv_str = "chín"
    else:
        dv_str = ""

    if chuc == 1 and dv == 0:
        print(f"Cách đọc số {n} là: {tram_str} mười")
    elif chuc == 0 and dv == 0:
        print(f"Cách đọc số {n} là: {tram_str}")
    elif chuc == 0:
        print(f"Cách đọc số {n} là: {tram_str} lẻ {dv_str}")
    elif chuc == 1:
        if dv == 0:
            print(f"Cách đọc số {n} là: {tram_str} mười")
        else:
            print(f"Cách đọc số {n} là: {tram_str} mười {dv_str}")
    else:
        if dv == 0:
            print(f"Cách đọc số {n} là: {tram_str} {chuc_str}")
        else:
            print(f"Cách đọc số {n} là: {tram_str} {chuc_str} {dv_str}")
else:
    print("Số nhập vào không phải là số nguyên có ba chữ số!")
