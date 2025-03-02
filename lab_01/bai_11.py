# Nhập số lần tung xúc xắc
n = int(input("Nhập số lần tung xúc xắc: "))
# Xác suất không có lần nào ra (6,6,6)
xac_suat_khong_co_666 = (215 / 216) ** n
# Xác suất có ít nhất 1 lần ra (6,6,6)
xac_suat_co_666 = 1 - xac_suat_khong_co_666
# Làm tròn kết quả đến 2 chữ số thập phân
xac_suat_co_666 = round(xac_suat_co_666, 2)
print(f"Xác suất có ít nhất 1 lần ra (6,6,6): {xac_suat_co_666}")