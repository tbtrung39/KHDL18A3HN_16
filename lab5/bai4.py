str1="Abc"
str2="12345"
result=""
max_len=max(len(str1),len(str2))
for i in range(max_len):
    if i < len(str1):
        result+=str1[i]
    elif i< len(str2):
        result+=str2[i]
print("Hai chuoi sau khi tron la:",result)