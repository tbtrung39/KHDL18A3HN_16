diem = float(input("Nhập điểm:"))
if 0 <= diem <= 10:
    if 0.0 <= diem <= 3.0:
        print("Loại kém")
    elif 3.0 <= diem <= 5.0:
        print("Loại kém")
    elif 5.0 <= diem <= 7.0:
        print("Loại trung bình")
    elif 7.0 <= diem <= 8.0:
        print("Loại khá")
    elif 9.0 <= diem <= 10.0:
        print("Loại giỏi")
else:
    print("Diểm không hợp lệ!")
    
