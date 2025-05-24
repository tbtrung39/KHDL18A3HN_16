A = set()
B = set()
while True:
    m = input("Nhập ký tự tập hợp A: ")
    n = input("Nhập ký tự tập hợp B: ")
    if m == 'q' and n == 'w':
        break
    A.add(m)
    B.add(n)
print(A)
print(B)

print('Phần tử chung:', A.intersection(B))