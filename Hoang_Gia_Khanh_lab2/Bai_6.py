so = input("Nhập 1 số nguyên 3 chữ số: ")
zero = "Không"
one = "Một"
two = "Hai"
three = "Ba"
four = "Bốn"
five = "Năm"
six = "Sáu"
seven = "Seven"
eight = "Tám"
nine = "Chín"
if len(so) >= 3:
    print("Chữ số hàng trăm là:", zero if so[0] == '0' else one if so[0] == '1' else two if so[0] == '2' else three if so[0] == '3' else four if so[0] == '4' else five if so[0] == '5' else six if so[0] == '6' else seven if so[0] == '7' else eight if so[0] == '8' else nine)
    print("Chữ số hàng chục là:", zero if so[1] == '0' else one if so[1] == '1' else two if so[1] == '2' else three if so[1] == '3' else four if so[1] == '4' else five if so[1] == '5' else six if so[1] == '6' else seven if so[1] == '7' else eight if so[1] == '8' else nine)
    print("Chữ số hàng đơn vị là:", zero if so[2] == '0' else one if so[2] == '1' else two if so[2] == '2' else three if so[2] == '3' else four if so[2] == '4' else five if so[2] == '5' else six if so[2] == '6' else seven if so[2] == '7' else eight if so[2] == '8' else nine)
else:
    print("Nhập lại")