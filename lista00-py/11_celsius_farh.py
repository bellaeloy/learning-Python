#Escreva um programa que receba um float −459.67 ≤ T ≤ 10000 representando uma temperatura em graus Fahrenheit e imprima a temperatura em Celcius e Kelvin. A conversão de graus Celcius para Kelvin é: K = C + 273.15. A fórmula para conversão de graus Fahrenheit para Celcius é: C = (F − 32) ∗ 5/9. Obs: Imprima o resultado arredondado para exatamente duas casas decimais após a vı́rgula.

tempF = float(input())

tempC = (tempF-32)*5/9
tempK = tempC+273.15

print(f"Celcius: {tempC:.2f}")
print(f"Kelvin: {tempK:.2f}")
