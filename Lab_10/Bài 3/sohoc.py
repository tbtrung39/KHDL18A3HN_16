def Ucln( a, b):
    if a< b:
        min= a
    else:
        min= b
    for i in range( 1, min+ 1):
        if a% i== 0 and b% i== 0:
            ucln= i
    print(" UCLN: ", ucln)
def Bcnn( a, b):
    if a< b:
        min= a
    else:
        min= b
    for i in range( 1, min+ 1):
        if a% i== 0 and b% i== 0:
            ucln= i
    bcnn= ( a* b)/ ucln
    print(" BCNN: ", bcnn)
def SumDivisor( n):
    tong= 0
    for i in range( 1, n+ 1):
        if n% i== 0:
            tong= tong+ i
    print(" Tổng những ước: ", tong)