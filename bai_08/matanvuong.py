def matran1(n):
    matrix = [[i for i in range(n)] for j in range(n)]
    return matrix

def matran2(n, m):
    matrix = [[i for i in range(n)] for j in range(m)]
    return matrix

def chuyenvi(n):
    matrix = [[i[j] for i in matran1(n)] for j in range(len(matran1(n)[0]))]
    return matrix

