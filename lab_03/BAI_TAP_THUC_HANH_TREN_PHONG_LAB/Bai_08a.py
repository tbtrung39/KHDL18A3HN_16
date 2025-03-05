# Nhập vào n 
n = int(input('Nhập n: '))
# Điều kiện và tính toán
if n <= 0:
    print('Nhập n là số nguyên dương đi không thì code không chạy đâu')
else:
    tong=0
    for i in range (1,n+1):
        tong = (i*(i+1))/2
# In
print('Tổng của S1 là:',tong)