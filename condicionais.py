def verificar_maioridade():
    """
    Crie uma função para verificar se a pessoa é maior de 18 anos. Se for maior, imprima “Maior de idade”, se for menor imprima “Menor de idade”. Ao final faça um commit no GitHub. Exemplo de entrada: 17 Exemplo de saída: “Menor de idade”
    """
    try:
        idade = int(input("Qual é a sua idade? "))
        if (idade >= 18):
            print("Maior idade")
        else:
            print("Menor idade")
    except:
        print("Entrada inválida")

def verifica_par_impar():
    """
    Crie uma função que verifica se um número digitado pelo usuário é par ou ímpar. Ao final faça um commit no GitHub.
    Exemplo de entrada: 11 Exemplo de saída: "O número é ímpar."
    """
    try:
        num = int(input("Digite um número: "))
        if ((num%2) == 0):
            print("O número é par")
        else:
            print("O número é impar")
    except:
        print("Entrada inválida")

verificar_maioridade()
verifica_par_impar()