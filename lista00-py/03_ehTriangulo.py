#Escreva um programa que receba tres numeros inteiros representando comprimentos de tres segmentos de reta e diga se eles podem formar um triangulo. Tres segmentos de reta de comprimentos A, B, C formam um triangulo se e somente se a soma de quaisquer dois deles ́e maior que o terceiro

#OPC 1 numeros = list(map(int, input("Digite os tamanhos separados por espaço e direi se formam um triângulo:").split()))

# opc2
numeros = [int(a) for a in input().split()] # list comprehension 

a = numeros[0]
b = numeros[1]
c = numeros[2]

if (a+b > c and b+c > a and c+b > a):
    print("Formam um triângulo")
else:
    print("Não formam um triângulo")