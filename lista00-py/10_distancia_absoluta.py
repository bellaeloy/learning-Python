#Escreva um programa que receba dois inteiros e retorne a distancia absoluta entre eles. A distancia absoluta entre dois numeros A, B  ́e dada como |A −B

numeros = [int(a) for a in input().split()]

num1 = numeros[0]
num2 = numeros[1]

print(abs(num1-num2))