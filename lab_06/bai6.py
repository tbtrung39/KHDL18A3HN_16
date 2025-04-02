import random
#1
ds=[]
for i in range(1000):
    so=random.randint(1,99999)
    ds.append(so)
print("20 so dau tien trong danh sach ban dau la:",ds[:20])

#2
ds_1=sorted(ds)
print("\n20 so dau tien sau khisap xep bang sorted() la:",ds_1[:20])

#3
ds_2=ds.copy()
n=len(ds_2)
for i in range(n):
    for j in range(n-1):
        if ds_2[j]>ds_2[j+1]:
            ds_2[j],ds_2[j+1]=ds_2[j+1],ds_2[j]
print("\n20 so dau tien sau khi sap xep thu cong la:",ds_2[:20])