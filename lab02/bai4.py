n=int(input('Nhập số nguyênnguyên: '))
if n>=100:
    n=(n//100)%10
else:
    n=0
print(f"Chữ số hàng trăm của {n} là: {n}")