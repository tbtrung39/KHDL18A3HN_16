def tach(ins, outs):
    with open(file= ins, mode= 'r') as f:
        numbers = list(map(int, f.readline().strip().split()))
        even = [str[i] for i in numbers if i % 2 == 0]
        odd = [str[i] for i in numbers if i % 2 != 0]

        with open(file= outs, mode= 'w') as f:
            f.write(' '.join(even) + '\n')
            f.write(' '.join(odd) + '\n')

tach('f_in.dat', 'f_out.dat')