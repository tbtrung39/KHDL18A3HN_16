from doicoso import doicoso1, doicoso2

n = 100
print("Từ hệ 10:")
print("Nhị phân:", doicoso1.dec_to_bin(n))
print("Bát phân:", doicoso1.dec_to_base8(n))
print("Hex:", doicoso1.dec_to_base16(n))

s_bin = '1100100'
print("\nTừ nhị phân:", s_bin)
print("Thập phân:", doicoso2.bin_to_dec(s_bin))
print("Hex:", doicoso2.bin_to_hex(s_bin))
