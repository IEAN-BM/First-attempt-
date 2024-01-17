array = []
List = [0,0,1]
z = 0
n = eval(input('enter limit'))
for i in range(0,n):
    array.append(input('enter a number'))
for i in range(0,len(array)):
    z = array[i] + List[-1]
    if (z < 0):
        del array[i]
print (array[i])