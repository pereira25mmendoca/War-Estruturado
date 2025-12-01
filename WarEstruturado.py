import random
from collections import deque

def criar_baralho():
    naipes = ['♠', '♥', '♦', '♣']
    valores = list(range(2, 15))
    baralho = [(valor, naipe) for valor in valores for naipe in naipes]
    random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho):
    metade = len(baralho) // 2
    jogador1 = deque(baralho[:metade])
    jogador2 = deque(baralho[metade:])
    return jogador1, jogador2

def jogar_war(j1, j2, max_rodadas=1000):
    rodada = 1
    while j1 and j2 and rodada <= max_rodadas:
        print(f"\n--- Rodada {rodada} ---")
        c1 = j1.popleft()
        c2 = j2.popleft()
        print(f"Jogador 1 joga: {c1[0]}{c1[1]}")
        print(f"Jogador 2 joga: {c2[0]}{c2[1]}")

        if c1[0] > c2[0]:
            j1.extend([c1, c2])
            print("Jogador 1 vence a rodada!")
        elif c2[0] > c1[0]:
            j2.extend([c2, c1])
            print("Jogador 2 vence a rodada!")
        else:
            # Empate: devolve cartas e continua
            j1.append(c1)
            j2.append(c2)
            print("Empate! Cartas devolvidas.")

        rodada += 1

    if len(j1) > len(j2):
        print("\n🏆 Jogador 1 venceu o jogo!")
    elif len(j2) > len(j1):
        print("\n🏆 Jogador 2 venceu o jogo!")
    else:
        print("\n🤝 Empate final!")

if __name__ == "__main__":
    baralho = criar_baralho()
    j1, j2 = distribuir_cartas(baralho)
    jogar_war(j1, j2)

