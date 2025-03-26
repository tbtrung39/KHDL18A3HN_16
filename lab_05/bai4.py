s1=input("nhap chuoi so s1:")
s2=input("nhap chuoi so s2:")
s=""
min_len=min(len(s1),len(s2))
for i in range(min_len):
    s +=s1[i]+s2[i]
s +=s1[min_len:]+s2[min_len:]
print("chuoi so sau khi chon:",s)