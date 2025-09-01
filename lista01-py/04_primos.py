#Escreva um programa que receba um número inteiro 1 ≤ N ≤ 10000 e diga se ele é primo. Um número é primo se ele é divisı́vel apenas por 1 ou por ele mesmo, com exceção dos números 0 e 1, que por definição são considerados não primos.
import math

num = int(input())

def ehPrimo(num):
    num_sqrt = math.sqrt(num)

    for i in range(2, int(num_sqrt)+1):
        if num%i == 0:
            print("Não é primo")
            return # se entrar na condição, já para de rodar
    
    print("Primo")

ehPrimo(num)