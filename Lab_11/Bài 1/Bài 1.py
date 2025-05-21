
def tinh_tong_so_le():
    tong = 0
    with open("dayso.dat", 'r') as tep:
        for dong in tep:
            for so in dong.strip().split():
                if int(so) % 2 == 1:
                    tong += int(so)
    return tong

# Gọi hàm và in kết quả
print("Tổng các số lẻ là:", tinh_tong_so_le())