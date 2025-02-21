# câu 11 
n = int(input("nhập số lần tung xúc xắc: "))
p_khong_ra = 215 / 216 
p_it_nhat_1_lan = 1 - (p_khong_ra ** n)
print(f"xác suất có ít nhất 1 lần cả 3 lần xúc xắc ra 6: {p_it_nhat_1_lan:.2f}")