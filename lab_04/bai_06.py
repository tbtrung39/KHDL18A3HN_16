so = int(input("nhập số: "))
while so > 0:
    chu_so = so % 10
    if chu_so == 0:
        print("không", end=" ")
    elif chu_so == 1:
        print("một", end=" ")
    elif chu_so == 2:
        print("hai", end=" ")
    elif chu_so == 3:
        print("ba", end=" ")
    elif chu_so == 4:
        print("bốn", end=" ")
    elif chu_so == 5:
        print("năm", end=" ")
    elif chu_so == 6:
        print("sáu", end=" ")
    elif chu_so == 7:
        print("bảy", end=" ")
    elif chu_so == 8:
        print("tám", end=" ")
    elif chu_so == 9:
        print("chín", end=" ")
    so //= 10
    
    

   
