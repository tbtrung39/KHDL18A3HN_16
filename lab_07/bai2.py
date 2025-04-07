chuoi = input("Nhap cac so tu nhien cach nhau boi dau cach: ")
Numbers = [int(x) for x in chuoi.split()]
A = set(Numbers)
print("Danh sach Numbers:", Numbers)
print("Tap hop A (cac phan tu khac nhau):", A)
