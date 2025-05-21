from My_QuanLySinhvien import quanlysinhvien as qlsv

def main():
    ds = qlsv.nhap_danh_sach()
    print("\nDanh sách sinh viên:")
    qlsv.in_bang(ds)
    qlsv.ghi_file_csv(ds, "lab11/cau10/files/ds_sinhvien.csv")
    print("\nDanh sách sau khi sắp xếp theo điểm RL:")
    ds_sap_xep = qlsv.sap_xep_theo_rl(ds)
    qlsv.in_bang(ds_sap_xep)
    sv_max = qlsv.tim_sv_diem_tl_cao_nhat(ds)
    print("\nSinh viên có điểm TL cao nhất:")
    print("{:<10} {:<25} {:<10.2f} {:<10.2f} {:<10.2f}".format(
        sv_max.ma, sv_max.ten, sv_max.diem_tb, sv_max.diem_rl, sv_max.diem_tl))

if __name__ == "__main__":
    main()
