# Nhập vào n 
n = int(input('Nhập n: '))
# Điều kiện và tính toán
if n <= 0:
    print('Nhập n là số nguyên dương đi không thì code không chạy đâu')
else:
    tong=0
    i = 2
    for i in range(2,2*i):
     tong = n*(n+1)
# In
print('Tổng của S3 là:',tong)