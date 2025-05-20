def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_cac_nguyen_to_khac_nhau():
    tap_nguyen_to = set()
    
    # Đọc file đầu vào
    with open("f_in.dat", 'r') as tep_vao:
        for dong in tep_vao:
            for so in map(int, dong.strip().split()):
                if la_nguyen_to(so):
                    tap_nguyen_to.add(so)

    # Ghi kết quả ra file
    with open("f_out.dat", 'w') as tep_ra:
        danh_sach_nt = sorted(tap_nguyen_to)
        tep_ra.write(str(len(danh_sach_nt)) + '\n')
        tep_ra.write(' '.join(map(str, danh_sach_nt)))

# Gọi hàm
tim_cac_nguyen_to_khac_nhau()
print("Đã ghi các số nguyên tố khác nhau vào file f_out.dat.")
