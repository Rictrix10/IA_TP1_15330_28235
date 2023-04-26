from games.diagonalblocks.players.defensivegreedy import DefensiveGreedyPlayer
from games.diagonalblocks.players.minimax import OffensiveMinimaxPlayer
from games.diagonalblocks.players.defensiveminimax import DefensiveMinimaxPlayer
from games.diagonalblocks.players.human import HumanTicTacToePlayer
from games.diagonalblocks.players.offensivegreedy import OffensiveGreedyPlayer
from games.diagonalblocks.players.random import RandomTicTacToePlayer
from games.diagonalblocks.simulator import TicTacToeSimulator
from games.game_simulator import GameSimulator
def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

        print("Results for the game:")
        simulator.print_stats()


def main():
    print("TicTacToe Simulator")

    num_iterations = 1

    tictactoe_simulations = [
        {
            "name": "TicTacToe - Human VS Human",
            "player1": HumanTicTacToePlayer("Human"),
            "player2": HumanTicTacToePlayer("Human")
        },
        {
            "name": "TicTacToe - Human VS Random",
            "player1": HumanTicTacToePlayer("Human"),
            "player2": DefensiveMinimaxPlayer("Minimax")
        },
        {
            "name": "TicTacToe - Random VS Random",
            "player1": RandomTicTacToePlayer("Random 1"),
            "player2": RandomTicTacToePlayer("Random 2")
        },
        {
            "name": "TicTacToe - Greedy VS Random",
            "player1": OffensiveGreedyPlayer("Greedy"),
            "player2": RandomTicTacToePlayer("Random")
        },
        {
            "name": "Minimax VS Random",
            "player1": OffensiveMinimaxPlayer("Minimax"),
            "player2": RandomTicTacToePlayer("Random")
        },
        {
            "name": "Minimax VS Greedy",
            "player1": DefensiveMinimaxPlayer("Minimax"),
            "player2": DefensiveGreedyPlayer("Greedy")
        }
    ]

    for sim in tictactoe_simulations:
        run_simulation(sim["name"], TicTacToeSimulator(sim["player1"], sim["player2"], 3), num_iterations)


if __name__ == "__main__":
    main()
