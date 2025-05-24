doan_van=input("Hay nhap doan van: ")
tu_don=input("Hay nhap tu don: ")
doan_van_t = ""
count=0
for char in doan_van:
    if char.isalpha():
        doan_van_t += char
    else:
        if doan_van_t != "":
            if doan_van_t == tu_don:
                count += 1
            doan_van_t = ""
if doan_van_t == tu_don:
    count += 1
print("tu don",tu_don,"'xuat hien",count,"lan trong doan van da nhap ")