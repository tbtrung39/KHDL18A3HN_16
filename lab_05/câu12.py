#câu12: cho chuoi ky tu Str, ta gọi 1 từ trong chuỗi ký tự...
s1=input("nhap chuoi ky tu:")
for ky_tu in [',' '\n']:
    s1=s1.replace(ky_tu,'')
tu=s1.split()
for i in tu:
    print(tu)