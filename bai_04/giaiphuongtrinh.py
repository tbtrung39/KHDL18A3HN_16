import math

def ptb1(a, b):
    if a == 0:
        return 'Vo nghiem'
    else:
        x = -b / a
        return x

def ptb2(a, b, c):
    if a == 0:
        ptb1(b, c)
    elif b == 0:
        x = math.sqrt(-c / a)
        if ValueError:
            print("Vo nghiem")
        else:
            print('Nghiem cua PTB2 la:', x)
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print('Vo nghiem')
        elif delta == 0:
            print('Nghiem kep:')
            x1 = x2 = -b/(2*a)
            print(x1, ',', x2)
        else:
            print('Co 2 nghiem:')
            x1 = (-b - math.sqrt(delta))/(2 * a)
            x2 = (-b + math.sqrt(delta))/(2 * a)
            print(x1, ',', x2)