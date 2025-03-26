#cách 1
n = int(input("Nhập số tự nhiên n: "))
so_nhi_phan=""
while n>0:
    so_nhi_phan = str(n%2)+so_nhi_phan
    n //=2
print("Chuỗi nhị phân =",so_nhi_phan)
#cách 2 
n = int(input("Nhập số nguyên n: "))
binary_str = bin(n)[2:]
print(f"So nhị phân tương ứng: {binary_str}")