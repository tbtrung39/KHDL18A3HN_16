def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)

# Hàm tính UCLN của cả danh sách
def ucln_list(n):
    if len(n) == 1:
        return n[0]
    else:
        return ucln(n[0], ucln_list(n[1:]))
i = int(input("Nhập số lượng phần tử: "))
n = []

# Nhập từng số
for _ in range(n):
    n.append(int(input("Nhập số: ")))
kqua= ucln_list(n)
print("UCLN của dãy số là:", kqua)