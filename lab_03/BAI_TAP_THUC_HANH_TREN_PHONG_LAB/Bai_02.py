# Nhập thông tin n (n là số nguyên dương)
n=int(input('Nhập số nguyên dương n: '))
# Tính toán và in
for i in range(1,n):
    tong_uoc=0
    for j in range(1,i):
        if i % j ==0:
            tong_uoc+=j
    if tong_uoc == i:
        print(i)