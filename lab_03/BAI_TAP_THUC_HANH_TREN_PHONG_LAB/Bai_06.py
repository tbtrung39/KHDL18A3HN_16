# Nhập n từ người dùng
n = int(input('Nhập số nguyên dương n: '))
# Tính toán và in kết quả
tong = 0
for i in range (1,n+1):
    tong+=i**3
print(f'Tổng bậc 3 của {n} số nguyên dương đầu tiên là: {tong}')