def tong_so_le(filename):
    tong = 0
    with open(filename, 'r') as f:
        for line in f:
            for so in line.strip().split():
                if so.isdigit():
                    x = int(so)
                    if x % 2 == 1:
                        tong += x
    return tong

print("Tổng các số lẻ:", tong_so_le("dayso.dat"))


