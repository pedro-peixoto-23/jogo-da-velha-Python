from multiprocessing.sharedctypes import Value
import os

matriz = [[" "], [" "], [" "],
          [" "], [" "], [" "],
          [" "], [" "], [" "]]

jogadas = 0
lista_coordenadas = []


def pedir_usuario_jogadas():
    global jogadas
    global jogador
    global lista_coordenadas

    if jogadas % 2 == 0:
        jogador = 1
    else:
        jogador = 2
    
    imprimir_jogo_velha()

    print(f"\nJogadas: {jogadas}")
    print(f"Jogador: {jogador}")

    try:
        linha_usuario = int(input("\nInsira a linha: "))
        coluna_usuario = int(input("Insira a coluna: "))

        coordenada = (linha_usuario, coluna_usuario)

        if linha_usuario > 3 or linha_usuario < 1 or coluna_usuario > 3 or coluna_usuario < 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Insira apenas números entre 1 e 3!")
            pedir_usuario_jogadas()
        if coordenada in lista_coordenadas:
            print(f"\nPosição {coordenada} já foi ocupada!")
            pedir_usuario_jogadas()
        else:
            lista_coordenadas.append(coordenada)
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Insira apenas números entre 1 e 3!")
        pedir_usuario_jogadas()

    jogadas += 1
    
    os.system('cls' if os.name == 'nt' else 'clear')

    atualizar_matriz(linha_usuario, coluna_usuario, jogador)


def atualizar_matriz(linha, coluna, jogador):
    global matriz

    if jogador == 1:
        X_ou_O = "X"
    else:
        X_ou_O = "O"
    
    if linha == 1 and coluna == 1:
        matriz[0][0] = X_ou_O
    elif linha == 1 and coluna == 2:
        matriz[1][0] = X_ou_O
    elif linha == 1 and coluna == 3:
        matriz[2][0] = X_ou_O
    elif linha == 2 and coluna == 1:
        matriz[3][0] = X_ou_O
    elif linha == 2 and coluna == 2:
        matriz[4][0] = X_ou_O
    elif linha == 2 and coluna == 3:
        matriz[5][0] = X_ou_O
    elif linha == 3 and coluna == 1:
        matriz[6][0] = X_ou_O
    elif linha == 3 and coluna == 2:
        matriz[7][0] = X_ou_O
    elif linha == 3 and coluna == 3:
        matriz[8][0] = X_ou_O
    
    if verificar_vitoria_empate() == 0:
        return 0

    pedir_usuario_jogadas()


def imprimir_jogo_velha():
    global matriz
        
    print("--1---2---3")
    print(f"1 {matriz[0][0]} | {matriz[1][0]} | {matriz[2][0]}")
    print("| ---------")
    print(f"2 {matriz[3][0]} | {matriz[4][0]} | {matriz[5][0]}")
    print("| ---------")
    print(f"3 {matriz[6][0]} | {matriz[7][0]} | {matriz[8][0]}")


def verificar_vitoria_empate():
    global jogador
    global matriz

    if jogador == 1:
        X_ou_O = "O"
    else:
        X_ou_O = "X"
    
    #verificar vitória
    if  matriz[0][0] == matriz[4][0] == matriz[8][0] and " " not in (matriz[0][0], matriz[4][0], matriz[8][0]):
        print(f"\nVencedor é o jogador {jogador}")
        return 0 # vencedor
    elif matriz[6][0] == matriz[4][0] == matriz[2][0] and " " not in (matriz[6][0], matriz[4][0], matriz[2][0]):
        print(f"\nVencedor é o jogador {jogador}")
        return 0 
    #vitoria nas linhas
    elif matriz[0][0] == matriz[1][0] == matriz[2][0] and " " not in (matriz[0][0], matriz[1][0], matriz[2][0]):
        print(f"\nVencedor é o jogador {jogador}")
        return 0
    elif matriz[3][0] == matriz[4][0] == matriz[5][0] and " " not in (matriz[3][0], matriz[4][0], matriz[5][0]):
        print(f"\nVencedor é o jogador {jogador}")
        return 0
    elif matriz[6][0] == matriz[7][0] == matriz[8][0] and " " not in (matriz[6][0], matriz[7][0], matriz[8][0]):
        print(f"\nVencedor é o jogador {jogador}")
        return 0
    #vitoria nas colunas
    elif matriz[0][0] == matriz[3][0] == matriz[6][0] and " " not in (matriz[0][0], matriz[3][0], matriz[6][0]):
        print(f"\nVencedor é o jogador {jogador}")
        return 0
    elif matriz[1][0] == matriz[4][0] == matriz[7][0] and " " not in (matriz[1][0], matriz[4][0], matriz[7][0]):
        print(f"\nVencedor é o jogador {jogador}")
        return 0
    elif matriz[2][0] == matriz[5][0] == matriz[8][0] and " " not in (matriz[2][0], matriz[5][0], matriz[8][0]):
        print(f"\nVencedor é o jogador {jogador}")
        return 0
    #verificar empate
    elif " " not in (matriz[0][0], matriz[1][0], matriz[2][0], matriz[3][0], matriz[4][0], matriz[5][0], matriz[6][0], matriz[7][0], matriz[8][0]):
        print(f"\nOcorreu um empate!")
        return 0


pedir_usuario_jogadas()
