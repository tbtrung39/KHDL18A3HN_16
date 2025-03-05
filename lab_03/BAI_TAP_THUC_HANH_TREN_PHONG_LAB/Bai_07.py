# Nhập n từ người dùng
n = int(input('Nhập số nguyên dương n: '))
# Tính
tong = 0
for i in range(1,n+1):
    tong+=1/i
# In
print('Tổng nghịch đảo của',n,'số nguyên đầu tiên là:',tong)