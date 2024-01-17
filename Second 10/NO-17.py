sum = 0
n = eval(input('enter an nteger'))
if (n>0 and n<10):
    print ('n is a single digit number',n)
else:
    z = n//10
    x = n-(z*10)
    sum = sum + z + x
    print ('sum of n digits gives', sum)
