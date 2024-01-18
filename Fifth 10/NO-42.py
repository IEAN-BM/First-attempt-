x1 = x2 = y1 = y2 = 0
def circle(x1,x2,y1,y2,r1,r2):
    z = x2-x1
    y = y2-y1
    x = z**2+y**2
    w = x*.5
    if (w < (r1+r2)):
        return True
    else:
        return False
r1 = eval(input('enter radius for c1'))
r2 = eval(input('enter radius for c2'))
x1 = eval(input('enter first x coordinate'))
x2 = eval(input('enter second x coordinate'))
y1 = eval(input('enter first y coordinate'))
y2 = eval(input('enter second y coordinate'))
print(circle(x1,x2,y1,y2,r1,r2))
