try:
    file = input('Nhap ten file: ')
    other_file = input('Nhap ten file khac de luu: ')

    with open(file= file, mode= 'r', encoding= 'utf-8') as f:
        read = f.read()

    with open(file= other_file, mode= 'w', encoding= 'utf-8') as f:
        f.write(read)
    print('Xong')

except FileNotFoundError:
    print('Khong tim thay file')
except:
    print('Loi')