class sinh_vien:
    def __init__(sv):
     '''
     Khởi tạo biến
     '''
     sv.ma_so_sinh_vien = ''
     sv.ho_ten = ''
     sv.que_quan = ''
     sv.nam_sinh = ''
     sv.diem_trung_binh_cac_nam_hoc = ''

    def input_info(sv):
     '''
     Nhập thông tin từ bàn phím
     '''
     sv.ma_so_sinh_vien = input('Nhập mã số sinh viên: ')
     sv.ho_ten = input('Nhập họ tên sinh viên: ')
     sv.que_quan = input('Nhập quê quán: ')
     sv.nam_sinh = input('Nhập năm sinh: ')
     sv.diem_trung_binh_cac_nam_hoc = input('Nhập điểm trung bình các năm học:')

    def output_info(sv):
     '''
     In thông tin ra màn hình
     '''
     print("\nThông tin sinh viên: ")
     print("Mã số sinh viên:", sv.ma_so_sinh_vien)
     print("Họ tên:", sv.ho_ten)
     print("Quê quán:", sv.que_quan)
     print("Năm sinh:", sv.nam_sinh)
     print("Điểm trung bình các năm:", sv.diem_trung_binh_cac_nam_hoc)
# Tạo sinh viên
sv = sinh_vien()
# Nhập thông tin sinh viên
sv.input_info()
# Xuất thông tin sinh viên 
sv.output_info()
