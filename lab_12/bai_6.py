import re

def is_email(ten):
    return re.fullmatch(r'[A-Za-z0-9]' + ten) is not None

lst = []
while True:
    ten = input('Nhap ten(nhan qq de thoat): ')
    if ten.lower() == 'qq':
        break
    try:
        if not is_email(ten):
            raise ValueError('Ten khong hop le.')
        email = ten + '@companygame.com'
        lst.append(email)
        print('Da tao:', email)
    except ValueError as e:
        print('Loi:', e)
    except:
        print('Loi')

for i in lst:
    print(i)
