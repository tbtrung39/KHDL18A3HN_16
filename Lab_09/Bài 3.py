def binh_phuong(n):
    if n == 1:
        return 2
    else:
        return 2 ** n + binh_phuong(n - 1)

n = int(input("Nhập số n: "))
kqua = binh_phuong(n)
print("Tổng lũy thừa của 2 là:", kqua)