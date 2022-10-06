import os


matriz = [[" "], [" "], [" "],
          [" "], [" "], [" "],
          [" "], [" "], [" "]]

jogadas = 0
lista_coordenadas = []


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def pedir_usuario_jogadas():
    global jogadas
    global jogador
    global lista_coordenadas

    if jogadas % 2 == 0:
        jogador = "X"
    else:
        jogador = "O"
    
    imprimir_jogo_velha()

    print(f"\nJogadas: {jogadas}")
    print(f"Jogador atual: {jogador}")

    try:
        linha_usuario = int(input("\nInsira a linha: "))
        coluna_usuario = int(input("Insira a coluna: "))

        limpar_terminal()

        coordenada = (linha_usuario, coluna_usuario)

        if linha_usuario > 3 or linha_usuario < 1 or coluna_usuario > 3 or coluna_usuario < 1:
            limpar_terminal()
            print("Insira apenas números entre 1 e 3!")
            pedir_usuario_jogadas()
            
        if coordenada in lista_coordenadas:
            limpar_terminal()
            print(f"\nPosição {coordenada} já foi ocupada!")
            pedir_usuario_jogadas()
        else:
            lista_coordenadas.append(coordenada)
    except:
        limpar_terminal()
        print("Insira apenas números entre 1 e 3!")
        pedir_usuario_jogadas()
    
    jogadas += 1

    atualizar_matriz(linha_usuario, coluna_usuario, jogador)


def atualizar_matriz(linha, coluna, jogador):
    global matriz

    X_ou_O = jogador
    
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
    else:
        pedir_usuario_jogadas()


def imprimir_jogo_velha():
    global matriz

    print("    1   2   3")
    print("  ┌───┬───┬───┐")
    print(f"1 │ {matriz[0][0]} │ {matriz[1][0]} │ {matriz[2][0]} │ 1")
    print("  ├───┼───┼───┤")
    print(f"2 │ {matriz[3][0]} │ {matriz[4][0]} │ {matriz[5][0]} │ 2")
    print("  ├───┼───┼───┤")
    print(f"3 │ {matriz[6][0]} │ {matriz[7][0]} │ {matriz[8][0]} │ 3")
    print("  └───┴───┴───┘")
    print("    1   2   3")


def verificar_vitoria_empate():
    global jogador
    global matriz

    X_ou_O = jogador
    
    #verificar vitória
    if  matriz[0][0] == matriz[4][0] == matriz[8][0] and " " not in (matriz[0][0], matriz[4][0], matriz[8][0]):
        imprimir_vencedor(1)
        return 0 # vencedor
    elif matriz[6][0] == matriz[4][0] == matriz[2][0] and " " not in (matriz[6][0], matriz[4][0], matriz[2][0]):
        imprimir_vencedor(2)
        return 0
    #vitoria nas linhas
    elif matriz[0][0] == matriz[1][0] == matriz[2][0] and " " not in (matriz[0][0], matriz[1][0], matriz[2][0]):
        imprimir_vencedor(3)
        return 0
    elif matriz[3][0] == matriz[4][0] == matriz[5][0] and " " not in (matriz[3][0], matriz[4][0], matriz[5][0]):
        imprimir_vencedor(4)
        return 0
    elif matriz[6][0] == matriz[7][0] == matriz[8][0] and " " not in (matriz[6][0], matriz[7][0], matriz[8][0]):
        imprimir_vencedor(5)
        return 0
    #vitoria nas colunas
    elif matriz[0][0] == matriz[3][0] == matriz[6][0] and " " not in (matriz[0][0], matriz[3][0], matriz[6][0]):
        imprimir_vencedor(6)
        return 0
    elif matriz[1][0] == matriz[4][0] == matriz[7][0] and " " not in (matriz[1][0], matriz[4][0], matriz[7][0]):
        imprimir_vencedor(7)
        return 0
    elif matriz[2][0] == matriz[5][0] == matriz[8][0] and " " not in (matriz[2][0], matriz[5][0], matriz[8][0]):
        imprimir_vencedor(8)
        return 0
    #verificar empate
    elif " " not in (matriz[0][0], matriz[1][0], matriz[2][0], matriz[3][0], matriz[4][0], matriz[5][0], matriz[6][0], matriz[7][0], matriz[8][0]):
        imprimir_jogo_velha()
        print(f"\nDeu velha!")
        return 0


def imprimir_vencedor(x):
    global jogador

    imprimir_resultado_formatado(x)
    print(f"\nVencedor é o jogador {jogador}")
    reiniciar_game()


def imprimir_resultado_formatado(x):
    global matriz
    global jogador

    jogador_formatado = "\033[0;32m{}\033[0;0m".format(jogador)

    if x == 1:
        matriz[0][0] = jogador_formatado
        matriz[4][0] = jogador_formatado
        matriz[8][0] = jogador_formatado
    elif x == 2:
        matriz[6][0] = jogador_formatado
        matriz[4][0] = jogador_formatado
        matriz[2][0] = jogador_formatado
    elif x == 3:
        matriz[0][0] = jogador_formatado
        matriz[1][0] = jogador_formatado
        matriz[2][0] = jogador_formatado
    elif x == 4:
        matriz[3][0] = jogador_formatado
        matriz[4][0] = jogador_formatado
        matriz[5][0] = jogador_formatado
    elif x == 5:
        matriz[6][0] = jogador_formatado
        matriz[7][0] = jogador_formatado
        matriz[8][0] = jogador_formatado
    elif x == 6:
        matriz[0][0] = jogador_formatado
        matriz[3][0] = jogador_formatado
        matriz[6][0] = jogador_formatado
    elif x == 7:
        matriz[1][0] = jogador_formatado
        matriz[4][0] = jogador_formatado
        matriz[7][0] = jogador_formatado
    elif x == 8:
        matriz[2][0] = jogador_formatado
        matriz[5][0] = jogador_formatado
        matriz[8][0] = jogador_formatado

    imprimir_jogo_velha()


def reiniciar_game():
    global matriz
    global jogadas
    global lista_coordenadas

    while True:
        try:
            resposta = input("\nVocê deseja jogar novamente? (s/n): ")

            if resposta == "s":

                matriz = [[" "], [" "], [" "],
                          [" "], [" "], [" "],
                          [" "], [" "], [" "]]
                jogadas = 0
                lista_coordenadas = []

                limpar_terminal()
                pedir_usuario_jogadas()
            else:
                limpar_terminal()
                print("Muito obrigado por usar o programa!")

        except:
            continue


limpar_terminal()
pedir_usuario_jogadas()

