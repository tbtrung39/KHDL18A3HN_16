danh_sach = []
while True:
    du_lieu = input("Nhập (Tên, Tuổi, Điểm) hoặc 'N' để dừng: ").strip()
    if du_lieu.upper() == 'N': 
        break
    try:
        ten, tuoi, diem = du_lieu.split(",")
        tuoi = int(tuoi.strip())  
        diem = float(diem.strip())  
        danh_sach.append((ten.strip(), tuoi, diem))
    except ValueError:
        print(" Dữ liệu không hợp lệ, vui lòng nhập lại theo định dạng: Name, Age, Score")
danh_sach.sort(key=lambda x: (x[0], x[1], x[2]))
print("\nDanh sách sau khi sắp xếp:")
for item in danh_sach:
    print(item)
