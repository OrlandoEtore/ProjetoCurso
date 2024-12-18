import cmath
n1=int(input('Number :'))

dobro  =n1*2
triplo =n1*3
raiz=cmath.sqrt(n1)  
r=pow(n1,0.5)
var =n1**(1/2)
print('Dobro :{}\nTriplo :{}\nRaiz Quadrada :{:.2f} {:.2f} {:.2f}'.format(dobro,triplo,raiz.real,r,var))