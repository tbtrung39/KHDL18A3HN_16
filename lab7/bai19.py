nv_dict={}
while True:
    print("\n1. Tao moi tu dien\n2.Them nhan vien\n3.Tim kiem nhan vien\n4.Tang luong\n5.Xoa nhan vien\n6.Sap xep nhan vien theo nam sinh\n7.Thoat")
    choice=input("Chon chuc nang:")
    if choice=="1":
        nv_dict.clear()
        print("Da co tao moi tu dien")
    elif choice=="2":
        ma_nv=input("Nhap ma nhan vien (4 so):")
        if ma_nv in nv_dict:
            print("Ma da ton tai")
        else:
            ten_nv=input("Nhap ho ten nhan vien:")
            nam_sinh=int(input("Nhap nam sinh:"))
            luong=int(input("Nhap luong:"))
            nv_dict[ma_nv]=(ten_nv, nam_sinh, luong)
            print("Da them nhan vien")
    elif choice=="3":
        ma_nv=input("Nhap ma nhan vien:")
        print(nv_dict.get(ma_nv, "Khong tim thay"))
    elif choice=="4":
        ma_nv=input("Nhap ma nhan vien:")
        if ma_nv in nv_dict:
            ten_nv, nam_sinh, luong = nv_dict[ma_nv]
            nv_dict[ma_nv] = (ten_nv, nam_sinh, luong + 1000000)
            print("Da tang luong")
        else:
            print("Khong tim thay")
    elif choice=="5":
        ma_nv=input("Nhap ma nhan vien:")
        if nv_dict.pop(ma_nv, None):
            print("Da xoa nhan vien")
        else:
            print("Khong tim thay")
    elif choice=="6":
        for ma_nv, (ten_nv, nam_sinh, luong) in sorted(nv_dict.items(), key=lambda x:[1][1]):
            print(f"Ma: {ma_nv}, Ten: {ten_nv}, Nam sinh: {nam_sinh}, Luong: {luong}")
    elif choice=="7":
        break
    else:
        print("Lua chon khong hop le, vui long nhap lai")