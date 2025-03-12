n = int(input("Nhập số n : "))
if n == 0:
    print("không")
else:
    result = ""
    while n > 0:
        chu_so = n % 10  
        n = n // 10
        if chu_so == 0:
            result = "không " + result
        elif chu_so == 1:
            result = "một " + result
        elif chu_so == 2:
            result = "hai " + result
        elif chu_so == 3:
            result = "ba " + result
        elif chu_so == 4:
            result = "bốn " + result
        elif chu_so == 5:
            result = "năm " + result
        elif chu_so == 6:
            result = "sáu " + result
        elif chu_so == 7:
            result = "bảy " + result
        elif chu_so == 8:
            result = "tám " + result
        elif chu_so == 9:
            result = "chín " + result
    print("Kết quả:", result.strip())  