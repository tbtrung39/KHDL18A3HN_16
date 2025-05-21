import csv

class SinhVien:
    def __init__(self, ma, ten, diem_tb, diem_rl):
        self.ma = ma
        self.ten = ten
        self.diem_tb = diem_tb
        self.diem_rl = diem_rl
        self.diem_tl = (diem_tb + diem_rl) / 2

    def to_list(self):
        return [self.ma, self.ten, self.diem_tb, self.diem_rl, self.diem_tl]

def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số lượng sinh viên: "))
    for _ in range(n):
        ma = input("Nhập mã SV: ")
        ten = input("Nhập họ tên: ")
        diem_tb = float(input("Nhập điểm TB: "))
        diem_rl = float(input("Nhập điểm RL: "))
        sv = SinhVien(ma, ten, diem_tb, diem_rl)
        ds.append(sv)
    return ds

def in_bang(ds):
    print("{:<10} {:<25} {:<10} {:<10} {:<10}".format("Mã SV", "Họ tên", "Điểm TB", "Điểm RL", "Điểm TL"))
    for sv in ds:
        print("{:<10} {:<25} {:<10.2f} {:<10.2f} {:<10.2f}".format(sv.ma, sv.ten, sv.diem_tb, sv.diem_rl, sv.diem_tl))
import os 

def ghi_file_csv(ds, ten_file):
    thu_muc = os.path.dirname(ten_file)
    if thu_muc and not os.path.exists(thu_muc):
        os.makedirs(thu_muc)

    with open(ten_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Mã SV: ", "Họ tên: ", "Điểm TB: ", "Điểm RL: ", "Điểm TL: "])
        for sv in ds:
            writer.writerow(sv.to_list())
def sap_xep_theo_rl(ds):
    return sorted(ds, key=lambda sv: sv.diem_rl)

def tim_sv_diem_tl_cao_nhat(ds):
    return max(ds, key=lambda sv: sv.diem_tl)
