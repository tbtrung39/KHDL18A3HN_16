def ghep_diem():
    with open("sbd_Ph.dat") as f:
        sbd_ph = dict(map(int, line.strip().split()) for line in f)

    with open("sbd_Ten.txt") as f:
        sbd_ten = {}
        for line in f:
            parts = line.strip().split(maxsplit=1)
            sbd_ten[int(parts[0])] = parts[1]

    with open("Phieu_diem.txt") as f:
        ph_diem = dict(map(int, line.strip().split()) for line in f)

    ketqua = []
    for sbd in sbd_ph:
        so_phach = sbd_ph[sbd]
        ho_ten = sbd_ten.get(sbd, "Unknown")
        diem = ph_diem.get(so_phach, -1)
        ketqua.append((sbd, ho_ten, diem))

    ketqua.sort()