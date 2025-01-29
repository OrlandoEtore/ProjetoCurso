import math 

a,b,c = map(float,input().split())

if (pow(b,2) - 4*a*c) > 0 and a !=0:
    r1 =(-b + math.sqrt(pow(b,2) - 4*a*c)) /(2*a)
    r2 =(-b - math.sqrt(pow(b,2)) - 4 *a*c) /(2*a)

    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
else :
    print("Impossivel Calcular")