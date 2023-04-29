import pygame
from pygame.locals import *
LARGURA_TELA = 400
ALTURA_TELA = 400
TAMANHO_CELULA = 20
NUM_CELULAS = 20
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
TAMANHO_TABULEIRO = NUM_CELULAS * TAMANHO_CELULA

pecas_escolhidas1 = []
pecas_escolhidas2 = []
tabuleiro = [[0] * 20 for _ in range(20)]

def criar_peca(i, j):
    peca1 = [[(i, j)]]

    peca2 = [[(i, j), (i, j+1)]]

    diagpeca2 = [[(i-1, j-1), (i+1, j-1), (i+1, j+2), (i-1, j+2)]]

    peca3 = [[(i, j), (i, j+1), (i, j+2)]]

    peca4 = [[(i, j), (i, j+1), (i-1, j+1)]]

    peca5 = [[(i, j), (i, j+1), (i, j+2), (i, j+3)]]

    peca6 = [[(i, j), (i, j+1), (i, j+2), (i-1, j+2)]]

    peca7 = [[(i, j), (i, j+1), (i, j+2), (i-1, j+1)]]

    peca8 = [[(i, j), (i, j+1), (i-1, j+1), (i-1, j+2)]]

    peca9 = [[(i, j), (i, j+1), (i-1, j), (i-1, j+1)]]

    peca10 = [[(i, j), (i, j+1), (i, j+2), (i, j+3), (i, j+4)]]

    peca11 = [[(i, j), (i, j+1), (i, j+2), (i, j+3), (i-1, j+3)]]

    peca12 = [[(i, j), (i, j+1), (i, j+2), (i, j+3), (i-1, j+2)]]

    peca13 = [[(i, j), (i, j+1), (i, j+2), (i-1, j+1), (i-2, j+2)]]

    peca14 = [[(i, j), (i, j+1), (i, j+2), (i-1, j+2), (i-1, j+3)]]

    peca15 = [[(i, j), (i, j+1), (i, j+2), (i-1, j+2), (i-2, j+2)]]

    peca16 = [[(i, j), (i, j+1), (i-1, j+1), (i-2, j+1), (i-2, j+2)]]

    peca17 = [[(i, j), (i, j+1), (i-1, j+1), (i-2, j+1), (i-2, j)]]

    peca18 = [[(i, j), (i, j+1), (i-1, j+1), (i-1, j+2), (i-2, j+2)]]

    peca19 = [[(i, j), (i, j+1), (i, j+2), (i+1, j+1), (i-1, j+1)]]

    peca20 = [[(i, j), (i, j+1), (i, j+2), (i-1, j+1), (i-2, j+1)]]

    peca21 = [[(i, j), (i, j+1), (i-1, j+1), (i-2, j+1), (i-1, j+2)]]
    '''
    lista_pecas1 = [peca1, peca2, peca3, peca4, peca5, peca6, peca7, peca8, peca9, peca10,
                        peca11, peca12, peca13, peca14, peca15, peca16, peca17, peca18, peca19, peca20, peca21]
    lista_pecas2 = [peca1, peca2, peca3, peca4, peca5, peca6, peca7, peca8, peca9, peca10,
                        peca11, peca12, peca13, peca14, peca15, peca16, peca17, peca18, peca19, peca20, peca21]
    '''
    return [peca1, peca2, diagpeca2, peca3, peca4, peca5, peca6, peca7, peca8, peca9, peca10,
                        peca11, peca12, peca13, peca14, peca15, peca16, peca17, peca18, peca19, peca20, peca21]


peca2 = [[(i, j), (i, j+1)],
[(i-1, j-1), (i+1, j-1), (i+1, j+2), (i-1, j+2)]]

    # Translada a peça para baixo
def translacao(peca2):
        nova_peca = []
        nova_peca = peca2
        for bloco in peca2:
            novo_bloco = [(bloco[0][0]+1, bloco[0][1]), (bloco[1][0]+1, bloco[1][1])]
            if len(bloco) > 2:
                novo_bloco.append((bloco[2][0]+1, bloco[2][1]))
                novo_bloco.append((bloco[3][0]+1, bloco[3][1]))
            nova_peca.append(novo_bloco)
        return nova_peca
    
def rotate_piece(peca2):
    # Transpõe a matriz
    rotated_piece = list(zip(*peca2[::-1]))
    # Converte as tuplas em listas
    rotated_piece = [list(row) for row in rotated_piece]
    return rotated_piece



def escolher_peca(round):
    global num_peca, i, j
    num_peca = int(input("Escolha uma peça: "))
    i = int(input("Escolha a linha: ")) - 1
    j = int(input("Escolha a coluna: ")) - 1
    lista_pecas1 = criar_peca(i,j)
    lista_pecas2 = criar_peca(i,j)

    if round % 2 == 0 :
        for x in range(len(lista_pecas1[num_peca-1])):
            print("Posição " + str(x+1))
            print(lista_pecas1[num_peca-1][x])
        num_posicao = int(input("Escolha a posição: "))
        print(lista_pecas1[num_peca-1][num_posicao-1])
        cordenadas = lista_pecas1[num_peca-1][num_posicao-1]
        pecas_escolhidas1.append(num_peca)
        for coordenada in cordenadas:
            i = coordenada[0]
            j = coordenada[1]
            tabuleiro[i][j] = 1
        return cordenadas

    else:
        for x in range(len(lista_pecas2[num_peca-1])):
            print("Posição " + str(x+1))
            print(lista_pecas2[num_peca-1][x])
        num_posicao = int(input("Escolha a posição: "))
        print(lista_pecas2[num_peca-1][num_posicao-1])
        cordenadas = lista_pecas2[num_peca-1][num_posicao-1]
        pecas_escolhidas2.append(num_peca)
        for coordenada in cordenadas:
            i = coordenada[0]
            j = coordenada[1]
            tabuleiro[i][j] = 2
        return cordenadas


def printTabuleiro():
    pygame.init()
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Diagonal Blocks')
    screen.fill(BRANCO)
    for i in range(0, LARGURA_TELA, TAMANHO_CELULA):
        pygame.draw.line(screen, PRETO, (i, 0), (i, ALTURA_TELA))
    for i in range(0, ALTURA_TELA, TAMANHO_CELULA):
        pygame.draw.line(screen, PRETO, (0, i), (LARGURA_TELA, i))
    pygame.display.flip()



def dentro_do_tabuleiro(posicao, NUM_CELULAS, TAMANHO_CELULA):
    x, y = posicao
    if x < 0 or y < 0:
        return False
    if x + TAMANHO_CELULA > NUM_CELULAS or y + TAMANHO_CELULA > NUM_CELULAS:
        return False
    return True

def atualizar_tabuleiro(screen, cordenadas, round):
    for i, j in cordenadas:
        x = j * TAMANHO_CELULA
        y = i * TAMANHO_CELULA
        if round % 2 == 0 :
            pygame.draw.rect(screen, VERMELHO,
                            (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
        else:
            pygame.draw.rect(screen, AZUL,
                            (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
        pygame.display.update()


def main():
    '''
    pygame.init()
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Diagonal Blocks')
    print_tabuleiro(screen)
    '''
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    printTabuleiro()

    for round in range(2):
        cordenadas = escolher_peca(round)
        atualizar_tabuleiro(screen, cordenadas, round)

    print(pecas_escolhidas1)
    print(pecas_escolhidas2)

    for row in tabuleiro:
        print(row)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Obter as coordenadas do mouse
                pos = pygame.mouse.get_pos()

                # Converter as coordenadas do mouse para coordenadas de célula
                x = pos[0] // TAMANHO_CELULA
                y = pos[1] // TAMANHO_CELULA

                # Imprimir as coordenadas da célula clicada
                print(f"Célula selecionada: ({x}, {y})")

        pygame.display.flip()


if __name__ == '__main__':
    main()
