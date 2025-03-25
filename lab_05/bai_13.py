A = input("Nhập chuỗi: ")
B = input("Nhập chuỗi: ")
equation = True
while equation:
    if equation:
        for i in A:
            if '0' <= i <= '9':
                A = i
                print(A, end='+')
        print('')
        for j in B:
            if '0' <= j <= '9':
                B = j
                print(B, end='+')
    else:
        print("Không tồn tại cách đặt")