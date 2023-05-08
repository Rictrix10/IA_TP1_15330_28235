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
    
    print("Diagonal Blocks")


    num_iterations = 1

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

def print_all_pieces(pieces):
        pieces = Piece.get_all()
        for piece in pieces:
            piece.print()
            #print("")

def select_piece(pieces):
        num_peca = int(input("Escolha uma peça: "))
        return pieces[num_peca - 1]


def get_user_choice():
        print("Opções:")
        print("1 - Selecionar peça")
        print("2 - Virar horizontalmente")
        print("3 - Virar verticalmente")
        print("4 - Rodar peça para a direita")
        print("5 - Rodar peça para a esquerda")
        return int(input("Escolha uma opção: "))




if __name__ == "__main__":
    
    main()

    pieces = Piece.get_all()
    print_all_pieces(pieces)
    place_piece = select_piece(pieces)
    print("Peça selecionada:")
    place_piece.print()


    while True:
        opcao = get_user_choice()
        if opcao == 1:
            #place_piece = select_piece(pieces)
            print("Peça selecionada:")
            place_piece.print()
            break
        elif opcao == 2:
            place_piece.flip_hor()
        elif opcao == 3:
            place_piece.flip_ver()
        elif opcao == 4:
            place_piece.rotate_direita()
        elif opcao == 5:
            place_piece.rotate_esquerda()
        
        print("Peça atual:")
        place_piece.print()
    
    
    
   
    
    
    
    

    '''
    pieces = Peca.get_all()


    for piece in pieces: 
        piece.print()
        print("")
        piece.flip_hor()
        piece.print()
        print("")
        piece.flip_ver()
        piece.print()
        
        print("")
        piece.rotate90()
        piece.print()
        print("")
    '''


