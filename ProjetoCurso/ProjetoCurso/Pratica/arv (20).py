
valor = float(input())
valor = int(valor*100)

# NOTAS
nota100 = valor//10000
valor %= 10000

nota50 = valor//5000
valor %= 5000

nota20 = valor//2000
valor %= 2000

nota10 = valor//1000
valor %=1000

nota5 = valor//500
valor %=500

nota2 = valor//200
valor %=200

#MOEDAS
moeda100 = valor //100
valor %= 100

moeda50 = valor//50
valor %=50

moeda25 = valor//25
valor %=25

moeda10 = valor//10
valor %=10

moeda5 = valor//5
valor %=5

moeda1 = valor

print('NOTAS:')
print(f'{nota100} nota de $ 100')
print(f'{nota50} nota de R$ 50')
print(f'{nota20} notas R$ 20')
print(f'{nota10} notas R$ 10')
print(f'{nota5} notas R$ 5')
print(f'{nota2} notas R$ 2')

print("MOEDAS:")
print(f'{moeda100} moeda de R$ 1')
print(f'{moeda50} moeda de R$ 0.50')
print(f'{moeda25} moeda de R$ 0.25')
print(f'{moeda10} moeda de R$ 0.10')
print(f'{nota5} moeda de R$ 0.05')
print(f'{moeda1} moeda de R$ 0.01')