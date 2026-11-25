"""Cria imagens genéricas para o jogo. Este script NÃO faz parte do jogo.

Ele só cria os arquivos que ainda não existem. Para usar outro sprite, basta
substituir o PNG em assets/imagens mantendo o mesmo nome.

Uso, a partir da pasta do projeto:
    python ferramentas/gerar_recursos.py
"""

from pathlib import Path

import pygame

PASTA_IMAGENS = Path(__file__).resolve().parent.parent / "assets" / "imagens"

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


if __name__ == "__main__":
    gerar_imagens(PASTA_IMAGENS)
