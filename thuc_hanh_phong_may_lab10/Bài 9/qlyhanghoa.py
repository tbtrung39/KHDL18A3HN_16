ds_mat_hang = []

def nhap_thong_tin():
    n = int(input("Số mặt hàng: "))
    for _ in range(n):
        mh = input("Mã hàng: ")
        th = input("Tên hàng: ")
        dvt = input("Đơn vị tính: ")
        dg = float(input("Đơn giá: "))
        sl = int(input("Số lượng: "))
        ds_mat_hang.append({
            'ma': mh,
            'ten': th,
            'dvt': dvt,
            'dongia': dg,
            'soluong': sl,
            'thanhtien': dg * sl,
            'VAT': dg * sl * 0.1
        })

def hien_thi():
    print(f"{'Mã hàng':<10} {'Tên hàng':<20} {'Đơn vị tính':<15} {'Đơn giá':<10} {'Số lượng':<10} {'Thành tiền':<15} {'VAT':<10}")
    print('-' * 80)
    for mh in ds_mat_hang:
        print(f"{mh['ma']:<10} {mh['ten']:<20} {mh['dvt']:<15} {mh['dongia']:<10} {mh['soluong']:<10} {mh['thanhtien']:<15} {mh['VAT']:<10}")

def sap_xep_theo_vat():
    ds_mat_hang.sort(key=lambda x: x['VAT'], reverse=True)
    hien_thi()
