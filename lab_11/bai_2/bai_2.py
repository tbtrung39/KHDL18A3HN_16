def doc(inp, out):
    with open(file= inp, mode= 'r') as f:
        numbers = sorted(list(map(int, f.readline().strip().split())))

        with open(file= out, mode= 'w') as f:
            f.write(' '.join(numbers) + '\n')

doc('Inp.txt', 'out.dat')