def tinh_luong(he_so_luong):
    return he_so_luong * 1490000

def tinh_phu_cap(chuc_vu):
    if chuc_vu == "TP":
        return 1000000
    elif chuc_vu == "PP":
        return 700000
    elif chuc_vu == "NV":
        return 300000
    else:
        return 0

def tinh_thuc_linh(luong, phu_cap):
    return luong + phu_cap

def tinh_toan_cho_danh_sach(ds_nhan_vien):
    for nv in ds_nhan_vien:
        luong = tinh_luong(nv['Hệ số lương'])
        phu_cap = tinh_phu_cap(nv['Chức vụ'])
        thuc_linh = tinh_thuc_linh(luong, phu_cap)

        nv['Lương'] = luong
        nv['Phụ cấp chức vụ'] = phu_cap
        nv['Thực lĩnh'] = thuc_linh

def sap_xep_theo_thuc_linh(ds_nhan_vien):
    return sorted(ds_nhan_vien, key=lambda x: x['Thực lĩnh'], reverse=True)

def luu_vao_file(ds_nhan_vien, ten_file):
    with open(ten_file, 'w', encoding='utf-8') as file:
        file.write("Mã NV, Tên NV, Chức vụ, Hệ số lương, Lương, Phụ cấp chức vụ, Thực lĩnh\n")
        for nv in ds_nhan_vien:
            line = f"{nv['Mã NV']},{nv['Tên NV']},{nv['Chức vụ']},{nv['Hệ số lương']},{nv['Lương']},{nv['Phụ cấp chức vụ']},{nv['Thực lĩnh']}\n"
            file.write(line)
