def tinh_tong_s1(n):
    if n < 1:
        raise ValueError("Giá trị n phải lớn hơn hoặc bằng 1.")
    return n + tinh_tong_s1(n - 1) if n > 1 else 1

def tinh_tong_s2(n):
    if n < 1:
        raise ValueError("Giá trị n phải lớn hơn hoặc bằng 1.")
    return n**2 + tinh_tong_s2(n - 1) if n > 1 else 1

def nhap_va_tinh_tong():
    try:
        n = int(input("Nhập giá trị n: "))
        s1 = tinh_tong_s1(n)
        s2 = tinh_tong_s2(n)
        print(f"S1 = {s1}, S2 = {s2}")
    
    except ValueError as e:
        print("Lỗi:", e)

nhap_va_tinh_tong()