# Nhập ngày,giờ,phút,giây
d = float(input('Nhập ngày: '))
h = float(input('Nhập giờ: '))
m = float(input('Nhập phút: '))
s = float(input('Nhập giây: '))
# Đổi ngày giờ phút giây sang giây
S1 = d*24*60*60
S2 = h*60*60
S3 = m*60
S4 = s
# Tổng số giây
S5 = S1+S2+S3+S4
# In ra màn hình 
print('Tổng số giây là: ',S5)