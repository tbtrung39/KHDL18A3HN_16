Str1= "Abc"
Str2= "12345"
result= ""
max_len = max(len(Str1), len(Str2))
for i in range(max_len):
    if i < len(Str1):  
        result = result+ Str1[i]
    if i < len(Str2):  
        result = result+ Str2[i]
print("Hai chuỗi sau khi trộn là:", result)