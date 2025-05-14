def nhap_ma_tran(n):
    return [[int(input(f"Nhập phần tử [{i}][{j}]: ")) for j in range(n)] for i in range(n)]

def in_ma_tran(ma_tran):
    for row in ma_tran:
        print(row)

def ma_tran_chuyen_vi(ma_tran):
    return [list(row) for row in zip(*ma_tran)]

def kiem_tra_doi_xung(ma_tran):
    chuyen_vi = ma_tran_chuyen_vi(ma_tran)
    return ma_tran == chuyen_vi
