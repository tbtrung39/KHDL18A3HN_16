n = int(input(" Nhập một số tự nhiên n: "))
A = []
B = []
for i in range(2, n):
    check = True
    for j in range(2, i):
        if i % j== 0:
            check = False
            break
    if check and n % i== 0:
        if i not in A:
            A.append(i)
    if check and n % i!= 0:
        if i not in B:
            B.append(i)
A = set(A)
B = set(B)
print(" Tập hợp A( các số nguyên tố là ước của n): ", A if A else 0)
print(" Tập hợp B( các số nguyên tố nhỏ hơn n và không phải là ước của n): ", B if B else 0)