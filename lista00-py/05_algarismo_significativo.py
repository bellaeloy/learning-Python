#Escreva um programa que receba dois numeros inteiros e imprima se eles tem o mesmo algarismo menos significativo. Por exemplo: o algarismo menos significativo do n ́umero 123  ́e o 3, entao o resultado seria Sim  para os n ́umeros 123 e 33, mas Nao para 123 e 32.

numeros = [int(a) for a in input().split()]

num1 = numeros[0]
num2 = numeros[1]

#algarismo menos significativo eh o resto da divisao por 10

if num1%10 == num2%10:
    print("Sim")
else:
    print("Não")