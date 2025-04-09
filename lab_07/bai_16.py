a = [i for i in range(101)]

for i in a:
    for j in a:
        if 0 <= i < j <= a[-1] and a[i] + 1 == a[j]:
            k = (i, j)
            print(k)