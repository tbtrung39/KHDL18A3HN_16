Str = input("Nhập 1 chuỗi ký tự: ").upper()
for i in Str:
    if '0' <= i <= '9' and 'A' <= i <= 'F':
        Str = i
    print(Str)