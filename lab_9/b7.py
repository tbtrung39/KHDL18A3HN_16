def find_solutions(n, parts=[], current_sum=0):
    if len(parts) == n:
        if current_sum == n:
            print(parts)
        return
    for i in range(n+1):
        find_solutions(n, parts + [i], current_sum + i)

n = int(input("Nhập số n: "))
find_solutions(n)