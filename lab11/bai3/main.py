def la_cuc_tri(a, i):
    return (a[i - 1] < a[i] > a[i + 1]) or (a[i - 1] > a[i] < a[i + 1])

def tim_cuc_tri(in_file, out_file):
    with open(in_file, 'r', encoding = 'utf-8') as f:
        a = list(map(int, f.read().strip().split()))

    ketqua = []
    for i in range(1, len(a) - 1):
        if la_cuc_tri(a, i):
            ketqua.append(a[i])

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(str(len(ketqua)) + '\n')
        f.write(' '.join(map(str, ketqua)) + '\n')

tim_cuc_tri('f_in.dat', 'f_out.dat')
print("Đã ghi kết quả vào f_out.dat")