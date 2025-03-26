Str= "10000010"
so_thap_phan= 0
for i in range(len(Str)):
    ky_tu = Str[i]
    if ky_tu == "1":
        so_thap_phan= so_thap_phan+ 2 ** ( len(Str)- 1- i)
print("Giá trị thập phân: ", so_thap_phan)