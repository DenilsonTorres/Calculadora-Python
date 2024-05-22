import os

calcular = []


class calculadora():
    n1 = n2 = 0

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2


def menu():
    os.system('cls') or None
    print("---Calculadora Python---")
    print("1  -  Adição")
    print("2  -  Subtração")
    print("3  -  Multiplicação")
    print("4  -  Divisão")
    opc = int(input("Digite a opção: "))
    return opc


def adicao():
    os.system('cls') or None
    print("---Adição---")
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    os.system('cls')
    resultado = x + y
    print("O resultado da adição é: "+str(resultado))
    os.system("pause")


def subtracao():
    os.system('cls') or None
    print("---Subtração---")
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    os.system('cls')
    resultado = x - y
    print("O resultado da subtração é: "+str(resultado))
    os.system("pause")


def multiplicacao():
    os.system('cls') or None
    print("---Multiplicação---")
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    os.system('cls')
    resultado = x * y
    print("O resultado da multiplicação é: "+str(resultado))
    os.system("pause")


def divisao():
    os.system('cls') or None
    print("---Divisão---")
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    os.system('cls')
    resultado = x / y
    print("O resultado da divisão é: "+str(resultado))
    os.system("pause")


ret = menu()

while ret < 5:
    if ret == 1:
        adicao()
    elif ret == 2:
        subtracao()
    elif ret == 3:
        multiplicacao()
    elif ret == 4:
        divisao()
    ret = menu()


os.system('cls') or None
os.system("pause")
