so_sang_chu = {
    '0': "không", '1': "một", '2': "hai", '3': "ba", '4': "bốn",
    '5': "năm", '6': "sáu", '7': "bảy", '8': "tám", '9': "chín"
}
so_nhap = input("Nhập số nguyên: ")
ket_qua = ""
i = 0
while i < len(so_nhap):
    ky_tu = so_nhap[i]
    if ky_tu in so_sang_chu:
        ket_qua += so_sang_chu[ky_tu] + " "
    i += 1
print("Bằng chữ:", ket_qua.strip())
