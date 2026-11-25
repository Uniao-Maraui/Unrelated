"""Cria imagens e sons genéricos para o jogo. Este script NÃO faz parte do jogo.

Ele só cria os arquivos que ainda não existem. Para usar outro sprite ou som,
basta substituir o arquivo em assets mantendo o mesmo nome.

Uso, a partir da pasta do projeto:
    python ferramentas/gerar_recursos.py
"""

import math
import wave
from pathlib import Path

import pygame

PASTA_ASSETS = Path(__file__).resolve().parent.parent / "assets"
PASTA_IMAGENS = PASTA_ASSETS / "imagens"
PASTA_SONS = PASTA_ASSETS / "sons"

# Cada letra dos desenhos é uma cor; o ponto é transparente
CORES = {
    "R": (230, 40, 40),
    "A": (50, 110, 255),
    "C": (110, 200, 255),
    "P": (170, 90, 220),
    "L": (255, 140, 30),
    "Y": (255, 220, 0),
    "G": (60, 210, 90),
    "W": (255, 255, 255),
    "K": (20, 20, 20),
}

CORACAO = [
    "................",
    "..XXXX....XXXX..",
    ".XXXXXX..XXXXXX.",
    "XXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXX",
    ".XXXXXXXXXXXXXX.",
    "..XXXXXXXXXXXX..",
    "...XXXXXXXXXX...",
    "....XXXXXXXX....",
    ".....XXXXXX.....",
    "......XXXX......",
    ".......XX.......",
    "................",
    "................",
]

NUVEM = [
    "................",
    "......CCCC......",
    "....CCCCCCCC....",
    "...CCCCCCCCCC...",
    ".CCCCCCCCCCCCCC.",
    "CCCCCCCCCCCCCCCC",
    "CCCKKCCCCCCKKCCC",
    "CCCKKCCCCCCKKCCC",
    "CCCCCCCCCCCCCCCC",
    "CCCCCKKKKKKCCCCC",
    ".CCCCCCCCCCCCCC.",
    "..CCCCCCCCCCCC..",
    "................",
    "..C....C....C...",
    "..C....C....C...",
    "................",
]

CRIATURA = [
    "................",
    "....PPPPPPPP....",
    "...PPPPPPPPPP...",
    "P..PPPPPPPPPP..P",
    "PP.PWWPPPPWWP.PP",
    "PPPPWKPPPPKWPPPP",
    "PPPPPPPPPPPPPPPP",
    "PP.PPPPPPPPPP.PP",
    "P..PPKKKKKKPP..P",
    "...PPKWKWKKPP...",
    "...PPPPPPPPPP...",
    "....PPPPPPPP....",
    "....PP....PP....",
    "...PPP....PPP...",
    "................",
    "................",
]

OLHO = [
    "................",
    ".....LLLLLL.....",
    "...LLLLLLLLLL...",
    "..LLLWWWWWWLLL..",
    ".LLWWWWWWWWWWLL.",
    ".LWWWWRRRRWWWWL.",
    "LLWWWRRKKRRWWWLL",
    "LLWWWRKKKKRWWWLL",
    "LLWWWRKKKKRWWWLL",
    "LLWWWRRKKRRWWWLL",
    ".LWWWWRRRRWWWWL.",
    ".LLWWWWWWWWWWLL.",
    "..LLLWWWWWWLLL..",
    "...LLLLLLLLLL...",
    ".....LLLLLL.....",
    "................",
]

ESTRELA = [
    "................",
    ".......YY.......",
    ".......YY.......",
    "......YYYY......",
    "......YYYY......",
    "YYYYYYYYYYYYYYYY",
    ".YYYYYYYYYYYYYY.",
    "..YYYYYYYYYYYY..",
    "...YYYYYYYYYY...",
    "....YYYYYYYY....",
    "...YYYYYYYYYY...",
    "...YYYY..YYYY...",
    "..YYYY....YYYY..",
    "..YY........YY..",
    "................",
    "................",
]

CRUZ = [
    "................",
    ".....WWWWWW.....",
    ".....WGGGGW.....",
    ".....WGGGGW.....",
    ".....WGGGGW.....",
    ".WWWWWGGGGWWWWW.",
    ".WGGGGGGGGGGGGW.",
    ".WGGGGGGGGGGGGW.",
    ".WGGGGGGGGGGGGW.",
    ".WGGGGGGGGGGGGW.",
    ".WWWWWGGGGWWWWW.",
    ".....WGGGGW.....",
    ".....WGGGGW.....",
    ".....WGGGGW.....",
    ".....WWWWWW.....",
    "................",
]

# nome do arquivo -> desenho
IMAGENS = {
    "jogador1.png": [linha.replace("X", "R") for linha in CORACAO],
    "jogador2.png": [linha.replace("X", "A") for linha in CORACAO],
    "inimigo_chuva.png": NUVEM,
    "inimigo_lateral.png": CRIATURA,
    "inimigo_mira.png": OLHO,
    "item_pontos.png": ESTRELA,
    "item_cura.png": CRUZ,
}


def criar_superficie(desenho: list[str]) -> pygame.Surface:
    """Transforma um desenho em texto numa imagem com fundo transparente."""
    superficie = pygame.Surface((len(desenho[0]), len(desenho)), pygame.SRCALPHA)
    for y, linha in enumerate(desenho):
        for x, letra in enumerate(linha):
            if letra != ".":
                superficie.set_at((x, y), CORES[letra])
    return superficie


def gerar_imagens(pasta: Path) -> None:
    """Cria na pasta apenas as imagens que faltam."""
    pasta.mkdir(parents=True, exist_ok=True)
    for nome, desenho in IMAGENS.items():
        caminho = pasta / nome
        if caminho.exists():
            print(f"mantido: {nome}")
        else:
            pygame.image.save(criar_superficie(desenho), str(caminho))
            print(f"criado:  {nome}")


# Sons

TAXA = 22050  # amostras por segundo
SUAVIZACAO = 110  # amostras (5 ms) para o som não "estalar" no começo e no fim


def criar_melodia() -> list[tuple[int, float]]:
    """Quatro acordes tocados nota por nota, para repetir em laço."""
    acordes = [(220, 262, 330, 440), (196, 247, 294, 392),
               (175, 220, 262, 349), (165, 208, 247, 330)]
    notas = []
    for acorde in acordes:
        for indice in (0, 1, 2, 3, 2, 1, 2, 1):
            notas.append((acorde[indice], 0.2))
    return notas


# nome do arquivo -> (volume, lista de notas como (frequência em Hz, segundos))
SONS = {
    "dano.wav": (0.30, [(220, 0.07), (150, 0.07), (100, 0.10)]),
    "coleta.wav": (0.25, [(988, 0.05), (1319, 0.10)]),
    "cura.wav": (0.25, [(523, 0.08), (659, 0.08), (784, 0.08), (1047, 0.14)]),
    "game_over.wav": (0.25, [(392, 0.18), (330, 0.18), (262, 0.18), (196, 0.45)]),
    "musica.wav": (0.12, criar_melodia()),
}


def criar_amostras(notas: list[tuple[int, float]], volume: float) -> bytes:
    """Transforma as notas em uma onda quadrada, com som de videogame antigo."""
    dados = bytearray()
    for frequencia, duracao in notas:
        total = int(TAXA * duracao)
        for i in range(total):
            onda = 1 if math.sin(2 * math.pi * frequencia * i / TAXA) >= 0 else -1
            envelope = min(1, i / SUAVIZACAO, (total - i) / SUAVIZACAO)
            valor = int(32767 * volume * onda * envelope)
            dados += valor.to_bytes(2, "little", signed=True)
    return bytes(dados)


def gerar_sons(pasta: Path) -> None:
    """Cria na pasta apenas os sons que faltam."""
    pasta.mkdir(parents=True, exist_ok=True)
    for nome, (volume, notas) in SONS.items():
        caminho = pasta / nome
        if caminho.exists():
            print(f"mantido: {nome}")
            continue
        with wave.open(str(caminho), "wb") as arquivo:
            arquivo.setnchannels(1)   # mono
            arquivo.setsampwidth(2)   # 16 bits
            arquivo.setframerate(TAXA)
            arquivo.writeframes(criar_amostras(notas, volume))
        print(f"criado:  {nome}")


if __name__ == "__main__":
    gerar_imagens(PASTA_IMAGENS)
    gerar_sons(PASTA_SONS)
