nhom_sv={161, 182, 161, 154, 176, 170, 167, 171, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 
         162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170}

print("so sinh vien trong nhom la:", len(nhom_sv))

TB=(sum(nhom_sv))/(len(nhom_sv))
print("Trung binh chieu cao trong nhom la:", TB)

khac_nhau=sorted(nhom_sv)
print(khac_nhau)
print(sum(khac_nhau)/len(khac_nhau))