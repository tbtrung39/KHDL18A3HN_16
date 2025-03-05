bang_ma_hoa = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 
    'G': 17, 'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 23, 
    'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29, 
    'S': 30, 'T': 31, 'U': 32, 'V': 33, 'W': 34, 'X': 35, 
    'Y': 36, 'Z': 37
}

so_container = input("Nhập số container: ")
tong_trong_so = 0
luy_thua = 1
for ky_tu in so_container[:-1]:
    if ky_tu in bang_ma_hoa:
        gia_tri = bang_ma_hoa[ky_tu]
    else:
        gia_tri = int(ky_tu)
    tong_trong_so = tong_trong_so + gia_tri * luy_thua
    luy_thua = luy_thua * 2
so_kiem_tra = tong_trong_so % 11
if so_kiem_tra == 10:
    so_kiem_tra = 0
if int(so_container[-1]) == so_kiem_tra:
    print("Số container hợp lệ")
else:
    print("Số container không hợp lệ")