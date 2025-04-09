n=int(input('nhap so tu nhien n:'))
A={i for i in range(2,n+1)if n%i==0 and all(i%j !=0 for j in range(2,int(i**0.5)+1))}
B={i for i in range(2,n)if all(i%j !=0 for j in range(2,int(i**0.5)+1)) and i not in A}
print('tap hop A la uoc cua n:',A)
print('tap hop B la so nho hon n va khong la uoc cua A:',B)