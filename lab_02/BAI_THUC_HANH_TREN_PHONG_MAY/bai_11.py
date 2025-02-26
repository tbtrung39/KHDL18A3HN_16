# Nhập ngày và tháng từ người dùng
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
# Tính toán
so_ngay_trong_thang=0
if 28<=so_ngay_trong_thang<=31:
 if (1 <= thang <= 12 and 1 <= ngay <= so_ngay_trong_thang):
  ngay_tiep=0
  thang_tiep=0
  if ngay < so_ngay_trong_thang:
    ngay_tiep=ngay+1,thang_tiep=thang
  else:
    if thang == 2 and ngay ==28:
      ngay_tiep=1,thang_tiep=thang+1
    if thang == 1 or 3 or 5 or 7 or 8 or 10 or 12 and ngay ==31:
       ngay_tiep=1,thang_tiep=thang+1
    if thang == 4 or 6 or 9 or 11 and ngay == 30:
       ngay_tiep=1,thang_tiep=thang+1      
# In
print('Ngày tiếp theo của ngày',ngay,'tháng',thang,'là ngày',ngay_tiep,'tháng',thang_tiep)


