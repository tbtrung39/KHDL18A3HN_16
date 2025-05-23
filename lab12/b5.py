def tinh_S1(n):
    if n == 1:
        return 1
    return n + tinh_S1(n - 1)

def tinh_S2(n):
    if n == 1:
        return 1
    return n**2 + tinh_S2(n - 1)

def nhap_va_tinh_tong():
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n <= 0:
            raise ValueError("n phải là số nguyên dương!")

        s1 = tinh_S1(n)
        s2 = tinh_S2(n)

        print(f"Tổng S1 = {s1}")
        print(f"Tổng S2 = {s2}")

    except ValueError as e:
        print("Lỗi:", e)

nhap_va_tinh_tong()
