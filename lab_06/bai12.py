so_du=0
while True:
    nhap=input("Nhap giao dich (D/W so tien) hoac bam Enter de ket thuc: ").strip()
    if not nhap:
        break
    phan_tu=nhap.split()
    if len(phan_tu)!=2:
        print("Du lieu khong hop le, vui long nhap lai!")
        continue
    loai_giao_dich, so_tien = phan_tu[0], phan_tu[1]
    if not so_tien.isdigit():
        print("So tien khong hop le")
        continue
    so_tien=int(so_tien)
    if loai_giao_dich=="D":
        so_du+=so_tien
    elif loai_giao_dich=="W":
        so_du-=so_tien
    else:
        print("Khong hop le, vui long nhap lai!")
print("So du cuoi cung la:",so_du)
