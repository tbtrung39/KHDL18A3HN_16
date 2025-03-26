str="Chuoi, chuoi thu nhat"
tu_hien_tai=""
for char in str:
    if "a"<=char<="z" or "A"<=char<="Z":
        tu_hien_tai+=char
    else:
        if tu_hien_tai:
            print(tu_hien_tai)
            tu_hien_tai=""
if tu_hien_tai:
    print(tu_hien_tai)