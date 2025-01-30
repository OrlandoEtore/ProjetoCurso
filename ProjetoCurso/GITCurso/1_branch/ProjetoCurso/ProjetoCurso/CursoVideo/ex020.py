# bibloteca para aleatorio
import random 


a = input("Aluno 1:")
b = input("Aluno 2:")
c = input("Aluno 3:")
d = input("Aluno 4:")

#lista com os nomes
nomes = [a,b,c,d]

#essa funcao faz pegar os nomes de forma aleatorio e depois colocar um rank de ordem 
random.shuffle(nomes)
print(nomes)