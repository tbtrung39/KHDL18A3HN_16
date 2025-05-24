def thap_ha_noi(n, cot_nguon, cot_trung_gian, cot_dich):
    if n == 1:
        print(f"Chuyen dia 1 tu {cot_nguon} sang {cot_dich}")
    else:
        thap_ha_noi(n - 1, cot_nguon, cot_dich, cot_trung_gian)
        print(f"Chuyen dia {n} tu {cot_nguon} sang {cot_dich}")
        thap_ha_noi(n - 1, cot_trung_gian, cot_nguon, cot_dich)
n = int(input("Nhap so dia: "))
print("Cac buoc chuyen dia:")
thap_ha_noi(n, "A", "B", "C")