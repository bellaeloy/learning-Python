#5.1
car = 'sabaru'
print("Is car == 'sabaru'? I predict True")
print(car == 'sabaru')

print(" Is car == 'audi'? I predict False ")
print(car == 'audi')


#5.2
nome_completo = 'Edward Cullen'
print("Is Edward Anthony Cullen right? I predict False")
print(nome_completo == 'Edward Anthony Cullen')

print("Is Edward Cullen right? I predict True")
print(nome_completo == 'Edward Cullen')

nome_completo = 'EDWARD CULLEN'
print("Is edward cullen right? I predict False")
print(nome_completo.lower() == 'edward cullen')

her_age = 34
my_age = 31
print("Am i older than her? I predict False")
print(my_age > her_age)

print("Is she older than me? I predict True")
print(my_age > her_age)

print("Are we the same age?")
print(my_age == her_age)

fruits = ['banana', 'apple', 'kiwi']
print("Is banana in the fruits list?")
print('banana' in fruits)
print("Is banana and apple in the fruits list?")
print('banana' and 'apple' in fruits)
print("Is banana and mango in the fruits list?")
print('banana' and 'mango' in fruits)
print("Is banana or mango in the fruits list?")
print('mango' or 'banana' in fruits)
print("Is mango is not the fruits list?")
print('mango' not in fruits)

#5.3 alien colors#1
alien_color = 'red'
if alien_color == 'green':
    print("you won 5 points!")
else: 
    print("Sorry, you don't have the right color")

#5.4 alien colors#2
alien_color = 'green'
alien_color2 = 'purple'
if alien_color == 'green':
    print("you won 5 points for open fire!")
else: 
    print("You won 10 points!")

if alien_color2 == 'green':
    print("you won 5 points for open fire!")
else: 
    print("You won 10 points!")

#5.5
alien_color3 = 'yellow'
if alien_color3 == 'green':
    print("you won 5 points for open fire!")
elif alien_color3 == 'blue':
    print("You won 10 points!")
else: 
    print("You won 15 points!")

#5.6 which age
age = 40
if age < 2:
    print("Você é um neném")
elif age > 2 and age < 4:
    print("Você é uma criança")
elif age >= 4 and age < 13:
    print("Você é um(a) garoto(a)")
elif age >= 13 and age < 4:
    print("Você é um(a) adolescente(a)")
elif age >= 20 and age < 65:
    print("Você é um(a) adulto(a)")
elif age > 65:
    print("Você é um(a) idoso(a)")

#5.7 favorite fruit
favorite_fruits = ['banana', 'apple', 'kiwi']
if 'banana' in favorite_fruits:
    print('You really like banana')
if 'mango' in favorite_fruits:
    print('You really like mango')
if 'watermellon' in favorite_fruits:
    print('You really like watermellon')

#5.8 hello admin
users = ['carla', 'bob', 'leo', 'james', 'admin']
for name in users:
    if(name == 'admin'):
        print("Hello Jaden, thank you for being here again!")
    else:
        print(f"Welcome {name}!")

#5.9 empty list
users = []
if users == []:
    print("It is necessary find some users!")
else:
    for name in users:
        if name == 'admin':
            print("Hello Jaden, thank you for being here again!")
        else:
            print(f"Welcome {name}!")

#5.10 checking names
current_users = ['bella', 'manu', 'gabe', 'andrei', 'rafa']
new_users = ['nat', 'tony', 'thor', 'bella', 'manu']

for name in new_users:
    if name in current_users:
        print(f"{name}, you need a diffent name")
    else:
        print(f"{name} your name is available.")