#Escreva um programa que calcule o MMC de uma terna de números.

n1 = int(input())
n2 = int(input())
n3 = int(input())

def mdc(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1%num2 #formula de euclides para calculo de mdc
    return num1

def mmc(num1, num2):
    mmc = num1 * num2 // mdc(num1, num2) #formula para achar o mmd a partir do mdc
    return mmc

#funcao para o calculo de tres numeros
def mmc_tres_num(num1, num2, num3):
    return mmc(mmc(num1, num2), num3)

#chamar a funcao
print(mmc_tres_num(n1, n2, n3))