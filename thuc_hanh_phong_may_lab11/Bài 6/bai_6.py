def in_dong_1_va_3():
    with open("matran.txt", 'r') as f:
        n = int(f.readline().strip())
        dong = [list(map(int, line.split())) for line in f.readlines()[:n]]
    
    if len(dong) > 0:
        print("Dòng 1:", dong[0])
    if len(dong) > 2:
        print("Dòng 3:", dong[2])
    else:
        print("Ma trận không đủ 3 dòng.")

in_dong_1_va_3()

def in_toan_bo_file():
    try:
        with open("matran.txt", 'r') as f:
            noi_dung = f.read()
            if noi_dung.strip():
                print(noi_dung)
            else:
                print("Tệp rỗng.")
    except FileNotFoundError:
        print("Tệp matran.txt không tồn tại.")

in_toan_bo_file()

def tach_so_le():
    with open("matran.txt", 'r') as f:
        n = int(f.readline().strip())
        matran = [list(map(int, line.split())) for line in f.readlines()[:n]]
    
    with open("ODD.txt", 'w') as f:
        for dong in matran:
            f.write(' '.join(str(x) if x % 2 == 1 else '0' for x in dong) + '\n')

tach_so_le()

def in_dong_cuoi_odd():
    try:
        with open("ODD.txt", 'r') as f:
            dong = f.readlines()
            if dong:
                print("Dòng cuối của ODD.txt:", dong[-1].strip())
            else:
                print("Tệp ODD.txt rỗng.")
    except FileNotFoundError:
        print("Tệp ODD.txt không tồn tại.")

in_dong_cuoi_odd()