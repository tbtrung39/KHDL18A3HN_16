import random
ds = []
for i in range(1000):
    so = random.randint(1, 99999)
    ds.append(so)
#1 dùng sorted
ds_sorted1 = sorted(ds)
print("Danh sách sau khi sắp xếp (dùng sorted()):", ds_sorted1[:20], "...") 
#2 kh dùng sorted 
ds_sorted2 = ds[:]  
n = len(ds_sorted2)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if ds_sorted2[j] > ds_sorted2[j + 1]:  
            ds_sorted2[j], ds_sorted2[j + 1] = ds_sorted2[j + 1], ds_sorted2[j]
print("Danh sách sau khi sắp xếp (không dùng sorted()):", ds_sorted2[:20], "...")