#Escreva um programa que receba dois numeros de ponto flutuante A, B (B ̸= 0) e imprima a soma, produto, e divis ̃ao (A/B) deles.

num = [float(a) for a in input().split()]

#operacoes
divisao = num[0]/num[1]
soma = num[0]+num[1]
produto = num[0]*num[1]

print(f"Soma: {soma:.2f}")
print(f"Produto: {produto:.2f}")
print(f"Divisão: {divisao:.2f}")
