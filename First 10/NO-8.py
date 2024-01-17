
def celtofah(temp):
    f = 1.8*temp+32
    return f

temp = eval(input('enter temperature in celcius'))
print ('In Fahrenheit, temperature =',celtofah(temp))