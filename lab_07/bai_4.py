nhom_sinh_vien = {161, 182, 161, 154, 176, 170, 167, 171, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
                  162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170}

print('So sinh vien trong nhom la:', len(nhom_sinh_vien))

trung_binh = (sum(nhom_sinh_vien))/(len(nhom_sinh_vien))
print('Trung binh chieu cao trong nhom la:', trung_binh)

khac_nhau = sorted(nhom_sinh_vien)
print(khac_nhau)
print(sum(khac_nhau)/len(khac_nhau))