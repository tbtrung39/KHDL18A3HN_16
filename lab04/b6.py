so_bang_chu = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
num = input("Nhập một số nguyên: ")
ket_qua = "Âm " if num[0] == '-' else ""
for ch in num.lstrip('-'): 
    ket_qua += so_bang_chu[int(ch)] + " "
print("Số dưới dạng chữ:", ket_qua.strip())
