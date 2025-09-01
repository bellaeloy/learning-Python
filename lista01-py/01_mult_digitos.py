#Escreva um progranumeroma que leia dois números inteiros N e X e diga depois de quantas multiplicações por 2 N fica com mais de X dı́gitos. Por exemplo: N=2, X=2 então depois de exatamente 6 multiplicações por 2 N fica com mais de X dı́gitos (N ∗ 2 ∗ 2 ∗ 2 ∗ 2 ∗ 2 ∗ 2 = 128)

input_num = [int(a) for a in input().split()]

numero = input_num[0]
digitos = input_num[1]

tam = str(numero)

while(len(tam) < digitos+1):
    temp = numero*2 #salvar em uma variavel temporaria
    numero = temp   #atualizar a variavel principal 
    tam = str(numero)   #transformar em string para contagem de digitos

print(numero)