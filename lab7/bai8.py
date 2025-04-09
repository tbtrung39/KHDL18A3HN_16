A="150512032006dtbtak@#"
count_number=0
count_word=0
for i in set(A):
    if '0' <=i <= '9':
        count_number+=1
    else:
        if 'a'<= i <= 'z':
            count_word+=1
print("So nguyen la:", count_number)
print("So ky tu la:", count_word)