def is_TamGiac( a, b, c):
    if a+ b> c or a+ c> b or b+ c> a:
        return True
    else:
        return False
def ChuviTamGiac( a, b, c):
    return a+ b+ c
def S_TamGiac( a, b, c):
    p= ( a+ b+ c) / 2
    return ( p* ( p- a) * ( p- b) * ( p- c)) ** 1/ 2