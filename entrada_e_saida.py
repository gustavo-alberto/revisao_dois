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

def divide_numero():
    try:
        num = float(input("Digite um número: "))
        resultado = num / 2
        print("A divisão do número {} por dois é: {}".format(num, resultado))
    except:
        print("Entrada inválida")

saudar_usuario()
soma_numeros()
multiplica_numeros()
divide_numero()