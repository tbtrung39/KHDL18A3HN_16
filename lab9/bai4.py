def generate_permutations(arr, l, r):
    if l == r:
        print(arr)
    else:
        for i in range(l, r+1):
            arr[l], arr[i] = arr[i], arr[l]  # Hoan doi
            generate_permutations(arr, l+1, r)
            arr[l], arr[i] = arr[i], arr[l]  # Hoan doi lai (quay lui)

n = int(input("Nhap so n: "))
lst = list(range(1, n+1))

generate_permutations(lst, 0, n-1)