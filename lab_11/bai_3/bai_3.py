def cuc_tri(a, k):
    return a[k - 1] < a[k] > a[k + 1] or a[k - 1] > a[k] < a[k + 1]

def tim_cuc_tri(inf, out):
    with open(file= inf, mode= 'r') as f:
        a = list(map(int, f.readline().strip().split()))
    ket_qua = []
    for i in range(1, len(a) - 1):
        if cuc_tri(a, i):
            ket_qua.append(a[i])

    with open(file= out, mode= 'w') as f:
        f.write('Cac phan tu cuc tri: ' + ' '.join(map(str, ket_qua)) + '\n')
        f.write('Tong cac phan tu cuc tri: ' + str(len(ket_qua)))

tim_cuc_tri('f_in.dat', 'f_out.dat')