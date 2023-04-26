from game.diagonalblocks.players.greedy import DiagonalBlocksPlayer
from game.diagonalblocks.players.minimax import DiagonalBlocksPlayer
from game.diagonalblocks.players.random import DiagonalBlocksPlayer
from game.diagonalblocks.players.human import HumanDiagonalBlocksPlayer
from game.diagonalblocks.simulator import DiagonalBlocksSimulator
from game.game_simulator import GameSimulator



def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 3

    diagonalblocks_simulations = [

        { 
             "name": "DiagonalBlocks - Human VS Human",
            "player1": HumanDiagonalBlocksPlayer("Human"),
           "player2": HumanDiagonalBlocksPlayer("Human")
        }
    ]

    '''
    diagonalblocks_othersimulations = [
        {
            "name": "DiagonalBlocks - Human VS Random",
            "player1": HumanDiagonalBlocksPlayer("Human"),
           "player2": DiagonalBlocksPlayer("Minimax")
        },
        {
            "name": "TicTacToe - Random VS Random",
            "player1": DiagonalBlocksPlayer("Random 1"),
            "player2": DiagonalBlocksPlayer("Random 2")
        },
        {
            "name": "TicTacToe - Greedy VS Random",
            "player1": DiagonalBlocksPlayer("Greedy"),
            "player2": DiagonalBlocksPlayer("Random")
        },
        {
            "name": "Minimax VS Random",
            "player1": DiagonalBlocksPlayer("Minimax"),
            "player2": DiagonalBlocksPlayer("Random")
        },
        {
            "name": "Minimax VS Greedy",
            "player1": DiagonalBlocksPlayer("Minimax"),
            "player2": DiagonalBlocksPlayer("Greedy")
        }
    ]
    '''

    for sim in diagonalblocks_simulations:
        run_simulation(sim["name"], DiagonalBlocksSimulator(sim["player1"], sim["player2"], 3), num_iterations)


if __name__ == "__main__":
    main()

