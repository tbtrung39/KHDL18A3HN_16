
with open('lab11/cau2/Inp.txt', 'r') as f:
    data = list(map(int, f.read().strip().split()))
data.sort()
with open('Out.dat', 'w') as f:
    f.write(' '.join(map(str, data)))
