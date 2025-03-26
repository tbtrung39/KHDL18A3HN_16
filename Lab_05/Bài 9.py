Str = input("Nhập chuỗi: ")
len_max = ""  
Str1 = ""  
for i in range(len(Str)):
    if i == 0 or Str[i] == Str[i - 1]:
        Str1= Str1+ Str[i]  
    else:
        if len(Str1) > len(len_max):  
            len_max = Str1  
        Str1 = Str[i]  
if len(Str1) > len(len_max):
    len_max = Str1
print("Chuỗi con có độ dài cực đại và giống nhau: ", len_max)















