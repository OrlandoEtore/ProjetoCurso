
'''
import math
ang =float(input())

r= math.radians(ang)

cossine=math.acos(r)
sine=math.asin(r)
tangente=math.atan(r)   
                                                                                  
print(f'{cossine} {sine} {tangente}')
'''

import math

ang  =float(input("Digite o angulo :"))

rad= math.radians(ang)

seno = math.asin(rad)
cons = math.acos(rad)
tang = math.atan(rad)

print('SENNO : {:.2f} COSSENO :{:.2f} TANGENTE :{:.2f}'.format(seno,cons,tang))

