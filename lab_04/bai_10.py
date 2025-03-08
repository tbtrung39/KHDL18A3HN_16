chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

so = input("Nhập một số thập phân: ")

i = 0
while so[i:]:  
    if so[i] == ".":
        print("chấm", end=" ")
    else:
        print(chu_so[int(so[i])], end=" ")
    i += 1