number = set()
print("Nhập số nguyên (nhấn Enter để tiếp tục, nhập 'ECS' để dừng):")

while True:
    value = input()
    if value.upper() == 'ECS':
        break
    try:
        number.add(int(value))
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

print("Tập hợp số nguyên:", number)

