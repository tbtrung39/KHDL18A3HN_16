print('\n\n\t\t============MENU============') 
print("1. Monday") 
print("2. Tuesday") 
print("3. Wenesday") 
print("4. Thursday") 
print("5. Friday")
print("6. Saturday")
print("7. Sunday")   
print('\n\t\t============END============') 
#Người dùng nhập lựa chọn 
print('Hãy nhập lựa chọn của bạn  (1-->7):',end='') 
luachon=int(input()) 
#Cấu trúc if elif else 
if luachon==1: 
    print('1: Monday\n') 
elif luachon==2: 
    print('2: Tuesday\n') 
elif luachon==3: 
    print('3: Wednesday\n')  
elif luachon==4: 
    print('4: Thursday\n')
elif luachon==5: 
    print('5: Friday\n')
elif luachon==6: 
    print('6: Saturday\n')
elif luachon==7: 
    print('7: Sunday\n')        
else: print('Lựa chọn không hợp lệ. Xin vui lòng kiểm tra lại') 