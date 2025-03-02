chu_so = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
n = int(input("Nhập vào một số nguyên có ba chữ số: "))
if 100 <= abs(n) <= 999:
    print("Số không hợp lệ! Vui lòng nhập số có đúng ba chữ số.")
so_am = n < 0
n = abs(n)  # Lấy giá trị tuyệt đối để dễ xử lý
hang_tram = n // 100
hang_chuc = (n // 10) % 10
hang_dv = n % 10
doc_so = "Âm " if so_am else ""  # Nếu là số âm, thêm "Âm"
doc_so += chu_so[hang_tram] + " trăm"
if hang_chuc == 0 and hang_dv != 0:
    doc_so += " lẻ " + chu_so[hang_dv]
elif hang_chuc == 1:
    doc_so += " mười " + (chu_so[hang_dv] if hang_dv != 0 else "")
else:
    if hang_chuc != 0:
        doc_so += " " + chu_so[hang_chuc] + " mươi"
    if hang_dv != 0:
        if hang_dv == 1 and hang_chuc > 1:
            doc_so += " mốt"
        elif hang_dv == 5 and hang_chuc > 0:
            doc_so += " lăm"
        else:
            doc_so += " " + chu_so[hang_dv]
print("Cách đọc:", doc_so)
