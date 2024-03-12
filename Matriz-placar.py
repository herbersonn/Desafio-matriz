# O código elabora uma matriz que porta um certo número de partidas e exibe a pontuação das determinadas equipes por partida
# a partida representa as linhas e os pontos das equipes as colunas



# importa uma biblioteca('sys' fornece acesso a algumas variáveis e funções específicas do interpretador)
import sys

num_partidas = int(input("Digite o número de partidas: "))
num_equipes = int(input("Digite o número de equipes: "))

# zera a matriz
placar = [[0 for _ in range(num_equipes)] for _ in range(num_partidas)]

# Função para inserir pontos
def inserir_pontos():
    for partida_atual in range(num_partidas):
        print(f"\nPartida {partida_atual + 1}")
        for equipe_atual in range(num_equipes):
            pontos = int(input(f"Digite os pontos da equipe {equipe_atual + 1} na partida {partida_atual + 1}: "))
            placar[partida_atual][equipe_atual] = pontos
    # O uso do (+ 1) serve para a matriz começar a partir do 1

# Função para mostrar o placar
def mostrar_placar():
    print("\nPlacar Final:")
    for partida_atual in range(num_partidas):
        print(f"Partida {partida_atual + 1}: {placar[partida_atual]}")

# Função para consultar dados
def consultar_dados():
    partida = int(input("Digite o número da partida para dar uma averiguada: "))
    match partida:
        case p if 1 <= p <= num_partidas:
            print(f"Placar da Partida {partida}: {placar[partida - 1]}")
            # O (- 1) foi usado para deixar mais compreensivel 
            # Pois sempre no ínicio de uma matriz o índice é 0
        case _:
            print("Número de partida ta errado.")

# Função para excluir dados
def excluir_dados():
    partida = int(input("Digite o número da partida que deseja excluir: "))
    match partida:
        case p if 1 <= p <= num_partidas:
            placar[partida - 1] = [0] * num_equipes
            print(f"Placar da Partida {partida} excluído.")
        case _:
            print("Número de partida inválido.")

# Esse é o loop principal "O MENU"
while True:
    print("\nMenu:")
    print("1. Inserir dados")
    print("2. Exibir dados")
    print("3. Consultar dados")
    print("4. Excluir dados")
    print("5. Sair")

    escolha = int(input("Escolha uma opção (1; 2; 3; 4; 5): "))

    match escolha:
        case 1:
            inserir_pontos()
        case 2:
            mostrar_placar()
        case 3:
            consultar_dados()
        case 4:
            excluir_dados()
        case 5:
            print("Saindo do programa. VALEWW, VOLTE SEMPRE!")
            sys.exit()
            # Encerra o programa
        case _:
            print("Tente um dos números que aprecem no menu")

