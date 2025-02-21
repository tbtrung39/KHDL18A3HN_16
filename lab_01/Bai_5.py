import math
a1, a2 = map(float, input("Nhập x, y của véc-tơ a: ").split())
b1, b2 = map(float, input("Nhập x, y của véc-tơ b: ").split())
cos_ab = (a1*b1+a2*b2)/(math.sqrt(a1**2+a2**2)*math.sqrt(b1**2+b2**2))
tich_vo_huong = math.sqrt(a1**2+a2**2) * math.sqrt(b1**2+b2**2) * cos_ab
print(f"Tích vô hướng của 2 véc_tơ là {tich_vo_huong}")