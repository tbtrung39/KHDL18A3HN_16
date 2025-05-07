def X(n):
    return 1  
def tinh_tong(n):
    total = 0
    for i in range(n):
        total += (n - i ** 2) * X(n)  
    return total
n = int(input("Nhập số n: "))
print("Giá trị tổng là:", tinh_tong(n))