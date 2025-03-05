container_number = input("Nhập số container (10 ký tự): ")
count = 0
for _ in container_number:
    count += 1

if count != 10:
    print("Số container không hợp lệ!")
else:
    total = 0
    power = 1
    for index in range(4):
        char = container_number[index]
        if 'A' <= char <= 'K':
            value = ord(char) - ord('A') + 10
        elif 'L' <= char <= 'U':
            value = ord(char) - ord('L') + 23
        elif 'V' <= char <= 'Z':
            value = ord(char) - ord('V') + 34
        else:
            print("Số container không hợp lệ! Ký tự đầu phải là chữ cái.")
            break
        total += value * power
        power *= 2
    for index in range(4, 10):
        char = container_number[index]
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        else:
            print("Số container không hợp lệ! 6 ký tự cuối phải là số.")
            break
        total += digit * power
        power *= 2
    check_digit = total % 11
    print( value)
    print("Số kiểm tra container là:", check_digit)
