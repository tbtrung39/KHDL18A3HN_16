# Hàm giải bài toán với hai biến x (số gà) và y (số thỏ)
def giaithuat(x, y):
    # Kiểm tra điều kiện tìm được số gà và số thỏ
    if x + y == 36 and 2*x + 4*y == 100:
        print(f"Số gà: {x}, số thỏ: {y}")
        return
    # Nếu không thỏa mãn điều kiện, tiếp tục kiểm tra
    if x + y > 36 or 2*x + 4*y > 100:
        return
    # Đệ quy thử các giá trị khác nhau cho x và y
    giaithuat(x + 1, y)  # Tăng số gà
    giaithuat(x, y + 1)  # Tăng số thỏ

# Bắt đầu với số gà và số thỏ bằng 0
giaithuat(0, 0)
