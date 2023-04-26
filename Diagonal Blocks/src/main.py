import pygame
from games.diagonalblocks.players.defensivegreedy import DefensiveGreedyPlayer
from games.diagonalblocks.players.minimax import OffensiveMinimaxPlayer
from games.diagonalblocks.players.defensiveminimax import DefensiveMinimaxPlayer
from games.diagonalblocks.players.human import HumanDiagonalBlocksPlayer
from games.diagonalblocks.players.offensivegreedy import OffensiveGreedyPlayer
from games.diagonalblocks.players.random import RandomDiagonalBlocksPlayer
from games.diagonalblocks.simulator import DiagonalBlocksSimulator
from games.game_simulator import GameSimulator
def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

        print("Results for the game:")
        simulator.print_stats()


def main():
    print("Diagonal Blocks")
    LARGURA_TELA = 400
    ALTURA_TELA = 400
    TAMANHO_CELULA = 20
    NUM_CELULAS = 20
    VERMELHO = (255, 0, 0)
    AZUL = (0, 0, 255)
    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
    TAMANHO_TABULEIRO = NUM_CELULAS * TAMANHO_CELULA
    
    pygame.init()
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Diagonal Blocks')
    screen.fill(BRANCO)
    for i in range(0, LARGURA_TELA, TAMANHO_CELULA):
        pygame.draw.line(screen, PRETO, (i, 0), (i, ALTURA_TELA))
    for i in range(0, ALTURA_TELA, TAMANHO_CELULA):
        pygame.draw.line(screen, PRETO, (0, i), (LARGURA_TELA, i))
    pygame.display.flip()

    num_iterations = 1

    diagonalblocks_simulations = [
        {
            "name": "TicTacToe - Human VS Human",
            "player1": HumanDiagonalBlocksPlayer("Human"),
            "player2": HumanDiagonalBlocksPlayer("Human")
        },
        {
            "name": "TicTacToe - Human VS Random",
            "player1": HumanDiagonalBlocksPlayer("Human"),
            "player2": DefensiveMinimaxPlayer("Minimax")
        },
        {
            "name": "TicTacToe - Random VS Random",
            "player1": RandomDiagonalBlocksPlayer("Random 1"),
            "player2": RandomDiagonalBlocksPlayer("Random 2")
        },
        {
            "name": "TicTacToe - Greedy VS Random",
            "player1": OffensiveGreedyPlayer("Greedy"),
            "player2": RandomDiagonalBlocksPlayer("Random")
        },
        {
            "name": "Minimax VS Random",
            "player1": OffensiveMinimaxPlayer("Minimax"),
            "player2": RandomDiagonalBlocksPlayer("Random")
        },
        {
            "name": "Minimax VS Greedy",
            "player1": DefensiveMinimaxPlayer("Minimax"),
            "player2": DefensiveGreedyPlayer("Greedy")
        }
    ]

    for sim in diagonalblocks_simulations:
        run_simulation(sim["name"], DiagonalBlocksSimulator(sim["player1"], sim["player2"], 20), num_iterations)


if __name__ == "__main__":
    main()
