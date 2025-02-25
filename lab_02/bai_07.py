diem = float(input("nhập điểm:"))
if 0 <= diem <= 10:
    if 0.0 <= diem <= 3.0:
        print("loại kém")
    elif 3.0 <= diem <= 5.0:
        print("loại kém")
    elif 5.0 <= diem <= 7.0:
        print("loại trung bình")
    elif 7.0 <= diem <= 8.0:
        print("loại khá")
    elif 9.0 <= diem <= 10.0:
        print("loại giỏi")
else:
    print("điểm không hợp lệ! vui lòng nhập lại")
    

