nhap_diem_thi = float(input("Nhập điểm thi: "))
if 0 <= nhap_diem_thi <= 3:
    print("Kém")
elif nhap_diem_thi <= 4:
    print("Yếu")
elif 5 <= nhap_diem_thi <= 6:
    print("Trung bình")
elif 7 <= nhap_diem_thi <= 8:
    print("Khá")
elif 9 <= nhap_diem_thi <= 10:
    print("Giỏi")
else:
    print("Nhập lại")