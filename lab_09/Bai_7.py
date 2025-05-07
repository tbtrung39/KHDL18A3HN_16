def tong_chu_so(n):
    if n == 0:
        return 0
    else:
        return n % 10 + tong_chu_so(n // 10)
n = int(input("Nhap mot so nguyen duong: "))
ket_qua = tong_chu_so(n)
print("Tong cac chu so la:", ket_qua)