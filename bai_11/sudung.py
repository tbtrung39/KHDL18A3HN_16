from doicoso import doicoso1 as a
from doicoso import doicoso2 as b

n = input('Nhap n = ')

nhi_phan = a.nhi_phan(n)
bat_phan = a.bat_phan(n)
thap_luc_phan = a.thap_luc_phan(n)

thap_phan = b.nhiphansangthapphan(n)
co_so_8 = b.batphansangthapphan(n)
co_so_16 = b.thaplucphansangthappahn(n)

print('Nhi phan:', nhi_phan)
print('Bat phan:', bat_phan)
print('Thap luc phan:', thap_luc_phan)

while b.loaibo(n):
    print('Day la:', b.chuoichotruoc(n))
    print('Co so 2 sang co so 10:', thap_phan)
    print('Co so 8 sang co so 10:', co_so_8)
    print('Co so 16 sang co so 10:', co_so_16)