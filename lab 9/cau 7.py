def tim_cach_phan_tich(n, danh_sach=None, tong_hien_tai=0):
    # Khởi tạo danh sách nếu chưa có
    if danh_sach is None:
        danh_sach = []

    # Nếu đã có đủ n phần tử
    if len(danh_sach) == n:
        # Và tổng các phần tử đúng bằng n thì in ra
        if tong_hien_tai == n:
            print(danh_sach)
        return

    # Thử tất cả giá trị từ 0 đến n cho mỗi vị trí
    for i in range(n + 1):
        tim_cach_phan_tich(n, danh_sach + [i], tong_hien_tai + i)

# Nhập số nguyên n từ bàn phím
so_n = int(input("Nhập số nguyên dương n: "))
tim_cach_phan_tich(so_n)