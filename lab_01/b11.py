# câu 11
# Khai báo biến
n = int(input("Nhập số lần tung xúc xắc: "))

xac_suat_3_ra_6 = (1/6) * (1/6) * (1/6)

xac_suat_khong_3_ra_6 = 1 - xac_suat_3_ra_6

xac_suat_khong_co_it_nhat_1_lan = xac_suat_khong_3_ra_6 ** n

xac_suat_it_nhat_1_lan = 1 - xac_suat_khong_co_it_nhat_1_lan

xac_suat_it_nhat_1_lan = round(xac_suat_it_nhat_1_lan, 2)

print("Xác suất khi tung", n, "lần 3 xúc xắc có ít nhất 1 lần cả 3 ra 6 là:", xac_suat_it_nhat_1_lan)
