Str = input("Nhap chuoi ky tu: ")
count = 0  
for i in Str:
    if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9'):
        count += 1  
print("SSo ky tu chi la tieng Anh la:", count)
