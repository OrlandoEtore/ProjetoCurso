dia=int(input("Dias Usando o Carro :"))
km =float(input('Quilomentros Rodados :'))

soma = (dia * 60) + (km * 0.15)

print("Valor a Pagar : {:.2f}".format(soma))