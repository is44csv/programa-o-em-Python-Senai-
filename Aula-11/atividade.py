# atividade 1 
def par_ou_impar():
    numero = int (input('digite um numero:'))
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'


print(par_ou_impar())

# atividade 2 
def multiplicação():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    c = float(input("Digite o terceiro número: "))

    resultado = a * b * c

    print("O resultado da multiplicação é:", resultado)

# atividade 3
def elevar(numero, expoente):
    return numero ** expoente

# Exemplo de uso
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = elevar(base, expoente)

print("Resultado:", resultado)

# atividade 4
def mostrar_mensagem(idade):
    if idade == 18:
        print("Parabéns! Você tem 18 anos e atingiu a maioridade.")
    else:
        print("Você tem", idade, "anos.")

# Entrada de dados
idade = int(input("Digite sua idade: "))

# Chamada da função
mostrar_mensagem(idade)

# atividade 5
from datetime import date

def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade

# Entrada de dados
ano = int(input("Digite o ano de nascimento: "))

# Chamada da função
idade = calcular_idade(ano)

print("Sua idade é:", idade, "anos.")

# atividade 6
def verificar_copa(ano):
    if ano == 1999:
        print("Não houve Copa do Mundo em 1999.")
    else:
        print("Ano diferente de 1999.")

# Entrada de dados
ano = int(input("Digite o ano: "))

# Chamada da função
verificar_copa(ano)

# atividade 7
# Lista com o cardápio
cardapio = ["Salada", "Macarronada", "Sanduíche", "Sorvete"]

# Função para cumprimentar o cliente
def cumprimentar():
    print("===================================")
    print("   Bem-vindo ao Restaurante!")
    print("===================================")

# Função do restaurante
def restaurante():
    while True:
        print("\nCardápio:")
        for i, item in enumerate(cardapio, start=1):
            print(f"{i} - {item}")

        opcao = int(input("\nEscolha uma opção (1 a 4): "))

        if opcao >= 1 and opcao <= 4:
            print(f"\nVocê escolheu: {cardapio[opcao - 1]}")
        else:
            print("\nOpção inválida!")

        continuar = input("\nDeseja fazer outro pedido? (S/N): ").upper()

        if continuar != "S":
            print("\nObrigado pela preferência! Volte sempre!")
            break

# Programa principal
cumprimentar()
restaurante()