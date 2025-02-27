n = int(input("nhập số n:"))
print("các sô nguyên tố nhỏ hơn hoặc bằng n:")
for i in range(2,n+1):
    tong = 0
    for j in range(2,i):
        if i%j ==0:
            tong = 1
    if tong == 0:
        print(i, end=" ")
