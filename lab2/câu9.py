soKM = int(input(" Nhap so KM: "))
tien_dien = 0
if soKM>= 0 and soKM<= 100:
    tien_dien = soKM*2000
elif soKM>= 101 and soKM<= 200:
    tien_dien = 100* 2000+ (soKM  100)* 2500
elif soKM>= 201 and soKM<= 300:
    tien_dien = 100* 2000+ 100* 2500+ (soKM- 200) * 3000
elif soKM> 300:
    tien_dien= 100* 2000+ 100* 2500+ 100* 3000+ (soKM- 300) * 5000
else:
    print("Nhap sai. nhap lai")
    
