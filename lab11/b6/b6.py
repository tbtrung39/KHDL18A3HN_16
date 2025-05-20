def xu_ly_ma_tran(ten_file):
    # Đọc file
    with open(ten_file, 'r') as f:
        dong = f.readlines()

    n = int(dong[0])  # số dòng (n)
    ma_tran = [list(map(int, dong[i].strip().split())) for i in range(1, len(dong))]

    # a. In dòng đầu và dòng thứ 3
    print("Dòng 1:", ma_tran[0])
    if len(ma_tran) >= 3:
        print("Dòng 3:", ma_tran[2])

    # b. In toàn bộ ma trận
    print("\nToàn bộ ma trận:")
    for hang in ma_tran:
        print(*hang)

    # c. Ghi file ODD.txt: chỉ giữ số lẻ, chẵn thì thay bằng 0
    with open("ODD.txt", 'w') as f:
        for hang in ma_tran:
            hang_moi = [str(x) if x % 2 == 1 else '0' for x in hang]
            f.write(' '.join(hang_moi) + '\n')

# Gọi hàm
xu_ly_ma_tran("matrix.txt")
