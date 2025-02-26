print('\n\n\t\t============MENU============') 
print("1. January")  
print("2. February") 
print("3. March") 
print("4. April") 
print("5. May")
print("6. June")
print("7. July")
print("8. August")
print("9. September")
print("10. October")
print("11. Nocember")
print("12. December")        
print('\n\t\t============END============') 
#Người dùng nhập lựa chọn 
print('Hãy nhập lựa chọn của bạn  (1-->12):',end='') 
luachon=int(input()) 
#Cấu trúc if elif else 
if luachon==1: 
    print('1: January\n') 
elif luachon==2: 
    print('2: February\n') 
elif luachon==3: 
    print('3: March\n')  
elif luachon==4: 
    print('4: April\n')
elif luachon==5: 
    print('5: May\n')
elif luachon==6: 
    print('6: June\n')
elif luachon==7: 
    print('7: July\n')
elif luachon==8: 
    print('8: August\n')
elif luachon==9: 
    print('9: September\n')
elif luachon==10: 
    print('10: October\n')
elif luachon==11: 
    print('11: November\n')
elif luachon==12: 
    print('12: December\n')                
else: print('Lựa chọn không hợp lệ. Xin vui lòng kiểm tra lại') 