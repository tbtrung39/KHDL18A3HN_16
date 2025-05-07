def permutation(n):
    if n == 1:
        return [[1]]
    hoan_vi_truoc = permutation(n - 1)
    kết_quả = []
    for hv in hoan_vi_truoc:
        for i in range(len(hv) + 1):
            mới = hv[:i] + [n] + hv[i:]
            kết_quả.append(mới)
    return kết_quả
def main():
    n = int(input("Nhập số nguyên n: "))
    hoan_vis = permutation(n)
    print(f"\nCó {len(hoan_vis)} hoán vị của dãy [1..{n}]:")
    for hv in hoan_vis:
        print(hv)
if __name__ == "__main__":
    main()
