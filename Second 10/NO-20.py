List = [1,2,3,4,5,6,7]
L = []
for i in range (0, len(List)):
    L.append(0)
s = len(List)
i = 0
L[0:-1] = List[1:]
L[-1] = List[0]
print(L)
    
