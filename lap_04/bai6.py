n = int(input("Nhập số n : "))

if n == 0:
    print("không")
else:
    result = ""
    while n > 0:
        digit = n % 10  
        n = n // 10 

        if digit == 0:
            result = "không " + result
        elif digit == 1:
            result = "một " + result
        elif digit == 2:
            result = "hai " + result
        elif digit == 3:
            result = "ba " + result
        elif digit == 4:
            result = "bốn " + result
        elif digit == 5:
            result = "năm " + result
        elif digit == 6:
            result = "sáu " + result
        elif digit == 7:
            result = "bảy " + result
        elif digit == 8:
            result = "tám " + result
        elif digit == 9:
            result = "chín " + result

    print("Kết quả:", result.strip())  