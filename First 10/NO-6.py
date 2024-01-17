x = 0
def fact(n):
    i = 1
    f = 1
    while(i<=n):
        f = f * i
        i = i+1
    return f
n = eval(input('enter a positive integer'))
print ('the factorial of',n,'is',fact(n))