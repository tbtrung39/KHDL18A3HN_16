def liet_ke_cacnghiem(n, tong=0, ket_qua=[], truoc=1):
    if tong == n:
        print(ket_qua)
        return
    for i in range(truoc, n - tong + 1):
        liet_ke_cacnghiem(n, tong + i, ket_qua + [i], i)

# Nhập số nguyên n
n = int(input("Nhập số tự nhiên n: "))
print(f"Các phân tích của {n} là:")
liet_ke_cacnghiem(n)
