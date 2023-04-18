num_peca = int(input("Escolha uma peça: "))

i = int(input("Escolha a linha: ")) - 1
j = int(input("Escolha a coluna: ")) - 1


tabuleiro = [[0] * 20 for _ in range(20)]


lista_pecas = []
pecas_disponivies = []

peca1 = (i, j)

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


peca19 = [(i, j), (i, j+1), (i, j+2), (i+1, j+1), (i-1, j+1)]


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

lista_pecas.append(peca1)
lista_pecas.append(peca2)
lista_pecas.append(peca3)
lista_pecas.append(peca4)
lista_pecas.append(peca5)
lista_pecas.append(peca6)
lista_pecas.append(peca7)
lista_pecas.append(peca8)
lista_pecas.append(peca9)
lista_pecas.append(peca10)
lista_pecas.append(peca11)
lista_pecas.append(peca12)
lista_pecas.append(peca13)
lista_pecas.append(peca14)
lista_pecas.append(peca15)
lista_pecas.append(peca16)
lista_pecas.append(peca17)
lista_pecas.append(peca18)
lista_pecas.append(peca19)
lista_pecas.append(peca20)
lista_pecas.append(peca21)

for x in range(len(lista_pecas[num_peca-1])):
    print("Posição " + str(x+1))
    print(lista_pecas[num_peca-1][x])


num_posicao = int(input("Escolha a posição: "))
print(lista_pecas[num_peca-1][num_posicao-1])

cordenadas = lista_pecas[num_peca-1][num_posicao-1]

#def verificacao():
    

    
for coordenada in cordenadas:
    j = coordenada[0]
    i = coordenada[1]
    tabuleiro[i][j] = 1


for row in tabuleiro:
    print(row)

    #TRABALHO IA

    #TESTE