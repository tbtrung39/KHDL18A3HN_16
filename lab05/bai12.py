str1=input("Nhap chuoi ky tu: ")
tu_hien_tai = ""
for char in str1:
    if char.isalpha():
        tu_hien_tai += char
    else:
        if tu_hien_tai:
            print(tu_hien_tai)
            tu_hien_tai = ""
if tu_hien_tai:
    print(tu_hien_tai)