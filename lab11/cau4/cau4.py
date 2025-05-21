def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def uoc_nguyen_to(n):
    tap_uoc = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            if la_so_nguyen_to(i):
                tap_uoc.add(i)
            if la_so_nguyen_to(n // i):
                tap_uoc.add(n // i)
        i += 1
    if la_so_nguyen_to(n):
        tap_uoc.add(n)
    return sorted(tap_uoc)
with open('lab11/cau4/f_in.dat', 'r') as tep_vao:
    cac_dong = tep_vao.readlines()
with open('lab11/cau4/f_out.dat', 'w') as tep_ra:
    for dong in cac_dong:
        so = int(dong.strip())
        cac_uoc_nt = uoc_nguyen_to(so)
        tep_ra.write(' '.join(map(str, cac_uoc_nt)) + '\n')
