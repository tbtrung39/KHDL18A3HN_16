import mtran_vuog
n= int(input("nhap n :"))
matran= mtran_vuog.nhap_mtran(n)
print("ma tran vua nhap",n)
mtran_vuog.in_ma_tran(matran)
print("\nma tran chuyen vi:")
matran_cv= mtran_vuog.chuyen_vi(matran)
mtran_vuog.in_ma_tran(matran_cv)
if mtran_vuog.ktra_doi_xung(matran):
    print("ma tran doi xung qua duong cheo chinh ")
else:
    print("ma tran khog doi xung ")
