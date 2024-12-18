# bibloteca para aleatorio
import random 

a = input("Aluno 1:")
b = input("Aluno 2:")
c = input("Aluno 3:")
d = input("Aluno 4:")

#lista com os nomes
nomes = [a,b,c,d]

#funcao da bibloteca que pega a lista e faz o sorteio de maneira aleatorio do nome do aluno 
sortiado = random.choice(nomes)

print(sortiado)