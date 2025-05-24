def doi_nhi_phan(n):
    if n == 0:
        return ""
    else:
        return doi_nhi_phan(n // 2) + str(n % 2)
n = int(input("Nhap mot so nguyen duong: "))
if n == 0:
    print("So nhi phan la: 0")
else:
    ket_qua = doi_nhi_phan(n)
    print("So nhi phan la:", ket_qua)