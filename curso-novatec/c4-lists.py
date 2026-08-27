#4.1
pizzas = ['calabresa', 'portuguesa', 'chocolate']
for pizza in pizzas:
    print(f"Gosto de pizza de {pizza}")
print("Eu amo pizza!")

#4.2
print("\n")
animais_voam = ['morcego', 'gavião', 'codorna', 'bem-te-vi']
for animal in animais_voam:
    print(f"O {animal} voa muito bem!")
print("Todos eles voam muito bem!")

#4.3
nums = range(1,21)
for num in nums:
    print(num, end = " ")

#4.4
nums2 = range(1, 10)
for num in nums2:
    print(num, end = " ")

#4.5
print("\n")
print(f"O mínimo eh: {min(nums2)}")
print(f"O máximo eh: {max(nums2)}")
print(f"O somatório eh: {sum(nums2)}")

#4.6
print("\n")
nums_impares = range(1,21,2)
for num in nums_impares:
    print(num)

#4.7
print("\n")
nums_mult_3 = range(3,30,3)
for num in nums_mult_3:
    print(num)

#4.8
print("\n")
cubos = range(1,11)
for num in cubos:
    print(num**3)

#4.9
cubes = [value**3 for value in range(1,11)]
print(cubes)

#4.10 - fatias
print(f"Os três primeiros cubos são: {cubes[:3]}")

animal_meio = len(animais_voam) // 2
print(f"Os três animais do meio são: {animais_voam[animal_meio-1:animal_meio+2]}")
print(f"Os três animais finais são: {animais_voam[-3:]}")

#4.11
gabriel_pizzas = pizzas[:]
print(gabriel_pizzas)
gabriel_pizzas.append('estrogonofe')
print(gabriel_pizzas)

print("Minhas pizzas favoritas são:")
for pizza in pizzas:
    print(pizza, end = ' ')

print("A pizzas favoritas de Gabriel são:")
for pizza in gabriel_pizzas:
    print(pizza, end = ' ')

#4.13 - turpla
print("\n")
menu = ('feijão', 'arroz', 'frango', 'bife', 'purê')
for comida in menu:
    print(comida)

#menu[1] = 'peixe' #o python n permite mudanca de turpla

menu = ('peixe', 'arroz', 'bisteca', 'bife', 'purê')
for comida in menu:
    print(comida)