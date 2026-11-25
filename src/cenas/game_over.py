"""A tela de fim de jogo."""

import pygame

from src import configuracoes as cfg
from src.cenas.cena import Cena
from src.interface import Botao, MenuBotoes
from src.regras import ResultadoPartida


class CenaGameOver(Cena):
    """Mostra o resultado e oferece jogar de novo ou voltar ao menu."""

    def __init__(self, jogo, resultado: ResultadoPartida):
        super().__init__(jogo)
        self.resultado = resultado
        self.fonte_titulo = pygame.font.Font(None, 100)
        self.fonte_texto = pygame.font.Font(None, 52)
        self.fonte_botao = pygame.font.Font(None, 44)
        centro_x = cfg.LARGURA_TELA // 2
        self.menu = MenuBotoes([
            Botao("Jogar Novamente", (centro_x, 390), self.jogar_novamente),
            Botao("Menu", (centro_x, 466), jogo.ir_para_menu),
        ])

    def jogar_novamente(self) -> None:
        self.jogo.iniciar_partida(self.resultado.modo)

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            self.jogo.ir_para_menu()
        else:
            self.menu.tratar_evento(evento)

    def atualizar(self, dt: float) -> None:
        pass

    def desenhar(self, tela: pygame.Surface) -> None:
        tela.fill(cfg.PRETO)
        self._escrever(tela, "Game Over", self.fonte_titulo, 150)
        self._escrever(tela, f"Pontuação: {self.resultado.pontos[0]}", self.fonte_texto, 260)
        self.menu.desenhar(tela, self.fonte_botao)

    def _escrever(self, tela: pygame.Surface, texto: str,
                  fonte: pygame.font.Font, y: int) -> None:
        """Escreve um texto centralizado na horizontal."""
        imagem = fonte.render(texto, True, cfg.BRANCO)
        tela.blit(imagem, imagem.get_rect(center=(cfg.LARGURA_TELA // 2, y)))
