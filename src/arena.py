"""A caixa onde os corações se movem."""

import random

import pygame

from src import configuracoes as cfg


class Arena:
    """Um retângulo centralizado que muda de tamanho de tempos em tempos.

    rect é o tamanho atual e rect_alvo é o tamanho para onde ele está indo.
    """

    def __init__(self, centro: tuple[int, int], tamanhos: list[tuple[int, int]]):
        self.centro = centro
        self.tamanhos = tamanhos
        largura, altura = tamanhos[0]
        # Guardados com casas decimais para a transição ficar suave
        self.largura = float(largura)
        self.altura = float(altura)
        self.rect = self._criar_rect(largura, altura)
        self.rect_alvo = self._criar_rect(largura, altura)

    def _criar_rect(self, largura: int, altura: int) -> pygame.Rect:
        rect = pygame.Rect(0, 0, largura, altura)
        rect.center = self.centro
        return rect

    def mudar_tamanho(self) -> None:
        """Sorteia um novo destino, diferente do atual."""
        opcoes = [tamanho for tamanho in self.tamanhos if tamanho != self.rect_alvo.size]
        if opcoes:
            largura, altura = random.choice(opcoes)
            self.rect_alvo = self._criar_rect(largura, altura)

    def update(self, dt: float) -> None:
        passo = cfg.VELOCIDADE_TRANSICAO_ARENA * dt
        self.largura = self._aproximar(self.largura, self.rect_alvo.width, passo)
        self.altura = self._aproximar(self.altura, self.rect_alvo.height, passo)
        self.rect = self._criar_rect(round(self.largura), round(self.altura))

    def _aproximar(self, valor: float, alvo: float, passo: float) -> float:
        """Anda um passo na direção do alvo, sem ultrapassá-lo."""
        if valor < alvo:
            return min(valor + passo, alvo)
        return max(valor - passo, alvo)

    def area_de_surgimento(self) -> pygame.Rect:
        """Retângulo em cuja borda os projéteis podem nascer.

        Considera o tamanho atual e o de destino, com uma margem. Assim nenhum
        projétil nasce dentro da caixa, nem enquanto ela está mudando.
        """
        folga = 2 * cfg.MARGEM_SURGIMENTO
        return self.rect.union(self.rect_alvo).inflate(folga, folga)

    def desenhar(self, tela: pygame.Surface) -> None:
        # A borda é desenhada por fora para o espaço interno ser exatamente self.rect
        espessura = cfg.ESPESSURA_BORDA_ARENA
        borda = self.rect.inflate(2 * espessura, 2 * espessura)
        pygame.draw.rect(tela, cfg.BRANCO, borda, espessura)
