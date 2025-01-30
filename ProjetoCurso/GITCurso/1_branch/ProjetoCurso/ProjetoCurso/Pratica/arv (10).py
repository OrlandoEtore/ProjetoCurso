import math

a,b,c = map(float, input().split())

triangulo = a*c / 2
circulo = c **2 * math.pi
trapezio = (a+b) * c /2
quadrado = b **2
retangulo = a *b 
print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
printf(f'TRAPEZIO: {trapezio:.3f}')
printf(f'QUADRADO: {quadrado:.3f}')
printf(f'RETANGULO: {retangulo:.3f}')