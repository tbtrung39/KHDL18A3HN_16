#Bài 4:
def tao_hoan_vi(mang, trai, phai):
    if trai == phai:
        print(mang)
    else:
        for i in range(trai, phai + 1):
            mang[trai], mang[i] = mang[i], mang[trai]
            tao_hoan_vi(mang, trai + 1, phai)
            mang[trai], mang[i] = mang[i], mang[trai]

so_n = int(input("Nhập số n: "))
danh_sach = list(range(1, so_n + 1))
tao_hoan_vi(danh_sach, 0, so_n - 1)