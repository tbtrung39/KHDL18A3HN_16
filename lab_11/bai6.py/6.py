def xu_ly_ma_tran(filename):
    with open(filename) as f:
        lines = f.readlines()

    n = int(lines[0])
    matrix = [list(map(int, line.strip().split())) for line in lines[1:]]

    print("Dong 1:", matrix[0])
    print("Dong 3:", matrix[2])

    print("\nToan bo file:")
    for row in matrix:
        print(*row)

    with open("ODD.txt", 'w') as f:
        for row in matrix:
            f.write(' '.join(str(x if x % 2 == 1 else 0) for x in row) + '\n')

xu_ly_ma_tran("matrix.txt")