def count_characters_recursive(string,count):
    if not string:
        return count
    if string[0].isalpha():
        count['alphabet']+1
    elif string[0].isdigit():
        count['digit']+=1
    else:
        count['special']+=1
    return count_characters_recursive(string[1:],count)
string=input('nhap mot chuoi ky tu:')
count={'alphabet':0,'digit':0,'special':0}
count=count_characters_recursive(string,count)
print('so luong cac ky tu chu cai:',count['alphabet'])
print('so luong ky tu cac chu so:',count['digit'])
print('so luong cac ky tu dac biet:',count['special'])