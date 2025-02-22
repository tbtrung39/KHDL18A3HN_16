# Bài 2 : Nhập các giá trị s tính bằng giây, m tính bằng phút, h tính bằng giờ, d tính bằng ngày.Viết công thức đổi giá trị “d ngày, h giờ, m phút, s giây
tong_so_giay = int(input('Nhập vào tổng số giây: '))
d = tong_so_giay // (24 *3600)
du = tong_so_giay % (24 *3600)
h = du // 3600
du = du % 3600
m = du // 60
s = du % 60
print(f'{d} ngày , {h} giờ , {m} phút , {s} giây')