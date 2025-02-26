def xep_loai_hoc_luc(diem_tk):
    if 0.0 <= diem_tk <= 3.0:
        return "Loại Kém"
    elif diem_tk == 4.0:
        return "Loại Yếu"
    elif 5.0 <= diem_tk <= 6.0:
        return "Loại Trung bình"
    elif 7.0 <= diem_tk <= 8.0:
        return "Loại Khá"
    elif 9.0 <= diem_tk <= 10.0:
        return "Loại Giỏi"
    else:
        return "Điểm không hợp lệ"
# Nhập điểm từ người dùng
try:
    diem_tk = float(input("Nhập điểm trung bình: "))
    print("Học lực:", xep_loai_hoc_luc(diem_tk))
except ValueError:
    print("Vui lòng nhập một số hợp lệ!")