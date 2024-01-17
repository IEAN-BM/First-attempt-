frequencies = [ ]
L = []
#count = 0
s = input ('input a string')
L = list(s)
for i in L:
    frequencies.append(L.count(i))
print(frequencies)