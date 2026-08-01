from statistics import mean, mode, StatisticsError, pstdev

# Função para cadastrar as notas
def cadastrar_notas():
    notas = []
    quantidade = int(input("Digite a quantidade de alunos: "))

    for i in range(quantidade):
        nota = float(input(f"Digite a nota do {i+1}º aluno: "))
        notas.append(nota)

    return notas


# Função para calcular a média
def calcular_media(notas):
    return mean(notas)


# Função para calcular a moda
def calcular_moda(notas):
    try:
        return mode(notas)
    except StatisticsError:
        return "Não existe moda."


# Função para calcular o desvio padrão
def calcular_desvio_padrao(notas):
    return pstdev(notas)  # Desvio padrão populacional


# Função para encontrar a menor nota
def menor_nota(notas):
    return min(notas)


# Função para encontrar a maior nota
def maior_nota(notas):
    return max(notas)


# Função para mostrar os resultados
def mostrar_resultados(notas):
    print("\n===== ESTATÍSTICAS DAS NOTAS =====")
    print(f"Notas: {notas}")
    print(f"Média: {calcular_media(notas):.2f}")
    print(f"Moda: {calcular_moda(notas)}")
    print(f"Desvio Padrão: {calcular_desvio_padrao(notas):.2f}")
    print(f"Menor Nota: {menor_nota(notas):.2f}")
    print(f"Maior Nota: {maior_nota(notas):.2f}")


# Programa Principal
def main():
    notas = cadastrar_notas()
    mostrar_resultados(notas)


main()