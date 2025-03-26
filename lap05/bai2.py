Str= "Abc@36#50017"
dem= 0
for i in Str:
    if not ( "a"<= i<= "z" or "A"<= i<= "Z" or "0"<= i<= "9" ):
        dem= dem+ 1
print(" Số kí tự không là chữ cái tiếng Anh và không là số: ", dem)