n = int(input("Nhập số n: "))
if n == 0:
    print("không")
else:
    ket_qua = ""
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    while n > 0:
        ket_qua = chu_so[n % 10] + " " + ket_qua 
        n //= 10  
    print("Kết quả:", ket_qua.strip())  
