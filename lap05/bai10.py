Str1= "Abc12345"
Str2= "Abc123456878"
len1 = len(Str1)
len2 = len(Str2)
chuoi_con_dai_nhat = ""
for i in range( len1):
    j= i+ 1
    for j in range( 1, len1+ 1):
        chuoi_con = Str1[i:j]
        if chuoi_con in Str2 and len(chuoi_con) > len(chuoi_con_dai_nhat):
            chuoi_con_dai_nhat = chuoi_con
print(" Chuỗi kí tự con chung của hai chuỗi có độ dài cực đại: ",chuoi_con_dai_nhat)