def hoan_vi(arr, l, r):
    if l == r:
        print(arr)
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]  # Hoán đổi
            hoan_vi(arr, l + 1, r)
            arr[l], arr[i] = arr[i], arr[l]  # Hoán đổi lại (quay lui)

n = int(input("Nhập số n: "))
lst = list(range(1, n + 1))
hoan_vi(lst, 0, n - 1)
