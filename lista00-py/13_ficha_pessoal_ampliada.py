#Reescreva o programa anterior para receber, também, as seguintes informações:
#(a) Já doou sangue antes? (se sim, também receba a idade que a pessoa tinha quando começou a doar sangue).
#(b) Peso em Kg.
#(c) Almoçou há mais de duas horas?

nome = input()
sobrenome = input()
idade = int(input())
altura = int(input())
tipo_sangu = input()
doou_sangue = input()
if doou_sangue == "Sim":
    idade_doacao = int(input())
peso = int(input())
almocou = input()


#separar digitos da altura
p1 = int(str(altura)[0])
p2 = int(altura)%100

#imprimir

print(f"Nome: {nome} {sobrenome}")
print(f"Idade: {idade} anos")
print(f"Altura: {p1}m{p2}")
print(f"Tipo sanguı́neo: {tipo_sangu}")
print(f"Já doou sangue antes: {doou_sangue}")
if doou_sangue == "Sim":
    print(f"Idade na primeira doação: {idade_doacao}")
print(f"Peso: {peso}Kg")
print(f"Almoçou há mais de duas horas: {almocou}")







