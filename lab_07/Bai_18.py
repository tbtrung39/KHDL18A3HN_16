thi_sinh = {}
while True:
    print("\n=== MENU ===")
    print("1. Nhap thi sinh moi")
    print("2. Hien thi danh sach thi sinh")
    print("3. Sap xep thi sinh theo diem giam dan")
    print("0. Thoat")
    chon = input("Chon chuc nang: ")
    if chon == "1":
        sbd = input("Nhap so bao danh: ")
        if sbd in thi_sinh:
            print("So bao danh da ton tai.")
        else:
            ten = input("Nhap ho va ten: ")
            diem = float(input("Nhap diem: "))
            thi_sinh[sbd] = [ten, diem]
            print("Da them thi sinh.")
    elif chon == "2":
        if len(thi_sinh) == 0:
            print("Chua co du lieu.")
        else:
            for sbd, info in thi_sinh.items():
                print(f"SBD: {sbd} | Ten: {info[0]} | Diem: {info[1]}")
    elif chon == "3":
        if len(thi_sinh) == 0:
            print("Chua co du lieu.")
        else:
            sap_xep = sorted(thi_sinh.items(), key=lambda x: x[1][1], reverse=True)
            for sbd, info in sap_xep:
                print(f"SBD: {sbd} | Ten: {info[0]} | Diem: {info[1]}")
    elif chon == "0":
        print("Thoat chuong trinh.")
        break
    else:
        print("Lua chon khong hop le.")