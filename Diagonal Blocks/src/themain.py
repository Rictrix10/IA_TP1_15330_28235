import pygame
from games.diagonalblocks.players.defensivegreedy import DefensiveGreedyPlayer
from games.diagonalblocks.players.minimax import OffensiveMinimaxPlayer
from games.diagonalblocks.players.defensiveminimax import DefensiveMinimaxPlayer
from games.diagonalblocks.players.human import HumanDiagonalBlocksPlayer
from games.diagonalblocks.players.offensivegreedy import OffensiveGreedyPlayer
from games.diagonalblocks.players.random import RandomDiagonalBlocksPlayer
from games.diagonalblocks.simulator import DiagonalBlocksSimulator
from games.game_simulator import GameSimulator
from games.diagonalblocks.piece import Piece



def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

        print("Results for the game:")
        simulator.print_stats()


def main():
    
    print("Diagonal Blocks\n")


    num_iterations = 2

    diagonalblocks_simulations = [
        {
            "name": "Diagonal Blocks - Human VS Human",
            "player1": HumanDiagonalBlocksPlayer("Human"),
            "player2": HumanDiagonalBlocksPlayer("Human")
        },
        {
            "name": "Diagonal Blocks - Human VS Random",
            "player1": HumanDiagonalBlocksPlayer("Human"),
            "player2": DefensiveMinimaxPlayer("Minimax")
        },
        {
            "name": "Diagonal Blocks - Random VS Random",
            "player1": RandomDiagonalBlocksPlayer("Random 1"),
            "player2": RandomDiagonalBlocksPlayer("Random 2")
        },
        {
            "name": "Diagonal Blocks - Greedy VS Random",
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



