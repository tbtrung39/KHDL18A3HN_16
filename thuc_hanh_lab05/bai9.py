#cách 1 
chuoi = "aaabbbcccccc"  
chuoi_max = ""  
chuoi_hien_tai = chuoi[0]  
for i in range(1, len(chuoi)):
    if chuoi[i] == chuoi[i - 1]:  
        chuoi_hien_tai += chuoi[i]
    else:
        if len(chuoi_hien_tai) > len(chuoi_max):  
            chuoi_max = chuoi_hien_tai
        chuoi_hien_tai = chuoi[i] 
if len(chuoi_hien_tai) > len(chuoi_max):
    chuoi_max = chuoi_hien_tai
print("Chuỗi con dài nhất:", chuoi_max)
