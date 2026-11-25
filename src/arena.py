"""A caixa onde os corações se movem."""

import pygame

from src import configuracoes as cfg


class Arena:
    """Um retângulo centralizado na tela."""

    def __init__(self, centro: tuple[int, int], tamanhos: list[tuple[int, int]]):
        self.centro = centro
        self.tamanhos = tamanhos
        largura, altura = tamanhos[0]
        self.rect = pygame.Rect(0, 0, largura, altura)
        self.rect.center = centro

    def desenhar(self, tela: pygame.Surface) -> None:
        # A borda é desenhada por fora para o espaço interno ser exatamente self.rect
        espessura = cfg.ESPESSURA_BORDA_ARENA
        borda = self.rect.inflate(2 * espessura, 2 * espessura)
        pygame.draw.rect(tela, cfg.BRANCO, borda, espessura)
