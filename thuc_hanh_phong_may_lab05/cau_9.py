#Bài 9:
#Cách 1
chuoi_nhap = input("Nhập chuỗi: ")
ky_tu_max = chuoi_nhap[0] if chuoi_nhap else ''
do_dai_max = 1
ky_tu_hien_tai = chuoi_nhap[0] if chuoi_nhap else ''
do_dai_hien_tai = 1
for vi_tri in range(1, len(chuoi_nhap)):
    if chuoi_nhap[vi_tri] == chuoi_nhap[vi_tri - 1]:
        do_dai_hien_tai += 1
        if do_dai_hien_tai > do_dai_max:
            do_dai_max = do_dai_hien_tai
            ky_tu_max = chuoi_nhap[vi_tri]
    else:
        do_dai_hien_tai = 1
print(ky_tu_max * do_dai_max)

#Cách 2:
chuoi_nhap = input("Nhập chuỗi: ")
chuoi_max, ky_tu_truoc, do_dai_hien_tai = '', '', 0
for ky_tu in chuoi_nhap:
    do_dai_hien_tai = do_dai_hien_tai + 1 if ky_tu == ky_tu_truoc else 1
    ky_tu_truoc = ky_tu
    if do_dai_hien_tai > len(chuoi_max):
        chuoi_max = ky_tu * do_dai_hien_tai
print(chuoi_max)