def creat_listA(n):
    listA=[]
    for i in range(n):
        number =int(input('nhap so nguyen:'))
        listA.append(number)
    return listA

def insert_recursive(list,value,index):
    if index==0:
        return [value]+ listA
    else:
        return [listA[0]] + insert_recursive(listA[:1],value,index-1)

n=int(input('nhap so muon chen:'))
listA=creat_listA(n)
print('listA ban dau:',listA)

x=int(input('nhap so muon chen:'))
k=int(input('nhap vi tri muon chen:'))
listA=insert_recursive(listA,x,k)
print('listA sau khi chen:',listA)