def ghep_diem():
    # Đọc file SBD và Số phách
    with open("sbd_Ph.dat") as f:
        sbd_ph = dict(map(int, line.strip().split()) for line in f)

    # Đọc file SBD và Tên
    with open("sbd_Ten.txt") as f:
        sbd_ten = {}
        for line in f:
            parts = line.strip().split(maxsplit=1)
            sbd_ten[int(parts[0])] = parts[1]

    # Đọc file Số phách và Điểm
    with open("Phieu_diem.txt") as f:
        ph_diem = dict(map(int, line.strip().split()) for line in f)

    # Ghép thông tin
    ketqua = []
    for sbd in sbd_ph:
        so_phach = sbd_ph[sbd]
        ho_ten = sbd_ten.get(sbd, "Unknown")
        diem = ph_diem.get(so_phach, -1)
        ketqua.append((sbd, ho_ten, diem))

    # Sắp xếp theo SBD
    ketqua.sort()

    with open("Ketqua.txt", "w") as f:
        for sbd, ten, diem in ketqua:
            f.write(f"{sbd} {ten} {diem}\n")

# Gọi hàm
ghep_diem()
