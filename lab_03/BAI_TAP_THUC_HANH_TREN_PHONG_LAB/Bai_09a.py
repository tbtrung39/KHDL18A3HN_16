# Nhập vào n 
n = int(input('Nhập n: '))
# Điều kiện và tính toán
if n <= 0:
    print('Nhập n là số nguyên dương đi không thì code không chạy đâu')
else:
    tong = 0
    i = 1
    for i in range(1,n+1):
        tong += i**2
# In
print('Tổng của S4 là:',tong)