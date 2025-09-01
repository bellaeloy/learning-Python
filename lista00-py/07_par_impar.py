#Escreva um programa que receba um n ́umero 0 ≤N ≤1000 e diga se ele e par ou ́ımpar.

num = int(input())

#verificar se está no intervalo
if num<0 or num>1000:
    print("Valor inválido. x>0 e x<1000")

elif num%2 == 0:
    print("Par")
else:
    print("Ímpar")
