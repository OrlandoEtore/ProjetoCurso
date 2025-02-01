def maior(a, b):
    return int((a + b + abs(a - b)) / 2)

a, b, c = map(int, input().split())

# Calculando o maior número
maior_ab = maior(a, b)
maior_abc = maior(maior_ab, c)

print(f'{maior_abc} eh o maior')