# Problema 1038 

item,qtdItem  = map(float,input().split(' '))

if (item == 1):
    precoTotal = 4.00 * qtdItem
elif (item == 2):
    precoTotal = 4.50 * qtdItem
elif (item == 3):
    precoTotal = 5.00 * qtdItem
elif (item ==4):
    precoTotal = 2.00 * qtdItem
elif(item == 5):
    precoTotal = 1.50 * qtdItem

print(f"Total : R$ {precoTotal:.2f}")