c1 = [2,3]
c2 = [4,5]
def circle(c1,c2,r1,r2):
    z = c2[:-1]-c1[:-1]
    y = c2[:-2]-c1[:-2]
    x = z**2+y**2
    w = x*.5
    if (w < (r1+r2)):
        return True
    else:
        return False
r1 = eval(input('enter radius for c1'))
r2 = eval(input('enter radius for c2'))
print(circle(c1,c2,r1,r2))