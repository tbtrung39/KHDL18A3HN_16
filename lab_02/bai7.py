print("\n học lực của học sinh")
diem=float(input("nhập điểm TK của học sinh:"))
if diem<=3.0:
    print("loại kém")
elif diem>=4.0 and diem<=5.0:
    print("loại yếu")
elif diem>=5.0 and diem<=6.0:
    print("loại trung bình")
elif diem>=7.0 and diem<=8.0:
    print("loại khá")
elif diem>=9.0 and diem<=10.0:
    print("loại giỏi")
else:
    print("điểm không hợp lệ.Vui lòng nhập lại")
    