container = input("Nhập số container (gồm 4 chữ cái đầu + số): ").upper()

# Bảng mã chữ cái theo giá trị
letter_values = {
    "A": 10, "B": 12, "C": 13, "D": 14, "E": 15, "F": 16, "G": 17, "H": 18, "I": 19, 
    "J": 20, "K": 21, "L": 23, "M": 24, "N": 25, "O": 26, "P": 27, "Q": 28, "R": 29, 
    "S": 30, "T": 31, "U": 32, "V": 34, "W": 35, "X": 36, "Y": 37, "Z": 38
}

# Tính tổng trọng số
total = 0
for i, char in enumerate(container):
    value = letter_values[char] if char in letter_values else int(char)
    total += value * (2 ** i)

# Lấy tổng chia 11 để tìm số kiểm tra
check_digit = total % 11
print("Số kiểm tra:", check_digit)
