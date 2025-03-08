chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
num = input("Nhập một số thập phân: ")
if "." in num:
    nguyen = num[:num.index(".")]
    thap_phan = num[num.index(".") + 1:]
    ket_qua = ""
    i = 0
    while i < len(nguyen):
        ket_qua += chu_so[int(nguyen[i])] + " "
        i += 1
    ket_qua += "phẩy "
    j = 0
    while j < len(thap_phan):
        ket_qua += chu_so[int(thap_phan[j])] + " "
        j += 1
    print(f"{num} là: {ket_qua.strip()}")
else:
    ket_qua = ""
    i = 0
    while i < len(num):
        ket_qua += chu_so[int(num[i])] + " "
        i += 1
    print(f"{num} là: {ket_qua.strip()}")
