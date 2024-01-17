from array import arr
def func(arr,n1,n2,element):
    for i in range (n1):
        for j in range (n2):
            if element == arr[i][j]:
                return arr[i][j],arr[i][j+1],arr[i][j+2]
n1 = eval(input('rowsize'))
n2 = eval(input('columnsize'))
for i in range (n1):
    for j in range(n2):
        arr[i][j] = arr.append(input('enter an element'))
element = eval (input('enter an element'))
print(func(arr,n1,n2,element))