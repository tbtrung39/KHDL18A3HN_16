n = int(input("nhập số lần tung xúc xắc: "))
xác_xuất_không_ra_6 = (125/216)**n
xác_xuất_ít_nhất_1_lần_ra_6 = 1 - xác_xuất_không_ra_6
print(f"xác xuất có ít nhất một lần ra mặt sau sau {n} lần ttung là: {xác_xuất_ít_nhất_1_lần_ra_6:.2f}")