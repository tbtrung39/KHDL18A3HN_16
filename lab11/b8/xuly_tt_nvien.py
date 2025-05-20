def tinh_luong(he_so):
    return he_so * 1490000

def tinh_phu_cap(chuc_vu):
    if chuc_vu == 'TP':
        return 1000000
    elif chuc_vu == 'PP':
        return 700000
    else:
        return 300000

def tinh_thuc_linh(luong, phu_cap):
    return luong + phu_cap
