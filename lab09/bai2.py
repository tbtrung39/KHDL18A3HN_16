def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)
def ucln_list(n):
    if len(n) == 1:
        return n[0]
    else:
        return ucln(n[0], ucln_list(n[1:]))
i = int(input("Nhập số lượng phần tử: "))
n = []
for _ in range(n):
    n.append(int(input("Nhập số: ")))
kqua= ucln_list(n)
print("UCLN của dãy số là:", kqua)