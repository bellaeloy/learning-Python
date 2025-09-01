#Escreva um programa que receba, nesta ordem: nome, sobrenome, idade, altura em centı́metros, e tipo sanguı́neo de uma pessoa e imprima esses dados de maneira organizada seguindo o exemplo abaixo.

nome = input()
sobrenome = input()
idade = input()
altura = int(input())
tipo_sangu = input()

#separar digitos da altura
p1 = int(str(altura)[0])
p2 = int(altura)%100

#imprimir

print(f"Nome: {nome} {sobrenome}")
print(f"Idade: {idade} anos")
print(f"Altura: {p1}m{p2}")
print(f"Tipo sanguı́neo: {tipo_sangu}")



