"""Carrega as imagens a partir da pasta do projeto."""

from pathlib import Path

import pygame

# __file__ é este arquivo (src/recursos.py). Dois níveis acima fica a pasta do
# projeto. Assim nenhum caminho do computador fica escrito no código, e o jogo
# funciona de qualquer pasta em que for executado.
PASTA_PROJETO = Path(__file__).resolve().parent.parent
PASTA_IMAGENS = PASTA_PROJETO / "assets" / "imagens"
PASTA_SONS = PASTA_PROJETO / "assets" / "sons"


class Recursos:
    """Carrega cada imagem uma única vez e a guarda para os próximos usos."""

    def __init__(self):
        self._imagens: dict[tuple, pygame.Surface] = {}

    def imagem(self, nome: str, tamanho: tuple[int, int]) -> pygame.Surface:
        """Devolve a imagem de assets/imagens já no tamanho pedido.

        Como ela é sempre redimensionada, um sprite trocado por outro de
        qualquer tamanho continua funcionando.
        """
        chave = (nome, tamanho)
        if chave not in self._imagens:
            caminho = PASTA_IMAGENS / nome
            if not caminho.is_file():
                raise FileNotFoundError(f"Imagem não encontrada: assets/imagens/{nome}")
            original = pygame.image.load(str(caminho)).convert_alpha()
            self._imagens[chave] = pygame.transform.scale(original, tamanho)
        return self._imagens[chave]
