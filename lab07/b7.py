A = set()
B = set()

while True:
    m = input("Nhập ký tự cho tập hợp A (nhập ESC để thoát): ")
    n = input("Nhập ký tự cho tập hợp B (nhập CSE để thoát): ")
    
    if m == 'ESC' and n == 'CSE':
        break

    A.add(m)
    B.add(n)

print("Tập hợp A:", A)
print("Tập hợp B:", B)
print("Phần tử chung:", A.intersection(B))
