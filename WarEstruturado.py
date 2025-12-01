import random
from collections import deque

# Criando o baralho
def criar_baralho():
    naipes = ['♠', '♥', '♦', '♣']
    valores = list(range(2, 15))  # 2-10, Valete=11, Dama=12, Rei=13, Ás=14
    baralho = [(valor, naipe) for valor in valores for naipe in naipes]
    random.shuffle(baralho)
    return baralho

# Distribuindo cartas entre dois jogadores
def distribuir_cartas(baralho):
    metade = len(baralho) // 2
    jogador1 = deque(baralho[:metade])
    jogador2 = deque(baralho[metade:])
    return jogador1, jogador2

# Função do jogo
def jogar_war(jogador1, jogador2):
    rodada = 1
    while jogador1 and jogador2:
        print(f"\n--- Rodada {rodada} ---")
        carta1 = jogador1.popleft()
        carta2 = jogador2.popleft()
        print(f"Jogador 1 joga: {carta1[0]}{carta1[1]}")
        print(f"Jogador 2 joga: {carta2[0]}{carta2[1]}")

        if carta1[0] > carta2[0]:
            print("Jogador 1 vence a rodada!")
            jogador1.extend([carta1, carta2])
        elif carta2[0] > carta1[0]:
            print("Jogador 2 vence a rodada!")
            jogador2.extend([carta2, carta1])
        else:
            print("Empate! Cada jogador recupera sua carta")
            jogador1.append(carta1)
            jogador2.append(carta2)

        rodada += 1

    if jogador1:
        print("\n🏆 Jogador 1 venceu o jogo!")
    else:
        print("\n🏆 Jogador 2 venceu o jogo!")

if __name__ == "__main__":
    baralho = criar_baralho()
    jogador1, jogador2 = distribuir_cartas(baralho)
    jogar_war(jogador1, jogador2)
