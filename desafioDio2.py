# Código do desafio dio 1

nome = input('Digite o nome do herói')

xp = int(input('Digite o total de xp de ' + nome))

match xp:
    case _ if xp <1000:
        nivel = "Ferro"
    case _ if xp in range(1001, 2000):
        nivel = "bronze"
    case _ if xp in range(2001, 5000):
        nivel = "Prata"
    case _ if xp in range(5001, 7000):
        nivel = "Ouro"
    case _ if xp in range(7001, 8000):
        nivel = "Platina"
    case _ if xp in range(8001, 9000):
        nivel = "Ascendente"
    case _ if xp in range(9001, 10000):
        nivel = "Imortal"
    case _ if xp >= 10001:
        nivel = "Radiante"
    case _:
        nivel = "what?"

print(f"O herói de nome {nome} está no nível de {nivel}")

# Agora entrando no código do desafio 2

# Definindo a função que aceita os parâmetros de vitórias e derrotas e faz o cálculo
def calculaRanque (v, d): # v para vitórias e d para derrotas
    numeroranque = v-d # Calcula o ranque em numeros para poder converter para a expressão do mesmo em texto usando o match
    match numeroranque:
        case _ if numeroranque <10:
            ranque = "Ferro"
        case _ if numeroranque in range(11, 20):
            ranque = "Bronze "
        case _ if numeroranque in range(21, 50):
            ranque = "Prata"
        case _ if numeroranque in range(51, 80):
            ranque = "Ouro"
        case _ if numeroranque in range(81,90):
            ranque = "Diamante"
        case _ if numeroranque in range(91, 100):
            ranque = "Lendário"
        case _ if numeroranque >= 101:
            ranque = "Imortal"

    return ranque


vitorias = int(input("Digite o nnúmero de vitórias do herói"))
derrotas = int(input("Agora digite o número de derrotas"))

# com os valores, vamos chamar a funçaõ e exibir

ranqueAtual = calculaRanque(vitorias, derrotas)

# Exibindo, novamente usando um print com f-string para facilitar a leitura
print(f"O herói {nome}, está no ranque {ranqueAtual}, no nível {nivel}")
input() # Uma chamada a uma função input vazia apenas para o leitor de tela poder ler todo o texto sem fechar o console na cara do usuário