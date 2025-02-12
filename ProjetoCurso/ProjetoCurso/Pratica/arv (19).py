
dia = int(input())

ano = dia//365
dia = dia%365

meses = dia //30
dia = dia %30

print(f'{ano} anos(s)\n{meses} mes(es)\n{dia} dia(s)\n')