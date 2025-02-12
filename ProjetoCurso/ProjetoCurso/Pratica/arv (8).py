
codigoA,quantidadeA,valorA = map(float,input().split())
codigoB,quandtidadeB,valorB = map(float,input().split())

custoA = quantidadeA * valorA
custoB = quandtidadeB * valorB

print(f'VALOR A PAGAR: R$ {(custoA + custoB):.2f}')