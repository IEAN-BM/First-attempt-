n = eval (input ('enter value of timetable'))
num = 0
for i in range (10) :
    num = (i+1) * n
    print ('%d * %d = %d'%(i+1,n,num))
