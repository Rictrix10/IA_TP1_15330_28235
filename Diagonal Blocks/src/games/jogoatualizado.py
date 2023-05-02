import pygame
from pygame.locals import *
LARGURA_TELA = 400
ALTURA_TELA = 400
TAMANHO_CELULA = 20
NUM_CELULAS = 20
VERMELHO = (255, 0, 0)
red = (255, 225, 225)
AZUL = (0, 0, 255)
blue = (225, 225, 255)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
TAMANHO_TABULEIRO = NUM_CELULAS * TAMANHO_CELULA

pecas_escolhidas1 = []
pecas_escolhidas2 = []
tabuleiro = [['0'] * 20 for _ in range(20)]

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

def criar_peca(i, j):
    peca1 = [[(i, j)]]

    peca2 = [[(i, j), (i, j+1)]]

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

    return [peca1, peca2, peca3, peca4, peca5, peca6, peca7, peca8, peca9, peca10,
                        peca11, peca12, peca13, peca14, peca15, peca16, peca17, peca18, peca19, peca20, peca21]

def criar_diagonal(i, j):

    PECA1 = [[(i-1, j-1), (i+1, j-1), (i-1, j+1), (i+1, j+1)]]

    PECA2 = [[(i-1, j-1), (i+1, j-1), (i+1, j+2), (i-1, j+2)]]

    PECA3 = [[(i-1, j-1), (i+1, j-1), (i-1, j+3), (i+1, j+3)]]

    PECA4 = [[(i-1, j-1), (i+1, j-1), (i-2, j), (i-2, j+2), (i+1, j+2)]]

    return [PECA1, PECA2, PECA3, PECA4]


def atualizar_tabuleiro(screen, cordenadas, diagonais_peca, round):
    for i, j in cordenadas:
        x = j * TAMANHO_CELULA
        y = i * TAMANHO_CELULA
        if round % 2 == 0 :
            pygame.draw.rect(screen, VERMELHO,
                            (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
        else:
            pygame.draw.rect(screen, AZUL,
                            (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
    for i, j in diagonais_peca:
        x = j * TAMANHO_CELULA
        y = i * TAMANHO_CELULA
        if round % 2 == 0:
            pygame.draw.rect(screen, red, 
                             (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
        else:
            pygame.draw.rect(screen, blue,
                            (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
    pygame.display.update()


def roda_peca_contra_relogio(i, j, peca_selecionada):
    nova_peca = []
    for coord in peca_selecionada:
        x, y = coord
        # Rotaciona a peça em 90 graus
        nova_x = -y
        nova_y = x
        nova_peca.append((nova_x, nova_y))
    # Translada a peça para que sua coordenada superior esquerda seja (0, 0)
    min_x = min(x for x, y in nova_peca)
    min_y = min(y for x, y in nova_peca)
    nova_peca = [(x - min_x + i, y - min_y + j) for x, y in nova_peca]
    # Ordena a lista de coordenadas para que a ordem seja consistente
    nova_peca = sorted(nova_peca)
    return nova_peca

def roda_diagonais_contra_relogio(i, j, diagonais_peca):
    nova_peca = []
    for coord in diagonais_peca:
        x, y = coord
        # Rotaciona a peça em 90 graus
        nova_x = -y
        nova_y = x
        nova_peca.append((nova_x, nova_y))
    # Translada a peça para que sua coordenada superior esquerda seja (0, 0)
    min_x = min(x for x, y in nova_peca)
    min_y = min(y for x, y in nova_peca)
    nova_peca = [(x - min_x + i-1, y - min_y + j-1) for x, y in nova_peca]
    # Ordena a lista de coordenadas para que a ordem seja consistente
    nova_peca = sorted(nova_peca)
    return nova_peca

def roda_peca_relogio(i, j, peca_selecionada):
    nova_peca = []
    for coord in peca_selecionada:
        x, y = coord
        # Rotaciona a peça em 90 graus no sentido contrário
        nova_x = y
        nova_y = -x
        nova_peca.append((nova_x, nova_y))
    # Translada a peça para que sua coordenada superior esquerda seja (0, 0)
    min_x = min(x for x, y in nova_peca)
    min_y = min(y for x, y in nova_peca)
    nova_peca = [(x - min_x + i, y - min_y + j) for x, y in nova_peca]
    # Ordena a lista de coordenadas para que a ordem seja consistente
    nova_peca = sorted(nova_peca)
    return nova_peca


def roda_diagonais_relogio(i, j, diagonais_peca):
    nova_peca = []
    for coord in diagonais_peca:
        x, y = coord
        # Rotaciona a peça em 90 graus no sentido contrário
        nova_x = y
        nova_y = -x
        nova_peca.append((nova_x, nova_y))
    # Translada a peça para que sua coordenada superior esquerda seja (0, 0)
    min_x = min(x for x, y in nova_peca)
    min_y = min(y for x, y in nova_peca)
    nova_peca = [(x - min_x + i-1, y - min_y + j-1) for x, y in nova_peca]
    # Ordena a lista de coordenadas para que a ordem seja consistente
    nova_peca = sorted(nova_peca)
    return nova_peca

def get_user_choice():
        print("Opções:")
        print("1 - Selecionar peça")
        print("2 - Virar horizontalmente")
        print("3 - Virar verticalmente")
        print("4 - Rodar 90º")
        return int(input("Escolha uma opção: "))

def validate_play(num_peca, i, j, pecas_jogadas, round):
    if not (1 <= num_peca <= 21):
        print("Essa peça não existe")
        return False
        
    if num_peca in pecas_jogadas:
        print("Essa peça já foi jogada")
        return False
    
    if not (1 <= i <= 20):
        print("Essa linha não existe")
        return False
    
    if not (1 <= j <= 20):
        print("Essa coluna não existe")
        return False
    
    return True

def jogadas_possiveis(tabuleiro):
    places = []
    for x in range(20):
        for y in range(20):
            if tabuleiro[x][y] == '1':
                places.append((x,y))
    return places


def main():
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    printTabuleiro()
    pecas_jogadas = []
    for round in range(1):


        global num_peca, i, j
        num_peca = int(input("Escolha uma peça: "))
        i = int(input("Escolha a linha: ")) - 1
        j = int(input("Escolha a coluna: ")) - 1
        validacao = validate_play(num_peca, i, j, pecas_jogadas, round)
        print(validacao)




        #'''  Peças e diagonais em listas separadas
        if round % 2 == 0 :   # jogador 1
            lista_pecas1 = criar_peca(i,j)
            diagonais1 = criar_diagonal(i, j)

            peca_selecionada = lista_pecas1[num_peca-1][0]
            diagonais_peca = diagonais1[num_peca-1][0]  
            print("Peça selecionada: ", peca_selecionada)
            print("Diagonais da peça: ", diagonais_peca)
            cordenadas = peca_selecionada
            diagonais = diagonais_peca

            # Rodar
            #nova_peca = roda_peca_contra_relogio(i, j, peca_selecionada) 
            #novas_diagonais = roda_diagonais_contra_relogio(i, j, diagonais_peca)
            nova_peca = roda_peca_relogio(i, j, peca_selecionada) 
            novas_diagonais = roda_diagonais_relogio(i, j, diagonais_peca)
            print("Peça rodada: ", nova_peca) 
            print("Diagonais rodadas: ", novas_diagonais)
            cordenadas = nova_peca
            diagonais = novas_diagonais

            atualizar_tabuleiro(screen, cordenadas, diagonais, round)
            pecas_jogadas.append(num_peca)
            print("Peças jogadas: ", pecas_jogadas)

            for coordenada in cordenadas:
                i = coordenada[0]
                j = coordenada[1]
                tabuleiro[i][j] = 'R'
            for diagonal in diagonais:
                i = diagonal[0]
                j = diagonal[1]
                tabuleiro[i][j] = '1'
            
                for row in tabuleiro:
                    print(row)
            
            locais = jogadas_possiveis(tabuleiro)
            print("Jogadas possíveis: ", locais)
            
        else:                 # jogador 2    - falta adaptar para aqui
            lista_pecas2 = criar_peca(i,j)
            diagonais2 = criar_diagonal(i, j)

            print(lista_pecas2[num_peca-1][0])
            cordenadas = lista_pecas2[num_peca-1][0]
            print(diagonais2[num_peca-1][0])
            diagonais_peca = diagonais2[num_peca-1][0]
            atualizar_tabuleiro(screen, cordenadas, diagonais_peca, round)
            for coordenada in cordenadas:
                i = coordenada[0]
                j = coordenada[1]
                tabuleiro[i][j] = 'B'
            for diagonal in diagonais_peca:
                i = diagonal[0]
                j = diagonal[1]
                tabuleiro[i][j] = '2'
        #'''


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        pygame.display.flip()


if __name__ == '__main__':
    main()



