# Nhập tháng và năm từ người dùng
thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))
# Tính toán và in kết quảquả
if thang in [1, 3, 5, 7, 8, 10, 12]:
 print('Tháng có 31 ngày.')
elif thang in [4, 6, 9, 11]:
 print('Tháng có 30 ngày.')
else:
 if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
      print('Tháng có 29 ngày.')
 else:
      print('Tháng có 28 ngày.')