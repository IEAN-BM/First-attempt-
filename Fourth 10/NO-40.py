L = []
def bubblesort(L,n):
    small = 0
    for i in range(0,len(L)):
        for j in range (1,len(L)):
            if L[j-1]>L[j]:
                small = L[j-1]
                L[j-1] = L[j]
                L[j] = small
    return L
n = eval(input('enter list size'))
for i in range(0,n):
    L.append(input('enter an element'))
print(bubblesort(L,n))