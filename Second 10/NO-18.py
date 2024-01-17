i = 2
count = 1
c = 0
print (2)
while (i<200):
    if count < 100:
        for z in range(0,i//2):
            if (i%(z+2) == 0):
                c = c + 1
        if c == 0:
            print (i)
            count = count + 1
        c = 0
    i += 1
