nhan_vien = {}
while True:
    print("\n=== MENU ===")
    print("1. Tao moi tu dien")
    print("2. Them nhan vien")
    print("3. Tim kiem nhan vien theo ma")
    print("4. Tang luong cho nhan vien")
    print("5. Xoa nhan vien theo ma")
    print("6. Sap xep giam dan theo nam sinh")
    print("0. Thoat")
    chon = input("Chon chuc nang: ")
    if chon == "1":
        nhan_vien = {}
        print("Da tao moi tu dien.")
    elif chon == "2":
        ma = input("Nhap ma nhan vien (4 ky tu): ")
        ten = input("Nhap ten nhan vien: ")
        ns = int(input("Nhap nam sinh: "))
        luong = int(input("Nhap luong: "))
        nhan_vien[ma] = [ten, ns, luong]
    elif chon == "3":
        ma = input("Nhap ma nhan vien can tim: ")
        if ma in nhan_vien:
            print(f"{ma}: {nhan_vien[ma]}")
        else:
            print("Khong tim thay.")

    elif chon == "4":
        ma = input("Nhap ma nhan vien can tang luong: ")
        if ma in nhan_vien:
            nhan_vien[ma][2] += 100000
            print("Da tang luong.")
        else:
            print("Khong tim thay.")
    elif chon == "5":
        ma = input("Nhap ma nhan vien can xoa: ")
        if ma in nhan_vien:
            del nhan_vien[ma]
            print("Da xoa.")
        else:
            print("Khong tim thay.")
    elif chon == "6":
        sap_xep = sorted(nhan_vien.items(), key=lambda x: x[1][1], reverse=True)
        for ma, info in sap_xep:
            print(f"{ma}: {info}")
    elif chon == "0":
        print("Thoat chuong trinh.")
        break
    else:
        print("Lua chon khong hop le.")