#3.1
friends = ['manu', 'rafa', 'andrei', 'erivan']
for friend in friends:
    print(friend)

#3.2
for friend in friends:
    print (f"{friend} eu amo você!")

#3.3
carros_legais = ['hrv', 'volvo xc60', 'bmw', 'audi']
for carro in carros_legais:
    print(f"eu adoraria ter um {carro}")

#3.4
pessoas_queridas = ['vovó','elis','gabriel']
for pessoa in pessoas_queridas:
    print(f"Oi {pessoa}, gostaria de jantar comigo?")
#3.5
    print("A vovó não vai")

#3.6
pessoas_queridas.insert(0,'manu')
pessoas_queridas.append('mainha')
pessoas_queridas.insert(2, 'titia')

for pessoa in pessoas_queridas:
    print(f"{pessoa}, o jantar está esfriando!")

#3.7
print("\n")
print(pessoas_queridas)
print("Infelizmente só poderei convidar duas pessoas")

while len(pessoas_queridas) > 2:
    ultima_pessoa = pessoas_queridas.pop()
    print(f"Oi {ultima_pessoa}, infelizmente não poderei levar você")

while len(pessoas_queridas) > 0:
    del pessoas_queridas[0]

print(pessoas_queridas)

#3.8
print("\n")
lugares = ["china", "barcelona", "londres", "madrid"]
print(lugares)
print(sorted(lugares))
print(lugares) #inalterada
print(sorted(lugares, reverse=True))
print(lugares) #inalterada
lugares.reverse()
print(lugares) #alterada
lugares.sort()
print(lugares) #alterada
lugares.sort(reverse=True)
print(lugares) #alterada

#3.9
print("\n")
print(f"Quero viajar para {len(lugares)} lugares!")

#3.10
print("\n")
comidas_deliciosas = ['bolo', 'sorvete', 'lasanha', 'pipoca', 'pão de queijo']

for comida in comidas_deliciosas:
    print(f"Mãe, tem {comida}?")

comidas_deliciosas.append('pamonha')
print(comidas_deliciosas)

comidas_deliciosas.insert(2, 'chocolate')
print(comidas_deliciosas)

print(sorted(comidas_deliciosas)) #nao altera a lista
print(sorted(comidas_deliciosas, reverse=True)) #nao altera a lista

comidas_deliciosas.sort()
print(f"em ordem alfabética: {comidas_deliciosas}")

comidas_deliciosas.sort(reverse=True)
print(f"em ordem alfabética contrária: {comidas_deliciosas}")


while len(comidas_deliciosas) > 2:
    comida = comidas_deliciosas.pop()
    print(f"Vou parar de comer {comida}")
    print(comidas_deliciosas)

#3.11 - erro de índice intencional
print(comidas_deliciosas[8])