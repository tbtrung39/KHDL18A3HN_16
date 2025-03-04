#câu10: viết chương trình nhập vào số nguyên dương rồi xuất ra dạng phân tích thừa số nguyên tố của số đó
def phan_tich_thua_so(n):
    if n <= 0:
        return "n phải là số nguyên dương!"
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

n = int(input("Nhập n: "))
print("Phân tích thừa số nguyên tố:", phan_tich_thua_so(n))