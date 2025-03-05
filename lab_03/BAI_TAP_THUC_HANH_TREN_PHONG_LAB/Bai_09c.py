# Nhập vào n 
n = int(input('Nhập n: '))
# Điều kiện và tính toán
if n <= 0:
    print('Nhập n là số nguyên dương đi không thì code không chạy đâu')
else:
    tong=0
    i = 1
    for i in range(2,2*n):
        tong += (2*i)**4
# In
print('Tổng của S6 là:',tong)