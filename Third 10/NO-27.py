L = []
n = eval(input('enter range'))
def square(L):
    L = [i*2 for i in L]
    return L
for i in range(0,n):
    L.append(input('enter a value'))
print(square(L))