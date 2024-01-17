def convert(s):
    List = []
    i = j = 0
    S = list(s)
    for i in S:
        List[j] = bin(i)
        j = j+1
    return List
s = input('enter a string')
print(convert(s))