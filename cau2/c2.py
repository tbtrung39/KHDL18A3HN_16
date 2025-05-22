def tao_file_inp():
    with open('inp.txt','w')as f:
        f.write('5 2 9 1 8 7')
def sap_sep_file_inp():
    try:
        with open('inp.txt','r')as file_in:
            data=file_in.read().split()
            numbers=[int(num)for num in data]
        numbers.sort()
        with open('out.dat','w')as file_out:
            file_out.write(''.join(str(num)for num in numbers))
            print('da sap xep xong ket qua ghi vao file out.dat')
    except FileNotFoundError:
        print('khong tim thay file inp.txt')
    except ValueError:
        print('file inp.txt co du lieu khong hop le')
tao_file_inp()
sap_sep_file_inp()