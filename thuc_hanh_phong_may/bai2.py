d, h, m, s = map(int, input("Nhập số ngày, giờ, phút, giây (cách nhau bởi dấu cách): ").split())

doi_thoi_gian = d * 86400 + h * 3600 + m * 60 + s

print("Tổng số giây:", doi_thoi_gian)
