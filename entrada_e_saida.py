def saudar_usuario():
    """
    Crie uma função que pede o nome do usuário e o imprime com uma saudação. Ao final desta tarefa faça um commit “Resolve questão 1”no repositório remoto.
    Exemplo de resultado: "Olá, [nome do usuário]! Seja bem-vindo(a)!"
    """
    nome = input("Qual é o seu nome? ")
    print("Olá, ", nome, "! Seja bem-vindo(a)!")

def soma_numeros():
    """
    Crie uma função que pede dois números, faz a soma deles e imprime o resultado. Ao final desta tarefa faça um commit no repositório remoto.
    Exemplo de saída: "A soma dos números é: [resultado] "
    """
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2
        print("A soma dos números é: ", soma)
    except:
        print("Entrada inválida")

def multiplica_numeros():
    """
    Crie uma função que pede dois números, faz a multiplicação deles e imprime o resultado. Ao final desta tarefa faça um commit no repositório remoto.
    Exemplo de saída: "O produto dos números é: [resultado] "
    """
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        produto = num1 * num2
        print("O produto dos números é: ", produto)
    except:
        print("Entrada inválida")

def divide_numero():
    """
    Crie uma função que pede um número, divide por 2 e imprime o resultado. Ao final desta tarefa faça um commit no repositório remoto.
    Exemplo de saída: "A divisão do número [numero] por dois é: [resultado] "
    """
    try:
        num = float(input("Digite um número: "))
        resultado = num / 2
        print("A divisão do número {} por dois é: {}".format(num, resultado))
    except:
        print("Entrada inválida")

def calcula_imc():
    """
    Crie uma função que pede a altura e o peso do usuário, calcula o seu IMC e imprime o resultado. Ao final desta tarefa faça um commit no repositório remoto.
    dica: O cálculo do IMC é: peso/(altura x altura).
    Exemplo de saída: "O seu IMC é: [resultado] "
    """
    try:
        altura = float(input("Digite sua altura: "))
        peso = float(input("Digite seu peso: "))
        imc = peso/(altura*altura)
        print("O seu IMC é: ", imc)
    except:
        print("Entrada inválida")

saudar_usuario()
soma_numeros()
multiplica_numeros()
divide_numero()
calcula_imc()