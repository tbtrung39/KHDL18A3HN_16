a=input('Nhap mot ky tu: ')
while True:
    if len(a)==1:
        break
    else:
        print('vui long nhap mot ky tu!')
        a=input('Nhap mot ky tu: ')
print('Ma ASCII cua ky tu',a,'la:',ord(a))