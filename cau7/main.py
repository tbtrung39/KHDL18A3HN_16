import day_so
n = int(input("Nhap so luong phan tu (≤100): "))
ds = day_so.sinh_day_so(n)
print("Day so vua sinh:", ds)
print("Cac so nguyen to chia het cho 7:", day_so.liet_ke_nt_chia_het_cho_7(ds))
print("Tong cac so le:", day_so.tinh_tong_so_le(ds))
print("Kiem tra co so chinh phuong:", day_so.co_chinh_phuong(ds))
