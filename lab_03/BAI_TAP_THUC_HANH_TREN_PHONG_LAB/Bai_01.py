# Nhập n từ người dùng
n = int(input('Nhập giá trị của n: '))
# Tính toán
tong = 1
tich = 1
for k in range(1,n+1):
    tu_so=2*(k+1)
    mau_so=2*k+3
    tich *= tu_so/mau_so
    tong += tich
    round(tong,3)
# In kết quả
print('Kết quả của phép toán sau là: ',tong)