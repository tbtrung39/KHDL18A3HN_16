def ghep_phach():
    sbd_phach = {}
    with open("Sbd_Ph.dat", 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                sbd, phach = map(int, parts[:2])
                sbd_phach[phach] = sbd

    sbd_ten = {}
    with open("SBD_Ten.txt", 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                sbd = int(parts[0])
                hoten = ' '.join(parts[1:])
                sbd_ten[sbd] = hoten

    ds_thi = []
    with open("Phieu_Diem.txt", 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                phach, diem = map(int, parts[:2])
                sbd = sbd_phach.get(phach)
                hoten = sbd_ten.get(sbd, "Unknown")
                if sbd is not None:
                    ds_thi.append((sbd, hoten, diem))

    ds_thi.sort(key=lambda x: -x[2])

    with open("Ketqua.txt", 'w') as f:
        for sbd, hoten, diem in ds_thi:
            f.write(f"{sbd} {hoten} {diem}\n")

ghep_phach()