import random
danh_sach=[x for x in range(2021) if x%5==0 and x%7==0]
so=random.randint(0,len(danh_sach)-1)
so_ngau_nhien=danh_sach[so]
print("So ngau nhien chia het cho 5 va 7 la:",so_ngau_nhien)