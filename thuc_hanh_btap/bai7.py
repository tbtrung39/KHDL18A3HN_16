print('\n\n\t\t=====PHÂN LOẠI HỌC SINH =====')
print("Nhập điểm của học sinh")
a = float(input("Nhập điểm: "))
if 0 < a <= 3:
    print("Học sinh kém")
elif 4 < a < 5:
    print("Học sinh yếu")
elif 5 <= a <= 6:
    print("Học sinh trung bình")
elif 7 <= a <= 8:
    print("Học sinh khá ")
elif 9 <= a < 10:
    print("Học sinh giỏi")
else:
    print("chấm trên thang điểm 10")

