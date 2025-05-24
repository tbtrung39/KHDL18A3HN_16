import csv
from libs.xu_ly_thong_tin_nhanvien import *

ds_nhanvien = []

def nhap_nhan_vien():
    while True:
        ma = input("Nhập mã NV: ")
        ten = input("Nhập tên NV: ")
        chuc_vu = input("Nhập chức vụ (TP, PP, NV): ")
        he_so = float(input("Nhập hệ số lương: "))
        
        luong = tinh_luong(he_so)
        phu_cap = tinh_phu_cap(chuc_vu)
        thuc_linh = luong + phu_cap

        ds_nhanvien.append({
            "MaNV": ma,
            "TenNV": ten,
            "ChucVu": chuc_vu,
            "HeSoLuong": he_so,
            "Luong": luong,
            "PhuCap": phu_cap,
            "ThucLinh": thuc_linh
        })

        tiep = input("Nhập thêm? (c/k): ")
        if tiep.lower() == 'k':
            break

def in_danh_sach():
    print(f"{'MaNV':<10}{'TenNV':<20}{'ChucVu':<10}{'HeSo':<6}{'Luong':<12}{'PhuCap':<10}{'ThucLinh':<12}")
    for nv in ds_nhanvien:
        print(f"{nv['MaNV']:<10}{nv['TenNV']:<20}{nv['ChucVu']:<10}{nv['HeSoLuong']:<6.2f}"
              f"{nv['Luong']:<12.0f}{nv['PhuCap']:<10.0f}{nv['ThucLinh']:<12.0f}")

def sap_xep_theo_thuc_linh():
    ds_nhanvien.sort(key=lambda x: x["ThucLinh"], reverse=True)

def luu_file():
    with open("files/ds_nhanvien.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["MaNV", "TenNV", "ChucVu", "HeSoLuong", "Luong", "PhuCap", "ThucLinh"])
        for nv in ds_nhanvien:
            writer.writerow([nv["MaNV"], nv["TenNV"], nv["ChucVu"], nv["HeSoLuong"],
                             nv["Luong"], nv["PhuCap"], nv["ThucLinh"]])

def menu():
    while True:
        print("\n===== QUẢN LÝ NHÂN VIÊN =====")
        print("1. Nhập danh sách nhân viên")
        print("2. Tính lương và in danh sách")
        print("3. Sắp xếp theo Thực lĩnh giảm dần và in")
        print("4. Lưu vào file CSV")
        print("0. Thoát")
        chon = input("Chọn chức năng: ")

        if chon == "1":
            nhap_nhan_vien()
        elif chon == "2":
            in_danh_sach()
        elif chon == "3":
            sap_xep_theo_thuc_linh()
            in_danh_sach()
        elif chon == "4":
            luu_file()
            print("Đã lưu file thành công.")
        elif chon == "0":
            break
        else:
            print("Chức năng không hợp lệ!")

if __name__ == "__main__":
    menu()
