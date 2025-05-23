def tim_so_chung(m, n, chung):
    with open(file= m, mode= 'r') as f:
        number1 = f.readline().strip().split()
    with open(file= n, mode= 'r') as r:
        number2 = r.readline().strip().split()

    jinx = []
    for i in number1:
        for j in number2:
            if i == j:
                jinx.append(j)

    with open(file= chung, mode= 'w') as q:
        q.write(str(jinx))

tim_so_chung('m_nums.txt', 'n_nums.txt', 'so_chung.txt')