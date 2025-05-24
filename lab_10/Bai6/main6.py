import doicoso2

hex_str = input("Nhập số hex: ")
print("Hex sang nhị phân:", doicoso2.hex_to_bin(hex_str))
print("Hex sang thập phân:", doicoso2.hex_to_dec(hex_str))

bin_str = input("Nhập số nhị phân: ")
print("Nhị phân sang thập phân:", doicoso2.bin_to_dec(bin_str))
print("Nhị phân sang hex:", doicoso2.bin_to_hex(bin_str))
