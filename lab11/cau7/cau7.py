with open('lab11/cau7/m_nums.txt', 'r') as tep_m:
    noi_dung_m = tep_m.read()
    tap_hop_m = set(map(int, noi_dung_m.strip().split()))
with open('lab11/cau7/n_nums.txt', 'r') as tep_n:
    noi_dung_n = tep_n.read()
    tap_hop_n = set(map(int, noi_dung_n.strip().split()))
so_chung = sorted(tap_hop_m.intersection(tap_hop_n))
with open('lab11/cau7/so_chung.txt', 'w') as tep_ket_qua:
    tep_ket_qua.write(' '.join(map(str, so_chung)))
print("Các số chung giữa hai file là:")
with open('lab11/cau7/so_chung.txt', 'r') as tep_kq:
    print(tep_kq.read())
