ds = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174,
      150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
      162, 159, 165, 165, 170, 180, 155, 159, 155, 153,
      162, 180, 168, 168, 167, 170]
print("So luong sinh vien trong nhom:", len(ds))
trung_binh = sum(ds) / len(ds)
print("Chieu cao trung binh cua sinh vien trong nhom:", round(trung_binh, 2), "cm")
khac_nhau = sorted(set(ds))
print("Cac chieu cao khac nhau cua sinh vien trong nhom:")
print(khac_nhau)
trung_binh = sum(ds) / len(ds)
print("\nChieu cao trung binh cua nhom:", round(trung_binh, 2), "cm")
