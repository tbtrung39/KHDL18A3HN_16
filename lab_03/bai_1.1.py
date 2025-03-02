char_values = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20,
    'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31,
    'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}
container_code = input("Nhập số container (4 chữ cái + 6 chữ số): ").upper()
# Kiểm tra tính hợp lệ của container code
if len(container_code) != 10 or not container_code[:4].isalpha() or not container_code[4:].isdigit():
    print("Mã container không hợp lệ! Vui lòng nhập lại.")
else:
    total_weight = 0
    for i in range(10):
        if i < 4:
            value = char_values[container_code[i]]  
        else:
            value = int(container_code[i]) 
        weight = value * (2 ** i) 
        total_weight += weight
    check_digit = total_weight % 11
    print(f"Số kiểm tra container là: {check_digit}")
