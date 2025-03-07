print("Nhập các số, chương trình sẽ dừng khi bạn nhập số âm.")
so = 0
while so >= 0:
    so = float(input("Nhập một số: "))
    if so >= 0:
        print("Bạn đã nhập:", so)
    else:
        print("Bạn đã nhập số âm", so, ". Chương trình kết thúc.")