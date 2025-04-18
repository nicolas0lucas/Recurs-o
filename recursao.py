def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|" + "|".join(linha) + "|")

def movimento_valido(tabuleiro, linha, coluna):
    n = len(tabuleiro)
    return 0 <= linha < n and 0 <= coluna < n and tabuleiro[linha][coluna] == ' '

def chegou_destino(linha, coluna):
    return linha == 0 and coluna == 3

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
    melhor_profundidade = float('inf')
    melhor_linha, melhor_coluna = linha_atual, coluna_atual
    
    direcoes = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # direita, esquerda, cima, baixo
    
    for dl, dc in direcoes:
        nova_linha, nova_coluna = linha_atual + dl, coluna_atual + dc
        
        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            if chegou_destino(nova_linha, nova_coluna):
                return (nova_linha, nova_coluna, profundidade)
            
            tabuleiro[nova_linha][nova_coluna] = '*'
            resultado = proximo_movimento(tabuleiro, nova_linha, nova_coluna, profundidade + 1)
            tabuleiro[nova_linha][nova_coluna] = ' '
            
            if resultado[2] < melhor_profundidade:
                melhor_linha, melhor_coluna, melhor_profundidade = resultado
    
    return (melhor_linha, melhor_coluna, melhor_profundidade)

def main():
    tabuleiro = [
        [' ', ' ', ' ', ' '],
        [' ', 'X', 'X', ' '],
        [' ', 'X', ' ', ' '],
        ['*', ' ', ' ', 'X']
    ]
    
    linha_atual, coluna_atual = 3, 0
    
    print("Tabuleiro Inicial:")
    mostrar_tabuleiro(tabuleiro)
    
    while not chegou_destino(linha_atual, coluna_atual):
        resultado = proximo_movimento(tabuleiro, linha_atual, coluna_atual, 0)
        
        if resultado[2] == float('inf'):
            print("Erro: Caminho não encontrado!")
            return
        
        linha_atual, coluna_atual = resultado[0], resultado[1]
        tabuleiro[linha_atual][coluna_atual] = '*'
        
        print(f"\nMovendo para ({linha_atual}, {coluna_atual}):")
        mostrar_tabuleiro(tabuleiro)
    
    print("Destino alcançado!")

if __name__ == "__main__":
    main()
