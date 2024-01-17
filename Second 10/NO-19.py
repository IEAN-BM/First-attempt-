n = eval(input('enter the starting number'))
z = eval(input('number prime numbers after start'))
L = []
for i in range (0,z):
    L.append(0)
print(L)
count = 0
c = j = 0
if n == 1 or n == 2:
    L.insert(j,2)
    count = count + 1
    j = j +1
i = n
while(i<(n+15)):
    if count <= z:
        for z in range(0,i//2):
            if (i%(z+2) == 0):
                c = c+1
                break
        if c == 1:
            L.insert(j,i)
            count = count + 1
            j = j+1
    c = 0
    i = i + 1
print (L)
    