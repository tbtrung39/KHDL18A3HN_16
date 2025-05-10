def hoan_vi(S, n, i = 0):
    if i == n:
        print(S)
    else:
        for j in range(i, n):
            S[i], S[j] = S[j], S[i]
            hoan_vi(S, n, i + 1)
            S[i], S[j] = S[j], S[i]

n = int(input('Nhap n = '))
S = [i for i in range(1, n + 1)]
hoan_vi(S, n)