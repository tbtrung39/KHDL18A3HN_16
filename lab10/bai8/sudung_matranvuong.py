import matranvuong

n=int(input("nhap kich thuoc ma tran vuong N x N: "))
matran=matranvuong.nhap_ma_tran(n)

matranvuong.in_ma_tran(matran)

print("ma tran chuyen vi: ")
matran_chuyen_vi=matranvuong.ma_tran_chuyen_vi(matran)
matranvuong.in_ma_tran(matran_chuyen_vi)

if matranvuong.la_ma_tran_doi_xung(matran):
    print("ma tran la ma tran doi xung")
else:
    print("ma tran khong phai la ma tran doi xung")