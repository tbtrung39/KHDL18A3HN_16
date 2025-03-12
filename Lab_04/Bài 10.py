n = input("Nhập một số: ")
result = " "
for digit in n:
    if digit == '0':
        result += "không "
    elif digit == '1':
        result += "một "
    elif digit == '2':
        result += "hai "
    elif digit == '3':
        result += "ba "
    elif digit == '4':
        result += "bốn "
    elif digit == '5':
        result += "năm "
    elif digit == '6':
        result += "sáu "
    elif digit == '7':
        result += "bảy "
    elif digit == '8':
        result += "tám "
    elif digit == '9':
        result += "chín "
    elif digit == '.':
        result += "chấm "
print("Kết quả:", result.strip())