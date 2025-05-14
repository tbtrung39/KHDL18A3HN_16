def nhap_ma_tran(n):
    matran=[]
    for i in range(n):
        row=list(map(int,input(f"nhap dong {i+1} (cach nhau boi dau cach): ").split()))
        matran.append(row)
    return matran

def in_ma_tran(matran):
    print("ma tran: ")
    for row in matran:
        print(" ".join(map(str, row)))

def ma_tran_chuyen_vi(matran):
    n=len(matran)
    return [[matran[j][i] for j in range(n)] for i in range(n)]

def la_ma_tran_doi_xung(matran):
    chuyen_vi=ma_tran_chuyen_vi(matran)
    return matran==chuyen_vi
