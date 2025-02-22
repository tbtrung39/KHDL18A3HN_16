# Nhập tọa độ của vecto A,B
Ax,Ay,Az = map(float,input('Xin mời nhập tọa độ vecto A: ').split())
Bx,By,Bz = map(float,input('Xin mời nhập tọa độ vecto B: ').split())
# Tổng 2 vecto
tong_vecto = (Ax+Bx,Ay+By,Az+Bz)
# Tích vô hướng hai vecto
tich_vo_huong = Ax*Bx+Ay*By+Az*Bz
# Kết quả
print('Tổng của 2 vecto: ',tong_vecto)
print('Tích vô hướng: ',tich_vo_huong)

