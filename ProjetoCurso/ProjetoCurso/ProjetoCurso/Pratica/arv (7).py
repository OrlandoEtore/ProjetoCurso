nome = input()
salario = float(input())
totalvendas = float(input())

totalRecebido = salario + (totalvendas *0.15)

print(f'TOTAL = R$ {totalRecebido:.2f}')