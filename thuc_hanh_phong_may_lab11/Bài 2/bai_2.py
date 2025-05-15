def sap_xep_day_so(infile, outfile):
    with open(infile, 'r') as f:
        day_so = list(map(int, f.read().strip().split()))

    day_so.sort()

    with open(outfile, 'w') as f:
        f.write(' '.join(map(str, day_so)))

sap_xep_day_so("Inp.txt", "out.dat")
print("Đã ghi dãy số đã sắp xếp vào out.dat")
