chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
while True:
    try:
        n = int(input("Nhập một số nguyên dương: "))
        if n >= 0:
            break
        else:
            print("Vui lòng nhập số nguyên dương!")
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")
ket_qua = ""
for so in str(n):  
    ket_qua += chu_so[int(so)] + " "
print(f"Số {n} đọc là: {ket_qua.strip()}")