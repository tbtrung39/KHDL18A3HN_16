sbd_phach = {}
with open('lab11/cau5/Sbd_Ph.dat', 'r') as f:
    for dong in f:
        sbd, phach = map(int, dong.strip().split())
        sbd_phach[phach] = sbd
sbd_ten = {}
with open('lab11/cau5/Sbd_Ten.txt', 'r') as f:
    for dong in f:
        tach = dong.strip().split(maxsplit=1)
        sbd = int(tach[0])
        ten = tach[1]
        sbd_ten[sbd] = ten
danh_sach = []
with open('lab11/cau5/Phieu_Diem.txt', 'r') as f:
    for dong in f:
        phach, diem = map(int, dong.strip().split())
        sbd = sbd_phach.get(phach)
        ten = sbd_ten.get(sbd)
        if sbd and ten:
            danh_sach.append((sbd, ten, diem))
danh_sach.sort(key=lambda x: -x[2])
with open('lab11/cau5/Ketqua.txt', 'w') as f:
    for sbd, ten, diem in danh_sach:
        f.write(f"{sbd} {ten} {diem}\n")
