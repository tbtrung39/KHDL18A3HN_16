def luong(n):
    if 1 <= n <= 10:
        return 1_000_000_000
    elif 10 <= n <= 100:
        return 1_000_000_000_000
    elif 100 <= n <= 1000:
        return 1_000_000_000_000_000

hoten = input("Nhap ho ten: ")
quequan = input("Nhap que quan: ")
tham_nien_cong_tac = int(input("Nhap tham nien cong tac: "))
tien_luong = luong(tham_nien_cong_tac)
print(f'            Ho ten: {hoten}')
print(f'          Que quan: {quequan}')
print(f'Tham nien cong tac: {tham_nien_cong_tac}')
print(f'             Luong: {tien_luong}')