tnct=int(input("nhap tham nien cong tac (thang): "))
luong_can_ban=1350000
if 0<tnct<12:
    luong=2.34*luong_can_ban
    print(f"luong cua nhan vien la: {luong} vnd")
elif 12<=tnct<36:
    luong=3.33*luong_can_ban
    print(f"luong cua nhan vien la: {luong} vnd")
elif 36<=tnct<60:
    luong=3.66*luong_can_ban
    print(f"luong cua nhan vien la: {luong} vnd")
elif 60<=tnct:
    luong=3.99*luong_can_ban
    print(f"luong cua nhan vien la: {luong} vnd")
else:
    print("khong hop le vui long nhap lai")