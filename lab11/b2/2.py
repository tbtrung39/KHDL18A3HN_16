def sap_xep_tang_dan(infile, outfile):
    with open(infile, 'r') as f:
        numbers = list(map(int, f.read().strip().split()))

    numbers.sort()

    with open(outfile, 'w') as f:
        f.write(' '.join(map(str, numbers)))


