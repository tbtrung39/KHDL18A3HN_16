#Bài 12:
#Cash 1
chuoi_nhap = input("Nhập chuỗi: ")
danh_sach_tu = chuoi_nhap.replace(',', ' ').split()
for tu in danh_sach_tu:
    print(tu)

#Cách 2
chuoi_nhap = input("Nhập chuỗi: ")
tu_hien_tai = ''
for ky_tu in chuoi_nhap:
    if ky_tu != ' ' and ky_tu != ',':
        tu_hien_tai += ky_tu
    else:
        if tu_hien_tai != "":
            print(tu_hien_tai)
            tu_hien_tai = ""
if tu_hien_tai != "":
    print(tu_hien_tai)