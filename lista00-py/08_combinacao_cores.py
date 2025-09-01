#Escreva um programa que receba duas cores prim ́arias e imprima o resultado da mistura delas.
#vermelho | amarelo | azul


cores = [(a) for a in input().split()]

cor1 = cores[0]
cor2 = cores[1]

#Laranja
if (cor1 == 'Vermelho' and cor2 == 'Amarelo') or (cor1 =='Amarelo' and cor2 == 'Vermelho'):
    print('Laranja')
elif (cor1 == 'Amarelo' and cor2 == 'Azul') or (cor1 =='Azul' and cor2 == 'Amarelo'):
    print('Verde')
elif (cor1 == 'Azul' and cor2 == 'Vermelho') or (cor1 =='Vermelho' and cor2 == 'Azul'):
    print('Roxo')
else:
    print('Cores inválidas')