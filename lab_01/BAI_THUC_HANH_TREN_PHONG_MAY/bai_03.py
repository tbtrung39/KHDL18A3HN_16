# Nhập bán kính và chiều cao
ban_kinh = int(input('Nhập bán kính r: '))
chieu_cao = int(input('Nhập chièu cao h: '))
pi = 3.14
# Công thức tính diện tích xung quanh hình trụ là : Sxq=2*pi*r*h
Sxq=2*pi*ban_kinh*chieu_cao
# Công thức tính diện tích toàn phần hình trụ là : Stp=2*pi*r*(r+h)
Stp=2*pi*ban_kinh*(ban_kinh+chieu_cao)
# Công thức tính thể tích là : V=pi*(r**2)*h
V=pi*(ban_kinh**2)*chieu_cao
# In kết quả (làm tròn 2 chữ số thập phân)
print('Diện tích xung quaanh là: ',round(Sxq,2))
print('Diện tích toàn phần là: ',round(Stp,2))
print('Thể tích là:',round(V,2))

