#Reescreva mais uma vez o programa acima (prometo que é a última) para que receba, antes da informação do doador, uma linha com oito números inteiros representando a porcentagem de saturação de bolsas de sangue de cada tipo no banco de sangue local: A-, A+, B-, B+, AB-, AB+, O-, O+ respectivamente. Caso o banco de sangue esteja saturado de sangue (100%) do mesmo tipo do doador, ele não poderá doar
#dados dos tipos sanguineos
porcentagem_sangues = [int(a) for a in input().split()]
a1 = porcentagem_sangues[0] #A-
a2 = porcentagem_sangues[1] #A+
b1 = porcentagem_sangues[2] #B-
b2 = porcentagem_sangues[3] #B+
ab1 = porcentagem_sangues[4]    #AB-
ab2 = porcentagem_sangues[5]    #AB+
o1 = porcentagem_sangues[6] #O-
o2 = porcentagem_sangues[7] #O+


#dados do paciente
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

print(f"A-:{a1} | A+: {a2} | B-:{b1} | B+:{b2} | AB-: {ab1} | AB+: {ab2} | O-: {o1} | O+:{o2}")


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

#verificar a quantidade de sangue
if tipo_sangu == "A-" and a1 == 100:
    print("Não pode doar sangue!")
elif tipo_sangu == "A+" and a2 == 100:
    print("Não pode doar sangue!")
elif tipo_sangu == "B-" and b1 == 100:
    print("Não pode doar sangue!")
elif tipo_sangu == "B+" and b2 == 100:
    print("Não pode doar sangue!")
elif tipo_sangu == "AB-" and ab1 == 100:
    print("Não pode doar sangue!")
elif tipo_sangu == "AB+" and ab2 == 100:
    print("Não pode doar sangue!")
elif tipo_sangu == "O-" and o1 == 100:
    print("Não pode doar sangue!")
elif tipo_sangu == "O+" and o2 == 100:
    print("Não pode doar sangue!")
elif idade > 16 and idade < 60 and peso > 50: #verificar se pode doar sangue pelo peso e idade
    print("Pode doar sangue!")
elif idade >= 60 and idade <= 69 and peso > 50 and doou_sangue == "Sim" and idade_doacao < 60:
    print("Pode doar sangue!")
else:
    print("Não pode doar sangue!")