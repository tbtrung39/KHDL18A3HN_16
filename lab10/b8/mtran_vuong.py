def nhap_mtran(n):
    matran= []
    print(f"nhap ptu cho ma tran{n}x {n}")
    for i in range(n):
        hang= []
        for j in range(n):
            x = float(input(f"nhap ptu [{i}][{j}]:"))
            hang.append(x)
        matran.append(hang)
    return matran
def in_ma_tran(matran):
    for hang in matran:
        print('\t'.join(str(x) for x in hang))
def chuyen_vi(matran):
    n = len(matran)
    return[[matran[i][j] for j in range (n) for i in range (n)]]
def ktra_doi_xung(matran):
    n = len(matran)
    for i in range():
        for j in range(n):
            if matran [i][j] != matran[j][i]:
                return False
    return True