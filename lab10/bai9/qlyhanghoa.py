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
    for mh in ds_mat_hang:
        print(mh)

def sap_xep_theo_vat():
    ds_mat_hang.sort(key=lambda x: x['VAT'], reverse=True)
    hien_thi()
