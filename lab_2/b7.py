# bài 7
diem = float(input("Nhập điểm tổng kết: "))
if 0 <= diem < 3.0:
    print("học lực kém")
elif diem ==4.0:
    print("học lực yếu")
elif 5.0 <= diem <= 6.0:
    print("học lực trung bình")
elif 7.0 <= diem <= 8.0:
    print("học lực khá")
elif 9.0 <= diem <= 10.0:
    print("học lực giỏi")