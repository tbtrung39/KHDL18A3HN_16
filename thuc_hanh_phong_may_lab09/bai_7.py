#Bài 7:
def tim_nghiem(so_n, danh_sach=[], tong_hien_tai=0):
    if len(danh_sach) == so_n:
        if tong_hien_tai == so_n:
            print(danh_sach)
        return
    for i in range(so_n + 1):
        tim_nghiem(so_n, danh_sach + [i], tong_hien_tai + i)

so_n = int(input("Nhập số n: "))
tim_nghiem(so_n)