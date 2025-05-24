def kiem_tra_doi_xung(chuoi):
    if len(chuoi) <= 1:
        return True
    if chuoi[0] != chuoi[-1]:
        return False
    return kiem_tra_doi_xung(chuoi[1:-1])
chuoi = input("Nhap mot chuoi: ")
chuoi = chuoi.replace(" ", "").lower()
if kiem_tra_doi_xung(chuoi):
    print("Chuoi doi xung.")
else:
    print("Chuoi khong doi xung.")