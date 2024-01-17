L = []
S = []
dist = 0
i = 2
count = 1
c = 0
while (i<1000):
    if count <= 100:
        for z in range(0,i//2):
            if (i%(z+2) == 0):
                c = c + 1
        if c == 0:
            count = count + 1
        c = 0
    else:
        dist = (i-1)-2
        break
    i += 1
print (dist)