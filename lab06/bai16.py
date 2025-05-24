danh_sach = []
print("Nhập danh sách tên, tuổi, điểm:")
while True:
    du_lieu = input("Nhập tên, tuổi, điểm: ") 
    if du_lieu.lower() == "q":
        break
    phan_tu = du_lieu.split(",")
    if (len(phan_tu) == 3 and 
        phan_tu[1].strip().isdigit() and 
        phan_tu[2].strip().isdigit()):
        ten = phan_tu[0].strip()              
        tuoi = int(phan_tu[1].strip())       
        diem = int(phan_tu[2].strip())       
        danh_sach.append((ten, tuoi, diem))
    else:
        print("Dữ liệu không hợp lệ")
danh_sach_sap_xep = sorted(danh_sach, key=lambda x: (x[0], -x[1], -x[2]))
print("Danh sách sau khi sắp xếp:")
for muc in danh_sach_sap_xep:
    print(muc)