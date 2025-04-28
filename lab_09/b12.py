def solve(x, y):
    if x + y == 36 and 2*x + 4*y == 100:
        print(f"Số gà: {x}, số chó: {y}")
        return
    if x + y > 36 or 2*x + 4*y > 100:
        return
    solve(x+1, y)
    solve(x, y+1)

solve(0, 0)