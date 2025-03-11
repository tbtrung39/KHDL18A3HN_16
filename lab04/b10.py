n = input("Nhập một số: ")

words = ()
for digit in n:
    if digit == '0':
        words += "không "
    elif digit == '1':
        words += "một "
    elif digit == '2':
        words += "hai "
    elif digit == '3':
        words += "ba "
    elif digit == '4':
        words += "bốn "
    elif digit == '5':
        words += "năm "
    elif digit == '6':
        words += "sáu "
    elif digit == '7':
        words += "bảy "
    elif digit == '8':
        words += "tám "
    elif digit == '9':
        words += "chín "
    elif digit == '.':
        words += "chấm "

print("Kết quả:", words.strip())
