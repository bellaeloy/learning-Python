# Escreva um programa que receba quatro numeros de ponto flutuante, dois em uma linha e dois na segunda linha, representando coordenadas x,y (respectivamente) de dois pontos e calcule a distˆancia euclidiana entre eles
import math

ponto1 = [float(a) for a in input().split()] 
ponto2 = [float(a) for a in input().split()]


x1 = ponto1[0]
y1 = ponto1[1]
x2 = ponto2[0]
y2 = ponto2[1]

distancia_euclidiana = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

print(f"Distancia Euclidiana é: {distancia_euclidiana:.2f}") #formatado duas casas decimais