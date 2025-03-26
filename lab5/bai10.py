str1="Abc12345"
str2="Abc123456878"
len1=len(str1)
len2=len(str2)
chuoi_con_dai_nhat=""
for i in range(len1):
    j=i+1
    for j in range(1,len1+1):
        chuoi_con=str1[i:j]
        if chuoi_con in str2 and len(chuoi_con) > len(chuoi_con_dai_nhat):
            chuoi_con_dai_nhat=chuoi_con
print("Cuoi ky tu con chung cua hai chuoi co do dai cuc dai:",chuoi_con_dai_nhat)