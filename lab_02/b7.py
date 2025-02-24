
print("Nhập điểm học lực của học sinh:")
hoc_luc = int(input("Nhập điểm: "))

if 0.0 <= hoc_luc <= 3.0:
    print("Học lực loại Kém")
elif hoc_luc == 4.0:
    print("Học lực loại Yếu")
elif 5.0 <= hoc_luc <= 6.0:
    print("Học lực loại Trung bình")
elif 7.0 <= hoc_luc <= 8.0:
    print("Học lực loại Khá")
elif 9.0 <= hoc_luc <= 10.0:
    print("Học lực loại Giỏi")
else:
    print("Không hợp lệ, xin vui lòng nhập lại.")
