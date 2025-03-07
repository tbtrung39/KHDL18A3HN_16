n = int(input("Nhập một số nguyên: "))
total = 0
while n:
    total += n%10
    n //= 10
print("Tổng các chữ số là:", total)
