thi_sinh_dict = {}

while True:
    so_bao_danh = input("\nNhập số báo danh: ").strip()
    
    if so_bao_danh in thi_sinh_dict:
        ho_ten, diem = thi_sinh_dict[so_bao_danh]
        print(f" Thí sinh đã có trong danh sách:")
        print(f"   Họ và tên: {ho_ten}")
        print(f"   Điểm thi: {diem}")
    else:
        ho_ten = input("Nhập họ và tên thí sinh: ").strip()
        
        try:
            diem = float(input("Nhập điểm thi thí sinh (0 - 10): "))
            if 0 <= diem <= 10:
                thi_sinh_dict[so_bao_danh] = (ho_ten, diem)
                print(f" Đã thêm: {ho_ten} - Điểm: {diem}")
            else:
                print(" Điểm thi không hợp lệ. Vui lòng nhập từ 0 đến 10.")
        except ValueError:
            print(" Điểm thi phải là một số.")

    tiep_tuc = input("Bạn có muốn nhập/tra cứu tiếp không? (y/n): ").lower()
    if tiep_tuc != 'y':
        break

print(" Danh sách thí sinh đã nhập:")
for sbd, (ho_ten, diem) in thi_sinh_dict.items():
    print(f"  SBD: {sbd} | Họ tên: {ho_ten} | Điểm: {diem}")
