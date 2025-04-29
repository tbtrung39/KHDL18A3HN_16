def permutation(arr):
    if len(arr) == 1:
        return [arr]
    perms = []
    for i in range(len(arr)):
        m = arr[i]
        rest = arr[:i] + arr[i+1:]
        for p in permutation(rest):
            perms.append([m] + p)
    return perms

n = int(input("Nhập số n: "))
lst = list(range(1, n+1))
result = permutation(lst)

# In kết quả
for p in result:
    print(p)