#Reescreva novamente o programa acima para decidir se uma determinada pessoa pode ser candidata a doação de sangue. Uma pessoa é elegı́vel para doação de sangue se:
#(a) Tem entre 16 e 69 anos (se tem entre 60 e 69 anos, só poderá doar aquele que já o tenha feito antes dos 60 anos)
#(b) Pesa no mı́nimo 50Kg.


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


#separar digitos da altura para impressao
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

#verificar se pode doar sangue
if idade > 16 and idade < 60 and peso > 50:
    print("Pode doar sangue!")
elif idade >= 60 and idade <= 69 and peso > 50 and doou_sangue == "Sim" and idade_doacao < 60:
    print("Pode doar sangue!")
else:
    print("Não pode doar sangue!")

