n = int(input("Nhập n từ bàn phím: "))
tong = 1 
tich = 1
for i in range(1,n+1):
    tich *= (2*i)/(2*i+1)
    tong += tich
print("Kết quả:",round(tong,3))