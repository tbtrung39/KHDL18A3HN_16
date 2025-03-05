# Nhập n từ người dùng
n = int(input('Nhập giá trị của n: '))
# Kiểm tra số nguyên tố
for i in range(n):
    kiem_tra =1
    if i < 2:
        kiem_tra=0
    elif i ==2:
        kiem_tra=1
    else:
        for j in range(2,i):
            if i % j == 0:
             kiem_tra = 0
             break
            else:
             kiem_tra=1
# In ra các số nguyên tố nhỏ hơn n
    if kiem_tra == 1:
        print(i, end=' ')