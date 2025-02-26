so = int(input("Nhập vào một số nguyên có 3 chữ số: "))

hang_tram = so // 100
hang_chuc = (so % 100) // 10
hang_don_vi = so % 10

ten_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

# Đọc hàng trăm
ket_qua = ten_so[hang_tram] + " trăm "

# Đọc hàng chục và đơn vị
if hang_chuc == 0:
    if hang_don_vi != 0:
        ket_qua += "lẻ " + ten_so[hang_don_vi]
elif hang_chuc == 1:
    ket_qua += "mười "
    if hang_don_vi == 5:
        ket_qua += "lăm"
    elif hang_don_vi != 0:
        ket_qua += ten_so[hang_don_vi]
else:
    ket_qua += ten_so[hang_chuc] + " mươi "
    if hang_don_vi == 1:
        ket_qua += "mốt"
    elif hang_don_vi == 5:
        ket_qua += "lăm"
    elif hang_don_vi != 0:
        ket_qua += ten_so[hang_don_vi]

print("Cách đọc: ", ket_qua)