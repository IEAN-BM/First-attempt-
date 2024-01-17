def fact(n):
    F = 1
    i = n
    while i>0:
        F = F*i
        i -= 1
    return F
n = int(input('enter a number'))
print(fact(n))