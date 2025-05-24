number = set()
print("Nhập số nguyên::")
while True:
    value = input()
    if value.upper() == 'q':
        break
    try:
        number.add(int(value))
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
print("Tập hợp số nguyên: ", number)