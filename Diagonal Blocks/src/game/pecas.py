import pygame
LARGURA_TELA = 400
ALTURA_TELA = 400
TAMANHO_CELULA = 20
NUM_CELULAS = 20
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
TAMANHO_TABULEIRO = NUM_CELULAS * TAMANHO_CELULA

num_peca = int(input("Escolha uma peça: "))
i = int(input("Escolha a linha: ")) - 1
j = int(input("Escolha a coluna: ")) - 1


tabuleiro = [[0] * 20 for _ in range(20)]


# listas_pecas = [[] for i in range(2)] # dois conjuntos de peças para dois jogadores
pecas_disponivies = []

peca1 = [[(i, j)]]

peca2 = [[(i, j), (i, j+1)],
         [(i, j), (i, j-1)],
         [(i, j), (i-1, j)],
         [(i, j), (i+1, j)]
         ]

peca3 = [[(i, j), (i, j+1), (i, j+2)],
         [(i, j), (i, j-1), (i, j-2)],
         [(i, j), (i-1, j), (i-2, j)],
         [(i, j), (i+1, j), (i+2, j)]
         ]


peca4 = [[(i, j), (i+1, j), (i-1, j+1)],
         [(i, j), (i, j-1), (i-1, j-1)],
         [(i, j), (i, j+1), (i+1, j+1)],
         [(i, j), (i, j-1), (i+1, j-1)]
         ]


peca5 = [[(i, j), (i, j+1), (i, j+2), (i, j+3)],
         [(i, j), (i, j-1), (i, j-2), (i, j-3)],
         [(i, j), (i-1, j), (i-2, j), (i-3, j)],
         [(i, j), (i+1, j), (i+2, j), (i+3, j)]
         ]


peca6 = [[(i, j), (i, j+1), (i, j+2), (i-1, j+2)],
         [(i, j), (i, j+1), (i, j+2), (i+1, j+2)],
         [(i, j), (i, j-1), (i, j-2), (i+1, j-2)],
         [(i, j), (i, j-1), (i, j-2), (i-1, j-2)],
         [(i, j), (i-1, j), (i-2, j), (i-2, j-1)],
         [(i, j), (i-1, j), (i-2, j), (i-2, j+1)],
         [(i, j), (i+1, j), (i+2, j), (i+2, j+1)],
         [(i, j), (i+1, j), (i+2, j), (i+2, j-1)]
         ]


peca7 = [[(i, j), (i, j+1), (i, j+2), (i-1, j+1)],
         [(i, j), (i, j-1), (i, j-2), (i+1, j-1)],
         [(i, j), (i-1, j), (i-2, j), (i-1, j-1)],
         [(i, j), (i+1, j), (i+2, j), (i+1, j+1)]
         ]


peca8 = [[(i, j), (i, j+1), (i-1, j+1), (i-1, j+2)],
         [(i, j), (i, j+1), (i+1, j+1), (i+1, j+2)],
         [(i, j), (i-1, j), (i-1, j+1), (i-2, j+1)],
         [(i, j), (i+1, j), (i+1, j+1), (i+2, j+1)]
         ]


peca9 = [[(i, j), (i, j+1), (i-1, j), (i-1, j+1)],
         [(i, j), (i+1, j), (i+1, j-1), (i, j-1)],
         [(i, j), (i, j-1), (i-1, j-1), (i+1, j)],
         [(i, j), (i, j+1), (i+1, j+1), (i+1, j)]
         ]


peca10 = [[(i, j), (i, j+1), (i, j+2), (i, j+3), (i, j+4)],
          [(i, j), (i, j-1), (i, j-2), (i, j-3), (i, j-4)],
          [(i, j), (i+1, j), (i+2, j), (i+3, j), (i+4, j)],
          [(i, j), (i-1, j), (i-2, j), (i-3, j), (i-4, j)]
          ]


peca11 = [[(i, j), (i, j+1), (i, j+2), (i, j+3), (i-1, j+3)],
          [(i, j), (i, j-1), (i, j-2), (i, j-3), (i-1, j-3)],
          [(i, j), (i, j+1), (i, j+2), (i, j+3), (i+1, j+3)],
          [(i, j), (i, j-1), (i, j-2), (i, j-3), (i+1, j-3)],
          [(i, j), (i+1, j), (i+2, j), (i+3, j), (i+3, j+1)],
          [(i, j), (i+1, j), (i+2, j), (i+3, j), (i+3, j-1)],
          [(i, j), (i-1, j), (i-2, j), (i-3, j), (i-3, j-1)],
          [(i, j), (i-1, j), (i-2, j), (i-3, j), (i-3, j+1)]
          ]


peca12 = [[(i, j), (i, j+1), (i, j+2), (i, j+3), (i-1, j+2)],
          [(i, j), (i, j+1), (i, j+2), (i, j+3), (i+1, j+2)],
          [(i, j), (i+1, j), (i+2, j), (i+3, j), (i+2, j-1)],
          [(i, j), (i+1, j), (i+2, j), (i+3, j), (i+2, j+1)],
          [(i, j), (i, j-1), (i, j-2), (i, j-3), (i+1, j-2)],
          [(i, j), (i, j-1), (i, j-2), (i, j-3), (i-1, j-2)],
          [(i, j), (i-1, j), (i-2, j), (i-3, j), (i-2, j-1)],
          [(i, j), (i-1, j), (i-2, j), (i-3, j), (i-2, j+1)]
          ]


peca13 = [[(i, j), (i, j+1), (i, j+2), (i-1, j+1), (i-2, j+2)],
          [(i, j), (i, j-1), (i, j-2), (i+1, j-1), (i+1, j-2)],
          [(i, j), (i, j+1), (i, j+2), (i+1, j+1), (i+1, j+2)],
          [(i, j), (i, j-1), (i, j-2), (i-1, j-1), (i+1, j-2)],
          [(i, j), (i+1, j), (i+2, j), (i+1, j+1), (i+2, j+1)],
          [(i, j), (i-1, j), (i-2, j), (i-1, j-1), (i-2, j-1)],
          [(i, j), (i+1, j), (i+2, j), (i+1, j-1), (i+2, j-1)],
          [(i, j), (i-1, j), (i-2, j), (i-1, j+1), (i-2, j+1)]
          ]


peca14 = [[(i, j), (i, j+1), (i, j+2), (i-1, j+2), (i-1, j+3)],
          [(i, j), (i+1, j), (i+2, j), (i+2, j+1), (i+3, j+1)],
          [(i, j), (i, j-1), (i, j-2), (i+1, j-2), (i+1, j-3)],
          [(i, j), (i-1, j), (i-2, j), (i-2, j-1), (i-3, j-1)],
          [(i, j), (i, j+1), (i, j+2), (i+1, j+2), (i+1, j+3)],
          [(i, j), (i-1, j), (i-2, j), (i-2, j+1), (i-3, j+1)],
          [(i, j), (i, j-1), (i, j-2), (i-1, j-2), (i-1, j-3)],
          [(i, j), (i+1, j), (i+2, j), (i+2, j-1), (i+3, j-1)]
          ]


peca15 = [[(i, j), (i, j+1), (i, j+2), (i-1, j+2), (i-2, j+2)],
          [(i, j), (i+1, j), (i+2, j), (i+2, j+1), (i+2, j+2)],
          [(i, j), (i, j-1), (i, j-2), (i+1, j-2), (i+2, j-2)],
          [(i, j), (i-1, j), (i-2, j), (i-2, j-1), (i-2, j-2)],
          [(i, j), (i-1, j), (i-2, j), (i-2, j-1), (i-2, j-2)],
          [(i, j), (i, j-1), (i, j-2), (i+1, j-2), (i+2, j-2)],
          [(i, j), (i+1, j), (i+2, j), (i+2, j+1), (i+2, j+2)],
          [(i, j), (i, j+1), (i, j+2), (i-1, j+2), (i-2, j+2)]
          ]


peca16 = [[(i, j), (i, j+1), (i-1, j+1), (i-2, j+1), (i-2, j+2)],
          [(i, j), (i+1, j), (i+1, j+1), (i+1, j+2), (i+2, j+2)],
          [(i, j), (i, j+1), (i-1, j+1), (i-2, j+1), (i-2, j+2)],
          [(i, j), (i+1, j), (i+1, j+1), (i+1, j+2), (i+2, j+2)],
          [(i, j), (i, j+1), (i+1, j+1), (i+2, j+1), (i+2, j+2)],
          [(i, j), (i-1, j), (i-1, j+1), (i-1, j+2), (i-2, j+2)],
          [(i, j), (i, j+1), (i+1, j+1), (i+2, j+1), (i+2, j+2)],
          [(i, j), (i-1, j), (i-1, j+1), (i-1, j+2), (i-2, j+2)]
          ]


peca17 = [[(i, j), (i, j+1), (i-1, j+1), (i-2, j+1), (i-2, j)],
          [(i, j), (i+1, j), (i+1, j+1), (i+1, j+2), (i, j+2)],
          [(i, j), (i, j-1), (i+1, j-1), (i+2, j-1), (i+2, j)],
          [(i, j), (i-1, j), (i-1, j-1), (i-1, j-2), (i, j-2)],
          [(i, j), (i-1, j), (i-1, j-1), (i-1, j-2), (i, j-2)],
          [(i, j), (i+1, j), (i+1, j+1), (i+1, j+2), (i, j+2)]
          ]


peca18 = [[(i, j), (i, j+1), (i-1, j+1), (i-1, j+2), (i-2, j+2)],
          [(i, j), (i+1, j), (i+1, j+1), (i+2, j+1), (i+2, j+2)],
          [(i, j), (i, j-1), (i+1, j-1), (i+1, j-2), (i+2, j-2)],
          [(i, j), (i-1, j), (i-1, j-1), (i-2, j-1), (i-2, j-2)],
          [(i, j), (i-1, j), (i-1, j-1), (i-2, j-1), (i-2, j-2)],
          [(i, j), (i, j-1), (i+1, j-1), (i+1, j-2), (i+2, j-2)],
          [(i, j), (i+1, j), (i+1, j+1), (i+2, j+1), (i+2, j+2)],
          [(i, j), (i, j+1), (i-1, j+1), (i-1, j+2), (i-2, j+2)]
          ]


peca19 = [[(i, j), (i, j+1), (i, j+2), (i+1, j+1), (i-1, j+1)]]


peca20 = [[(i, j), (i, j+1), (i, j+2), (i-1, j+1), (i-2, j+1)],
          [(i, j), (i+1, j), (i+2, j), (i+1, j+1), (i+1, j+2)],
          [(i, j), (i, j-1), (i, j-2), (i+1, j-1), (i+2, j-1)],
          [(i, j), (i-1, j-1), (i-1, j-2), (i-1, j), (i-2, j)],
          [(i, j), (i, j-1), (i, j-2), (i+1, j-1), (i+2, j-1)],
          [(i, j), (i, j+1), (i, j+2), (i-1, j+1), (i-2, j+1)]
          ]


peca21 = [[(i, j), (i, j+1), (i-1, j+1), (i-2, j+1), (i-1, j+2)],
          [(i, j), (i+1, j), (i+1, j+1), (i+1, j+2), (i+3, j+1)],
          [(i, j), (i, j-1), (i+1, j-1), (i+1, j-2), (i+2, j-1)],
          [(i, j), (i-1, j), (i-1, j-1), (i-1, j-2), (i-2, j-1)],
          [(i, j), (i, j+1), (i+1, j+1), (i+2, j+1), (i+1, j+2)],
          [(i, j), (i-1, j), (i-1, j+1), (i-1, j+2), (i-1, j+1)],
          [(i, j), (i, j-1), (i-1, j-1), (i-2, j-1), (i-1, j-2)],
          [(i, j), (i+1, j), (i+1, j-1), (i+1, j-2), (i+2, j-1)]
          ]

lista_pecas1 = [peca1, peca2, peca3, peca4, peca5, peca6, peca7, peca8, peca9, peca10,
                peca11, peca12, peca13, peca14, peca15, peca16, peca17, peca18, peca19, peca20, peca21]
lista_pecas2 = [peca1, peca2, peca3, peca4, peca5, peca6, peca7, peca8, peca9, peca10,
                peca11, peca12, peca13, peca14, peca15, peca16, peca17, peca18, peca19, peca20, peca21]


for x in range(len(lista_pecas1[num_peca-1])):
    print("Posição " + str(x+1))
    print(lista_pecas1[num_peca-1][x])


num_posicao = int(input("Escolha a posição: "))
print(lista_pecas1[num_peca-1][num_posicao-1])

cordenadas = lista_pecas1[num_peca-1][num_posicao-1]


for coordenada in cordenadas:
    j = coordenada[0]
    i = coordenada[1]
    tabuleiro[i][j] = 1


for row in tabuleiro:
    print(row)

def desenhar_tabuleiro(screen):
    # desenhar células vazias em branco
    for i in range(NUM_CELULAS):
        for j in range(NUM_CELULAS):
            x = j * TAMANHO_CELULA
            y = i * TAMANHO_CELULA
            pygame.draw.rect(
                screen, BRANCO, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))

    # desenhar linhas verticais
    for i in range(0, TAMANHO_TABULEIRO, TAMANHO_CELULA):
        pygame.draw.line(screen, PRETO, (i, 0), (i, TAMANHO_TABULEIRO), 1)

    # desenhar linhas horizontais
    for j in range(0, TAMANHO_TABULEIRO, TAMANHO_CELULA):
        pygame.draw.line(screen, PRETO, (0, j), (TAMANHO_TABULEIRO, j), 1)

    # desenhar células ocupadas em vermelho
    for i, j in cordenadas:
        x = j * TAMANHO_CELULA
        y = i * TAMANHO_CELULA
        pygame.draw.rect(screen, VERMELHO,
                         (x, y, TAMANHO_CELULA, TAMANHO_CELULA))

'''
def dentro_do_tabuleiro(posicao, NUM_CELULAS, TAMANHO_CELULA):
    """
    Verifica se a posição da célula superior esquerda da peça está dentro do tabuleiro.
    posicao: tupla (x,y) com as coordenadas da célula superior esquerda da peça.
    tam_tabuleiro: inteiro com o tamanho do tabuleiro (largura e altura iguais).
    tam_peca: inteiro com o tamanho da peça (largura e altura iguais).
    Retorna True se a posição está dentro do tabuleiro e False caso contrário.
    """
    x, y = posicao
    if x < 0 or y < 0:
        return False
    if x + TAMANHO_CELULA > NUM_CELULAS or y + TAMANHO_CELULA > NUM_CELULAS:
        return False
    return True
'''


def main():
    pygame.init()

    # Criar a janela do jogo
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Diagonal Blocks')

    # Desenhar o tabuleiro
    desenhar_tabuleiro(screen)

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
