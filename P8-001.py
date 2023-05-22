''' # 1. Escreva um programa que preencha duas matrizes (A e B), 
ambas de ordem 2x3, com valores inteiros fornecidos pelo usuário 
(ou gerados aleatoriamente). O programa deverá somar as duas matrizes, 
armazenando o resultado em uma terceira matriz (C). Ao final, exiba as 3
matrizes (no formato de matriz).'''
#definição da ordem das matrizes(variáveis):
nlin = 2
ncol = 3
# inicialização das matrizes:

a = []
for i in range(nlin):
    a.append([0]*ncol)
b = []
for i in range(nlin):
    b.append([0]*ncol)
c = []
for i in range(nlin):
    c.append([0]*ncol)

#leitura das matrizes:
print('Digite a matriz A: ')
for i in range(nlin):
    for j in range(ncol):
        a[i][j] = int(input())

print('Digite a matriz B: ')
for i in range(nlin):
    for j in range(ncol):
        b[i][j] = int(input())

#Calculo da matriz C = A + B

for i in range(nlin):
    for j in range(ncol):
        c[i][j] = a[i][j] + b[i][j]

# Impressão das matrizes:
print('Matriz A: ')
for i in range(nlin):
    for j in range(ncol):
        print(a[i][j], end=" ")#end vai colocar os valores um do lado do outro
    print()#quebra a linha

print('Matriz B: ')
for i in range(nlin):
    for j in range(ncol):
        print(b[i][j], end=" ")#end vai colocar os valores um do lado do outro
    print()

print('Matriz C: ')
for i in range(nlin):
    for j in range(ncol):
        print(c[i][j], end=" ")#end vai colocar os valores um do lado do outro
    print()

