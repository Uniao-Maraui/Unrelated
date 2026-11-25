"""Valores ajustáveis do jogo. Para balancear, altere apenas este arquivo."""

import pygame

# Tela
LARGURA_TELA, ALTURA_TELA = 800, 600
FPS = 60
DT_MAXIMO = 0.05
TITULO = "Unrelated"

# Cores
PRETO, BRANCO = (0, 0, 0), (255, 255, 255)
AMARELO, CINZA = (255, 220, 0), (120, 120, 120)

# Modos e controles
MODO_SOLO, MODO_VERSUS = "solo", "versus"
AFASTAMENTO_VERSUS = 60                   # distância inicial de cada um ao centro
TECLAS_P1 = {"cima": pygame.K_w, "baixo": pygame.K_s,
             "esquerda": pygame.K_a, "direita": pygame.K_d}
TECLAS_P2 = {"cima": pygame.K_UP, "baixo": pygame.K_DOWN,
             "esquerda": pygame.K_LEFT, "direita": pygame.K_RIGHT}

# Jogador (velocidades em pixels por segundo, tempos em segundos)
VIDAS_MAXIMAS = 3
TEMPO_INVULNERAVEL = 2.0
INTERVALO_PISCAR = 0.1
VELOCIDADE_JOGADOR = 220
TAMANHO_JOGADOR = (27, 27)

# Arena
CENTRO_ARENA = (400, 330)
TAMANHOS_ARENA = [(480, 300), (360, 260), (600, 220), (300, 300)]
VELOCIDADE_TRANSICAO_ARENA = 200
ESPESSURA_BORDA_ARENA = 4

# Projéteis
RAIO_PROJETIL = 6                         # tamanho do círculo dos projéteis soltos
TAMANHO_PROJETIL = (24, 24)               # imagem dos projéteis dos inimigos
VELOCIDADE_PROJETIL = 150
VELOCIDADE_MAXIMA_PROJETIL = 260
MARGEM_SURGIMENTO = 90
MAXIMO_PROJETEIS = 60

# Inimigos
TAMANHO_INIMIGO = (64, 64)
POSICOES_INIMIGOS = [(400, 70), (230, 70), (570, 70)]
INTERVALO_CHUVA, INTERVALO_LATERAL, INTERVALO_MIRA = 0.7, 1.1, 1.4
QUANTIDADE_CHUVA = 2

# Ondas e dificuldade
DURACAO_ONDA = 20.0
INIMIGOS_POR_ONDA = [1, 1, 2, 3]          # da 4a onda em diante, 3
AUMENTO_VELOCIDADE_POR_ONDA = 0.08
AUMENTO_FREQUENCIA_POR_ONDA = 0.10
MULTIPLICADOR_VELOCIDADE_MAXIMO = 1.6
MULTIPLICADOR_FREQUENCIA_MAXIMO = 1.8
INTERVALO_SOLTO_INICIAL = 3.0
INTERVALO_SOLTO_MINIMO = 0.6
REDUCAO_INTERVALO_SOLTO = 0.03            # por segundo de partida

# Pontos e coletáveis
PONTOS_POR_SEGUNDO = 10
PONTOS_COLETAVEL = 50
BONUS_SOBREVIVENCIA = 200
INTERVALO_COLETAVEL = 4.0
DURACAO_COLETAVEL = 6.0
CHANCE_CURA = 0.15
TAMANHO_COLETAVEL = (32, 32)

# Som (volume de 0.0 a 1.0)
ARQUIVO_MUSICA = "musica.wav"
VOLUME_MUSICA = 0.2
VOLUME_EFEITOS = 0.35
