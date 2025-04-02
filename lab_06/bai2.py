so_phan_tu=int(input("Nhap so phan tu cua danh sach: "))
ds=list(map(int,input("Nhap danh sach so: ").split()))

if so_phan_tu<2:
    print("Khong co phan tu lon thu hai")
else:
    lon_nhat=ds[0]
    lon_nhi=ds[0]
    vi_tri_lon_nhat=0
    vi_tri_lon_nhi=-1
    for i in range(1,so_phan_tu):
        if ds[i]>lon_nhat:
            lon_nhi=lon_nhat
            vi_tri_lon_nhi=vi_tri_lon_nhat
            lon_nhat=ds[i]
            vi_tri_lon_nhat=i
        elif ds[i]>lon_nhi and ds[i]!=lon_nhat:
            lon_nhi=ds[i]
            vi_tri_lon_nhi=i
    if lon_nhi==lon_nhat:
        print("Khong co phan tu lon thu hai")
    else:
        print(f"Phan tu lon thu hai: {lon_nhi}, vi tri:{vi_tri_lon_nhi}")

dem_max=0
dem_hien_tai=0
for so in ds:
    if so>0:
        dem_hien_tai+=1
        if dem_hien_tai>dem_max:
            dem_max=dem_hien_tai
    else:
        dem_hien_tai=0
print(f"So luong so duong lien tep nhieu nhat la:{dem_max}")

tong_max=ds[0] if ds else 0
tong_hien_tai=0
so_phan_tu_max=0
so_phan_tu_hien_tai=0
for so in ds:
    if so>0:
        tong_hien_tai+=so
        so_phan_tu_hien_tai+=1
        if tong_hien_tai>tong_max:
            tong_max=tong_hien_tai
            so_phan_tu_max=so_phan_tu_hien_tai
    else:
        tong_hien_tai=0
        so_phan_tu_hien_tai=0
print(f"So luong so duong lien tiep cos tong lon nhat la:{so_phan_tu_max}")