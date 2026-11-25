"""Tela inicial."""

import pygame

from src import configuracoes as cfg
from src.cenas.cena import Cena


class CenaMenu(Cena):
    """Menu inicial com o título do jogo."""

    def __init__(self, jogo):
        super().__init__(jogo)
        self.fonte_titulo = pygame.font.Font(None, 110)

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        pass

    def atualizar(self, dt: float) -> None:
        pass

    def desenhar(self, tela: pygame.Surface) -> None:
        tela.fill(cfg.PRETO)
        titulo = self.fonte_titulo.render(cfg.TITULO, True, cfg.BRANCO)
        tela.blit(titulo, titulo.get_rect(center=(cfg.LARGURA_TELA // 2, 160)))
