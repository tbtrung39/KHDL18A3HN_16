ky_tu = [['$','#','@'],
         ['0','1','2','3','4','5','6','7','8','9'],
         ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'],
         ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']]

password = input("NHập mật khẩu: ")

while True:
    for i in password:
        if i not in ky_tu[0]:
            print("Phải có 1 ký tự trong mật khẩu.")
        elif i not in ky_tu[1]:
            print("Phải có 1 chữ số trong mật khẩu.")
        elif i not in ky_tu[2]:
            print("Phải có 1 chữ cái thường trong mật khẩu.")
        elif i not in ky_tu[3]:
            print("Phải có 1 chữ cái hoa trong mật khẩu.")
        else:
            break
    if len(password) < 6:
        print("Phải tối thiểu 6 ký tự.")
    elif len(password) > 12:
        print("Tối đa 12 ký tự.")
    else:
        break

if ',' in password:
    print(password.split(','))