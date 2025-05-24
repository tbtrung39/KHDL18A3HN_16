n=int(input('Nhap so tu nhien n:'))
A={i for i in range(2,n+1)if n%i==0 and (i%j !=0 for j in range(2,int(i**0.5)+1))}
B={i for i in range(2,n) if (i%j !=0 for j in range(2,int(i**0.5)+1)) and i not in A}
print('Tap hop A la uoc cua n:', A)
print('Tap hop B la so nho hon n:',B)