from libs.xu_ly_thong_tin_nhanvien import *
import os

def tao_thu_muc(duong_dan):
    if not os.path.exists(duong_dan):
        os.makedirs(duong_dan)

def nhap_nhan_vien():
    ds = []
    while True:
        print("\nNhập thông tin nhân viên (bỏ trống mã NV để kết thúc):")
        ma_nv = input("Mã NV: ").strip()
        if not ma_nv:
            break
        ten_nv = input("Tên NV: ").strip()
        chuc_vu = input("Chức vụ (TP/PP/NV): ").strip().upper()
        try:
            he_so = float(input("Hệ số lương: "))
        except ValueError:
            print("Hệ số lương không hợp lệ! Nhập lại.")
            continue

        nv = {
            'Mã NV': ma_nv,
            'Tên NV': ten_nv,
            'Chức vụ': chuc_vu,
            'Hệ số lương': he_so,
            'Lương': 0,
            'Phụ cấp chức vụ': 0,
            'Thực lĩnh': 0
        }
        ds.append(nv)
    return ds

def in_danh_sach(ds):
    if not ds:
        print("Danh sách rỗng.")
        return
    print("\n{:<10} {:<20} {:<10} {:<10} {:<15} {:<15} {:<15}".format(
        "Mã NV", "Tên NV", "Chức vụ", "Hệ số", "Lương", "Phụ cấp", "Thực lĩnh"
    ))
    print("-" * 95)
    for nv in ds:
        print("{:<10} {:<20} {:<10} {:<10.2f} {:<15,.0f} {:<15,.0f} {:<15,.0f}".format(
            nv['Mã NV'], nv['Tên NV'], nv['Chức vụ'], nv['Hệ số lương'],
            nv['Lương'], nv['Phụ cấp chức vụ'], nv['Thực lĩnh']
        ))

def main():
    danh_sach = []

    while True:
        print("\n--- MENU QUẢN LÝ NHÂN VIÊN ---")
        print("1. Nhập danh sách")
        print("2. Tính toán lương, phụ cấp, thực lĩnh")
        print("3. Hiển thị danh sách")
        print("4. Sắp xếp theo Thực lĩnh giảm dần")
        print("5. Lưu vào file CSV")
        print("0. Thoát")

        chon = input("Chọn: ")

        if chon == "1":
            danh_sach = nhap_nhan_vien()
        elif chon == "2":
            if danh_sach:
                tinh_toan_cho_danh_sach(danh_sach)
                print("Đã tính xong.")
            else:
                print("Danh sách trống.")
        elif chon == "3":
            in_danh_sach(danh_sach)
        elif chon == "4":
            if danh_sach:
                danh_sach = sap_xep_theo_thuc_linh(danh_sach)
                print("Đã sắp xếp.")
            else:
                print("Danh sách trống.")
        elif chon == "5":
            if danh_sach:
                tao_thu_muc("files")
                luu_vao_file(danh_sach, "files/ds_nhanvien.csv")
                print("Đã lưu vào files/ds_nhanvien.csv")
            else:
                print("Không có dữ liệu để lưu.")
        elif chon == "0":
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
