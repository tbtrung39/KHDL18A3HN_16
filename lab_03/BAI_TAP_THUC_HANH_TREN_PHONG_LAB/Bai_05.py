# Nhập chiều dài và chiều rộng từ người dùng
chieu_dai = int(input('Nhập chiều dài: '))
chieu_rong = int(input('Nhập chiều rộng: '))
# Tính toán và in
for i in range(chieu_dai):
    for j in range(chieu_rong):
        print('*',end='')
    print()
