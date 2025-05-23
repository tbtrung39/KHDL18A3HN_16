def tong_S1(n):
    if n == 1:
        return 1
    return n + tong_S1(n - 1)

def tong_S2(n):
    if n == 1:
        return 1
    return n * n + tong_S2(n - 1)

try:
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        raise ValueError("Lỗi: n phải là số nguyên dương.")
    s1 = tong_S1(n)
    s2 = tong_S2(n)
    print("S1 =", s1)
    print("S2 =", s2)
except ValueError as e:
    print("Lỗi nhập liệu:", e)
