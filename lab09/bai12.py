def tim_ga_cho(ga=0):
    cho = 36 - ga  
    if ga > 36:
        return
    if ga * 2 + cho * 4 == 100:
        print(f"Gà: {ga}, Chó: {cho}")
    # Gọi đệ quy với số gà tăng lên
    tim_ga_cho(ga + 1)
tim_ga_cho()

