def uoc(n):
    so = []
    for i in range(1, n + 1):
        if n % i == 0:
            so.append(i)
    return so

n = int(input("Nhập 1 số nguyên: "))
uoc_so = uoc(n)
print(f'{uoc_so} là ước của {n}')