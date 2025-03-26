tr="Abc@36#50017"
dem=0
for i in str:
    if not ("a"<=i<="z" or "A"<=i<="Z" or "0"<=i<="9"):
        dem+=1
print("So ky tu khong ls chu cai tieng anh va khong la so:",dem)