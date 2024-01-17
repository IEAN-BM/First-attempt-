List = [0,1,1,0,0,0,0,0,0,0]
i = 3
while (i<10):
    List[i] = List[i-1] + List[i-2]
    i = i + 1
print(List)