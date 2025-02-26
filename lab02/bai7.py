diem_tong_ket = float(input('Nhập điểm tổng kếtkết: '))
if 0.0 <= diem_tong_ket <= 3.0:
    print("Loại kém")
elif 3.0 < diem_tong_ket <= 5.0:
    print("Loại yếu")
elif 5.0 < diem_tong_ket <= 6.0:
    print("Loại trung bình")
elif 6.0 < diem_tong_ket <= 8.0:
    print("Loại khá")
elif 8.0 < diem_tong_ket <= 10.0:
    print("Loại giỏi")
else:
    print("Không hợp lệ. Vui lòng nhập lại")