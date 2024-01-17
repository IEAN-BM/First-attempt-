def boolean(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range (0,n//2):
            if (n%(i+2) == 0):
                return False
            break
        return True
n = eval(input('enter a number'))
s = boolean(n)
if s == True:
    print('Number is prime')
else:
    print('number is not prime')
            
        