x = float(input("Nhập giá trị x: "))
cos_x, term, k = 1, 1, 0
while abs(term) > 1e-4:
    k += 1
    term *= -x**2 / ((2*k) * (2*k - 1))
    cos_x += term
print("cos(x) ≈", cos_x)
