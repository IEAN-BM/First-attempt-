def calcul(x1,x2,y1,y2):
    w = x2-x1
    z = y2-y1
    q = ((w**2)+(z**2))*.5
    return q
x1 = eval(input('enter x1'))
x2 = eval(input('enter x2'))
y1 = eval(input('enter y1'))
y2 = eval(input('enter y2'))
print(calcul(x1,x2,y1,y2))