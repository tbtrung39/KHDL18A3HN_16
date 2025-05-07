#Bài 12:
def tim_nghiem(so_ga, so_cho):
    if so_ga + so_cho == 36 and 2 * so_ga + 4 * so_cho == 100:
        print(f"Số gà: {so_ga}, số chó: {so_cho}")
        return
    if so_ga + so_cho > 36 or 2 * so_ga + 4 * so_cho > 100:
        return
    tim_nghiem(so_ga + 1, so_cho)
    tim_nghiem(so_ga, so_cho + 1)

tim_nghiem(0, 0)