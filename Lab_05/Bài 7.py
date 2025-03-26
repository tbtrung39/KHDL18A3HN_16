Str= "Abc12345"
chuoi_ki_tu_la_so= ""
for i in Str:
    if "0"<= i<= "9":
        chuoi_ki_tu_la_so= chuoi_ki_tu_la_so+ i
print(" Chuỗi kí tự là số: ", chuoi_ki_tu_la_so)
number= int(chuoi_ki_tu_la_so)
tong= 0
for j in range( 1, number):
    if number% j== 0:
        tong= tong+ j
if tong== number:
    print(" Đây là số hoàn hảo")
else:
    print(" Đây không là số hoàn hảo")