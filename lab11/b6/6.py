def xu_ly_ma_tran(filename):
    with open(filename) as f:
        lines = f.readlines()

    n = int(lines[0])
    matrix = [list(map(int, line.strip().split())) for line in lines[1:]]

    # a. Dòng đầu tiên và dòng thứ 3
    print("Dong 1:", matrix[0])
    print("Dong 3:", matrix[2])

    # b. Hiện toàn bộ file
    print("\nToan bo file:")
    for row in matrix:
        print(*row)

    # c. Lưu file ODD.txt
    with open("ODD.txt", 'w') as f:
        for row in matrix:
            f.write(' '.join(str(x if x % 2 == 1 else 0) for x in row) + '\n')

# Gọi hàm
xu_ly_ma_tran("matrix.txt")
