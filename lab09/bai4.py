def hoan_vi(ds, i=0):
    if i == len(ds) - 1:
        print(ds)
    else:
        for j in range(i, len(ds)):
            ds[i], ds[j] = ds[j], ds[i]
            hoan_vi(ds, i+1)
            ds[i], ds[j] = ds[j], ds[i]
n = int(input("Nhập n: "))            
day = list(range(1, n+1))            
hoan_vi(day)
