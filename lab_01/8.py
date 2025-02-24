xa, ya = map(float, input("nhập đỉnh A: ").split())  
xb, yb = map(float, input("nhập đỉnh B: ").split())  
xc, yc = map(float, input("nhập đỉnh C: ").split())  
xg = (xa+xb+xc)/3  
yg = (ya+yb+yc)/3  
print("trọng tâm tam giác là: ",round(xg,2),round(yg,2))