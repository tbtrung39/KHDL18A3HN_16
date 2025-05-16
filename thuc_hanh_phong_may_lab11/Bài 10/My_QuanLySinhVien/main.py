from quanlysinhvien import *

def nhap_sinh_vien():
    ds = []
    while True:
        ma = input("Mã SV (Enter để kết thúc): ").strip()
        if ma == "":
            break
        ten = input("Họ tên: ").strip()
        try:
            tb = float(input("Điểm TB: "))
            rl = float(input("Điểm RL: "))
        except ValueError:
            print("Điểm không hợp lệ.")
            continue
        ds.append({"Mã SV": ma, "Họ tên": ten, "TB": tb, "RL": rl})
    return ds

def in_danh_sach(ds):
    print("{:<10} {:<20} {:<5} {:<5} {:<5}".format("Mã SV", "Họ tên", "TB", "RL", "TL"))
    for sv in ds:
        print("{:<10} {:<20} {:<5.1f} {:<5.1f} {:<5.1f}".format(
            sv["Mã SV"], sv["Họ tên"], sv["TB"], sv["RL"], sv["TL"]
        ))

def main():
    ds = nhap_sinh_vien()
    tinh_diem_tich_luy(ds)
    print("\n--- Danh sách sinh viên ---")
    in_danh_sach(ds)

    ds_sorted = sap_xep_theo_rl(ds)
    print("\n--- Danh sách sau sắp xếp theo RL ---")
    in_danh_sach(ds_sorted)

    sv_max = tim_sinh_vien_max_tl(ds)
    print("\n--- Sinh viên có TL cao nhất ---")
    print(f"{sv_max['Mã SV']} - {sv_max['Họ tên']} - TL: {sv_max['TL']}")

    luu_file(ds, "My_QuanLySinhVien/ds_sinhvien.csv")
    print("\nĐã lưu vào file ds_sinhvien.csv")

if __name__ == "__main__":
    main()
