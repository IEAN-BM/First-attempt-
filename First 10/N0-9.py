def celtofah(temp):
    c = (temp-32)/1.8
    return c

temp = eval(input('enter temperature in Fahrenheit'))
print ('In Celcius, temperature =',celtofah(temp))