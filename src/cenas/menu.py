"""Tela inicial."""

import pygame

from src import configuracoes as cfg
from src.cenas.cena import Cena
from src.interface import Botao, MenuBotoes


class CenaMenu(Cena):
    """Menu com duas páginas: a inicial e a de escolha do modo."""

    def __init__(self, jogo):
        super().__init__(jogo)
        self.fonte_titulo = pygame.font.Font(None, 110)
        self.fonte_botao = pygame.font.Font(None, 44)
        self.mostrar_inicial()

    def mostrar_inicial(self) -> None:
        self.pagina = "inicial"
        centro_x = cfg.LARGURA_TELA // 2
        self.menu = MenuBotoes([
            Botao("Iniciar", (centro_x, 330), self.mostrar_modos),
        ])

    def mostrar_modos(self) -> None:
        self.pagina = "modo"
        centro_x = cfg.LARGURA_TELA // 2
        self.menu = MenuBotoes([
            Botao("Solo", (centro_x, 300),
                  lambda: self.jogo.iniciar_partida(cfg.MODO_SOLO)),
            Botao("Versus", (centro_x, 376),
                  lambda: self.jogo.iniciar_partida(cfg.MODO_VERSUS)),
            Botao("Voltar", (centro_x, 452), self.mostrar_inicial),
        ])

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        apertou_esc = evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE
        if apertou_esc and self.pagina == "modo":
            self.mostrar_inicial()
        else:
            self.menu.tratar_evento(evento)

    def atualizar(self, dt: float) -> None:
        pass

    def desenhar(self, tela: pygame.Surface) -> None:
        tela.fill(cfg.PRETO)
        titulo = self.fonte_titulo.render(cfg.TITULO, True, cfg.BRANCO)
        tela.blit(titulo, titulo.get_rect(center=(cfg.LARGURA_TELA // 2, 160)))
        self.menu.desenhar(tela, self.fonte_botao)
