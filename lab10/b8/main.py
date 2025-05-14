import mtran_vuong
n= int(input("nhap n :"))
matran= mtran_vuong.nhap_mtran(n)
print("ma tran vua nhap",n)
mtran_vuong.in_ma_tran(matran)
print("\nma tran chuyen vi:")
matran_cv= mtran_vuong.chuyen_vi(matran)
mtran_vuong.in_ma_tran(matran_cv)
if mtran_vuong.ktra_doi_xung(matran):
    print("ma tran doi xung qua duong cheo chinh ")
else:
    print("ma tran khog doi xung ")