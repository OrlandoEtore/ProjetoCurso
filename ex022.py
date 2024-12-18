import string

nome = input('')
mai = nome.upper()
mins = nome.lower()
sesp =nome.replace(' ','')

pnome = nome.split()[0]

print(' Maisculo {}\n Misculo {}\n Sem Espaco {}\n Tamanho da string sem espaco {} \n Primeiro Nome {}\n Tamanho letras Primeiro Nome {}'.format(mai,mins,sesp,len(sesp),pnome,len(pnome)))

"""
nome = str(input()).strip()

print('Maiscula {}'.format(nome.upper()))
print('Miscula {}'.format(nome.lower()))
print('Letras Ao Todo {}'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Primeiro Nome {} e ele tem {} letras'.format(separa[0],len(separa[0])))

"""