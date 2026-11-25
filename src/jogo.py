"""Janela, laço principal e troca de telas."""

import pygame

from src import configuracoes as cfg
from src.cenas.cena import Cena
from src.cenas.game_over import CenaGameOver
from src.cenas.menu import CenaMenu
from src.cenas.partida import CenaPartida
from src.recursos import Recursos
from src.regras import ResultadoPartida


class Jogo:
    """Dono da janela e do laço principal.

    É a única classe que conhece todas as telas. Quando uma tela quer trocar
    para outra, ela pede ao Jogo. Assim as telas não precisam importar umas
    às outras (o que causaria importação circular).
    """

    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((cfg.LARGURA_TELA, cfg.ALTURA_TELA))
        pygame.display.set_caption(cfg.TITULO)
        # Criado depois da janela: carregar imagens exige que ela exista
        self.recursos = Recursos()
        self.relogio = pygame.time.Clock()
        self.rodando = True
        self.cena: Cena = CenaMenu(self)

    def trocar_cena(self, nova: Cena) -> None:
        self.cena = nova

    def ir_para_menu(self) -> None:
        self.trocar_cena(CenaMenu(self))

    def iniciar_partida(self, modo: str) -> None:
        self.trocar_cena(CenaPartida(self, modo))

    def mostrar_game_over(self, resultado: ResultadoPartida) -> None:
        self.trocar_cena(CenaGameOver(self, resultado))

    def executar(self) -> None:
        """Repete até a janela ser fechada: eventos, lógica e desenho."""
        while self.rodando:
            # tick() limita a 60 quadros por segundo e devolve a duração do
            # último quadro em milissegundos. O limite evita um salto grande
            # quando a janela é arrastada ou o computador trava.
            dt = min(self.relogio.tick(cfg.FPS) / 1000, cfg.DT_MAXIMO)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False
                else:
                    self.cena.tratar_evento(evento)
            self.cena.atualizar(dt)
            self.cena.desenhar(self.tela)
            pygame.display.flip()
        pygame.quit()
