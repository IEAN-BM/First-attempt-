from random import randint
List = []
def random(n):
    for i in range(0,n):
        List.append(randint(1,n))
    return List
n = int(input('enter range'))
print(random(n))