try:
    file = input('Nhap ten file: ')
    with open(file= file, mode= 'r', encoding= 'utf-8') as f:
        read = f.read()

    with open(file= 'copy.dat', mode= 'w', encoding= 'utf-8') as f:
        f.write(read)
    print('Xong')

except FileNotFoundError:
    print('Khong tim thay file')
except:
    print('Loi')
