def hien_thi(text, odd):
    with open(file= text, mode= 'r') as f:
        matrix = f.readlines()
        print('Dong dau tien:', matrix[0])
        print('Dong thu 3:', matrix[2])
        print('Noi dung:')
        for i in matrix:
            print(i, end= '')

        with open(file= odd, mode='w') as r:
            number = list(map(int, f.readline().strip().split()))
            for i in number:
                if i % 2 != 0:
                    r.write(i)
            r.write(matrix[3])

hien_thi('text.txt', 'ODD.txt')