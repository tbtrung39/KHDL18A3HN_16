def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def loc_so_nguyen_to(filename_in, filename_out):
    with open(filename_in, 'r') as f:
        ds = list(map(int, f.read().split()))

    so_ngto = sorted(set(filter(la_nguyen_to, ds)))

    with open(filename_out, 'w') as f:
        f.write(' '.join(map(str, so_ngto)))

loc_so_nguyen_to("f_in.dat", "f_out.dat")
