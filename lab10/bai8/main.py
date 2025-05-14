import Matranvuong

n = 3
ma_tran = Matranvuong.nhap_ma_tran(n)
print("Ma trận:")
Matranvuong.in_ma_tran(ma_tran)

print("Ma trận chuyển vị:")
Matranvuong.in_ma_tran(Matranvuong.ma_tran_chuyen_vi(ma_tran))

if Matranvuong.kiem_tra_doi_xung(ma_tran):
    print("Ma trận đối xứng.")
else:
    print("Ma trận không đối xứng.")
