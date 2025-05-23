n = int(input("Nhập số lần tung xúc xắc: "))
# xác suất để mỗi lần tung đều là 6 
a = 1/216
# ít nhấ 1 lần đều là 6 
xac_suat = 1 - (1-a)**n
print(f"Kết quả: {xac_suat:.2f}")