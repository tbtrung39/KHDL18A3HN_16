def sum_recursive(n,result,current_sum,current_list):
    if current_sum==n:
        print(n,'=',current_list)
        return
    for i in range(1,n+1):
        if current_sum +1 <=n:
           sum_recursive(n,result,current_sum + i,current_list + [i])

n=int(input('nhap vao so tu nhen n:'))
sum_recursive(n,[],0,[])