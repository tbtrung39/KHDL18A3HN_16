def ghep_diem():
    # Đọc file SBD và Số phách
    with open("sbd_Ph.dat", 'r') as f:
        sbd_phach = dict(map(int, line.strip().split()) for line in f)

    # Đọc file SBD và Họ tên
    with open("sbd_Ten.txt", 'r') as f:
        sbd_ten = {}
        for dong in f:
            ma, ten = dong.strip().split(maxsplit=1)
            sbd_ten[int(ma)] = ten

    # Đọc file Số phách và điểm
    with open("Phieu_diem.txt", 'r') as f:
        phach_diem = dict(map(int, line.strip().split()) for line in f)

    # Ghép kết quả
    ket_qua = []
    for sbd in sbd_phach:
        phach = sbd_phach[sbd]
        ten = sbd_ten.get(sbd, "Không rõ")
        diem = phach_diem.get(phach, -1)
        ket_qua.append((sbd, ten, diem))

    # Sắp xếp theo SBD tăng dần
    ket_qua.sort()

    # Ghi ra file kết quả
    with open("Ketqua.txt", 'w') as f:
        for sbd, ten, diem in ket_qua:
            f.write(f"{sbd} {ten} {diem}\n")

# Gọi hàm
ghep_diem()
print("Đã ghép xong điểm vào file Ketqua.txt.")
