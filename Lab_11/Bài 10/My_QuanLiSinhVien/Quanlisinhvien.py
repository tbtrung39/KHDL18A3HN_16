def tinh_tl(tb, rl):
    return round((tb + rl) / 2, 2)

def tinh_diem_tich_luy(ds):
    for sv in ds:
        if isinstance(sv.get("TB"), (int, float)) and isinstance(sv.get("RL"), (int, float)):
            sv["TL"] = tinh_tl(sv["TB"], sv["RL"])
        else:
            sv["TL"] = 0

def sap_xep_theo_rl(ds):
    return sorted(ds, key=lambda sv: sv["RL"])

def tim_sinh_vien_max_tl(ds):
    if not ds:
        return None
    return max(ds, key = lambda sv: sv["TL"])

def luu_file(ds, ten_file):
    try:
        with open(ten_file, "w", encoding = "utf-8") as f:
            f.write("Mã SV, Họ tên, TB, RL, TL\n")
            for sv in ds:
                f.write(f"{sv['Mã SV']},{sv['Họ tên']},{sv['TB']},{sv['RL']},{sv['TL']}\n")
    except Exception as e:
        print(f"Lỗi khi ghi file {ten_file}: {e}")