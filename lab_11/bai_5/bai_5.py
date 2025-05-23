def doc_du_lieu(sbd, hoten, phieudiem, ketqua):
    with open(file= sbd, mode= 'r') as f:
        data1 = f.readline()
    with open(file= hoten, mode= 'r') as r:
        data2 = r.readline()
    with open(file= phieudiem, mode= 'r') as q:
        data3 = q.readline()
    ket_qua = {'So bao danh': data1,
               'Ho va ten': data2,
               'Diem': data3}
    with open(file= ketqua, mode= 'w') as p:
        p.write(str(ket_qua))

doc_du_lieu('Sbd_Ph.dat', 'SBD_Ten.txt', 'Phieu_Diem.txt', 'Ketqua.txt')