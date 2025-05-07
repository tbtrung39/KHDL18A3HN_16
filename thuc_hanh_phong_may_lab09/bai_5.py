#Bài 5:
def tao_hoan_vi(mang):
    if len(mang) == 1:
        return [mang]
    danh_sach_hoan_vi = []
    for i in range(len(mang)):
        phan_tu = mang[i]
        phan_con_lai = mang[:i] + mang[i+1:]
        for hoan_vi in tao_hoan_vi(phan_con_lai):
            danh_sach_hoan_vi.append([phan_tu] + hoan_vi)
    return danh_sach_hoan_vi

so_n = int(input("Nhập số n: "))
danh_sach = list(range(1, so_n + 1))
ket_qua = tao_hoan_vi(danh_sach)

for hoan_vi in ket_qua:
    print(hoan_vi)