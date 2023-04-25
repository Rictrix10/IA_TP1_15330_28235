from game.diagonalblocks.players.greedy import GreedyConnect4Player
from game.diagonalblocks.players.minimax import MinimaxConnect4Player
from game.diagonalblocks.players.random import RandomConnect4Player
from game.diagonalblocks.simulator import Connect4Simulator
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

    num_iterations = 1000

    c4_simulations = [
        # uncomment to play as human
        #{
        #    "name": "Connect4 - Human VS Random",
        #    "player1": HumanConnect4Player("Human"),
        #    "player2": RandomConnect4Player("Random")
        #},
        {
            "name": "TicTacToe - Random VS Random",
            "player1": RandomConnect4Player("Random 1"),
            "player2": RandomConnect4Player("Random 2")
        },
        {
            "name": "TicTacToe - Greedy VS Random",
            "player1": GreedyConnect4Player("Greedy"),
            "player2": RandomConnect4Player("Random")
        },
        {
            "name": "Minimax VS Random",
            "player1": MinimaxConnect4Player("Minimax"),
            "player2": RandomConnect4Player("Random")
        },
        {
            "name": "Minimax VS Greedy",
            "player1": MinimaxConnect4Player("Minimax"),
            "player2": GreedyConnect4Player("Greedy")
        }
    ]


    for sim in c4_simulations:
        run_simulation(sim["name"], Connect4Simulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()

