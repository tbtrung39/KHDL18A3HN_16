import csv

class SinhVien:
    def __init__(self, ma_sv, ho_ten, diem_tb, diem_rl):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.diem_tb = float(diem_tb)
        self.diem_rl = float(diem_rl)
        self.diem_tl = (self.diem_tb + self.diem_rl) / 2
    
    def __str__(self):
        return f"{self.ma_sv:10}\t{self.ho_ten:20}\t{self.diem_tb:5.1f}\t{self.diem_rl:5.1f}\t{self.diem_tl:5.1f}"

class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []
    
    def nhap_danh_sach(self):
        n = int(input("Nhập số lượng sinh viên: "))
        for i in range(n):
            print(f"\nNhập thông tin sinh viên thứ {i+1}:")
            ma_sv = input("Mã SV: ")
            ho_ten = input("Họ tên: ")
            diem_tb = float(input("Điểm TB: "))
            diem_rl = float(input("Điểm RL: "))
            sv = SinhVien(ma_sv, ho_ten, diem_tb, diem_rl)
            self.danh_sach.append(sv)
        self.tinh_diem_tl()
    
    def tinh_diem_tl(self):
        for sv in self.danh_sach:
            sv.diem_tl = (sv.diem_tb + sv.diem_rl) / 2
    
    def in_danh_sach(self):
        print("\nDANH SÁCH SINH VIÊN")
        print("="*80)
        print(f"{'Mã SV':10}\t{'Họ tên':20}\t{'Điểm TB':7}\t{'Điểm RL':7}\t{'Điểm TL':7}")
        for sv in self.danh_sach:
            print(sv)
        print("="*80)
    
    def luu_file_csv(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Mã SV', 'Họ tên', 'Điểm TB', 'Điểm RL', 'Điểm TL'])
            for sv in self.danh_sach:
                writer.writerow([sv.ma_sv, sv.ho_ten, sv.diem_tb, sv.diem_rl, sv.diem_tl])
        print(f"\nĐã lưu dữ liệu vào file {filename}")
    
    def sap_xep_theo_diem_rl(self):
        self.danh_sach.sort(key=lambda x: x.diem_rl)
    
    def tim_sv_diem_tl_cao_nhat(self):
        if not self.danh_sach:
            return None
        max_tl = max(self.danh_sach, key=lambda x: x.diem_tl)
        return max_tl
    
    def menu(self):
        while True:
            print("\nQUẢN LÝ SINH VIÊN")
            print("1. Nhập danh sách sinh viên")
            print("2. Hiển thị danh sách")
            print("3. Lưu vào file CSV")
            print("4. Sắp xếp theo điểm rèn luyện")
            print("5. Tìm SV có điểm TL cao nhất")
            print("0. Thoát")
            
            choice = input("Chọn chức năng: ")
            
            if choice == '1':
                self.nhap_danh_sach()
            elif choice == '2':
                self.in_danh_sach()
            elif choice == '3':
                self.luu_file_csv('files/ds_sinhvien.csv')
            elif choice == '4':
                self.sap_xep_theo_diem_rl()
                print("Đã sắp xếp theo điểm rèn luyện tăng dần")
                self.in_danh_sach()
            elif choice == '5':
                sv = self.tim_sv_diem_tl_cao_nhat()
                if sv:
                    print("\nSinh viên có điểm TL cao nhất:")
                    print(f"{'Mã SV':10}\t{'Họ tên':20}\t{'Điểm TB':7}\t{'Điểm RL':7}\t{'Điểm TL':7}")
                    print(sv)
                else:
                    print("Danh sách sinh viên trống")
            elif choice == '0':
                break
            else:
                print("Lựa chọn không hợp lệ")