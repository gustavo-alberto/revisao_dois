"""
Crie uma função que simula uma calculadora simples, onde o usuário pode escolher as operações: soma, subtração, multiplicação e divisão. Ao final faça um commit no GitHub. 
- A função deve imprimir um menu com as opções disponíveis.
- A função solicita dois números: o primeiro número e o segundo número.
- Ao final da função deve imprimir o resultado.
"""

def get_numbers():
    """
    Solicita ao usuário dois numeros e retorna uma tupla.

    Returns:
        numbers: tupla que armazena os dois valores digitados pelo usuário.
    """
    try:
        number1 = float(input("Digite o primeiro número: "))
        number2 = float(input("Digite o segundo número: "))
        numbers = (number1, number2)
        return numbers
    except:
        print("Entrada inválida!")
        get_numbers()

def show_result(operation, number1, number2, result):
    """
    Exibe na tela os dois números fornecidos e o resultado.

    Args:
        operation (string): Operação que foi realizada.
        number1 (float): O primeiro número.
        number2 (float): O segundo número.
        result (float): O resultado da operação.
    """
    print("A {} de {:g} por {:g} é: {:g}".format(operation, number1, number2, result))

def operation_header(operation):
    """
    Exibe um cabeçalho na chamada da função de operação

    Args:
        operation (string): Operação que será realizada
    """
    print("--------- {} ---------".format(operation))

def sum():
    """
    Realiza soma entre dois números e mostra o resultado na tela
    """
    operation_header("Soma")
    numbers = get_numbers()
    result = numbers[0] + numbers[1]
    show_result("soma", numbers[0], numbers[1], result)

def subtraction():
    """
    Realiza subtração entre dois números e mostra o resultado na tela
    """
    operation_header("Subtração")
    numbers = get_numbers()
    result = numbers[0] - numbers[1]
    show_result("subtração", numbers[0], numbers[1], result)

def multiplication():
    """
    Realiza multiplicação entre dois números e mostra o resultado na tela
    """
    operation_header("Multiplicação")
    numbers = get_numbers()
    result = numbers[0] * numbers[1]
    show_result("multiplicação", numbers[0], numbers[1], result)

def division():
    """
    Realiza divisão entre dois números e mostra o resultado na tela
    """
    operation_header("Divisão")
    numbers = get_numbers()
    try:
        result = numbers[0] / numbers[1]
        show_result("divisão", numbers[0], numbers[1], result)
    except ZeroDivisionError:
        print("Impossível dividir por zero")
        division()

def menu():
    print("--------------------------------")
    print("Calculadora simples")
    print("--------------------------------")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    print("--------------------------------")
    
    try:
        option = int(input("Digite a opção desejada: "))
        if option == 1:
            sum()
        elif option == 2:
            subtraction()
        elif option == 3:
            multiplication()
        elif option == 4:
            division()
        elif option == 0:
            print("Obrigado por utilizar a calculadora")
            print("\n")
        else:
            raise Exception
    except:
        print("Opção inválida")
        print("\n")

menu()