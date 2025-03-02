diem_tk = float(input("Nhập điểm trung bình (0.0 - 10.0): "))
if 0.0 <= diem_tk <= 10.0:
    print("Điểm không hợp lệ! Vui lòng nhập lại trong khoảng 0.0 - 10.0.")
if diem_tk <= 3.0:
    hoc_luc = "Kém"
elif diem_tk == 4.0:
    hoc_luc = "Yếu"
elif 5.0 <= diem_tk <= 6.0:
    hoc_luc = "Trung bình"
elif 7.0 <= diem_tk <= 8.0:
    hoc_luc = "Khá"
else:
    hoc_luc = "Giỏi"
print(f"Học lực của học sinh là: {hoc_luc}")
