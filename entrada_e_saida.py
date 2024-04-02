def saudar_usuario():
    nome = input("Qual é o seu nome? ")
    print("Olá, ", nome, "! Seja bem-vindo(a)!")

def soma_numeros():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2
        print("A soma dos números fornecidos é:", soma)
    except:
        print("Entrada inválida")

def multiplica_numeros():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        produto = num1 * num2
        print("A multiplicação entre números fornecidos é:", produto)
    except:
        print("Entrada inválida")

saudar_usuario()
soma_numeros()
multiplica_numeros()