"""A tela em que a partida acontece."""

import pygame

from src import configuracoes as cfg
from src.arena import Arena
from src.cenas.cena import Cena
from src.jogador import Jogador


class CenaPartida(Cena):
    """Reúne a arena e os jogadores de uma partida."""

    def __init__(self, jogo, modo: str):
        super().__init__(jogo)
        self.modo = modo
        self.arena = Arena(cfg.CENTRO_ARENA, cfg.TAMANHOS_ARENA)
        imagem = jogo.recursos.imagem("jogador1.png", cfg.TAMANHO_JOGADOR)
        # No Solo valem os dois conjuntos de teclas
        self.jogadores = [
            Jogador("Jogador 1", imagem, cfg.CENTRO_ARENA,
                    [cfg.TECLAS_P1, cfg.TECLAS_P2]),
        ]

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            self.jogo.ir_para_menu()

    def atualizar(self, dt: float) -> None:
        teclas = pygame.key.get_pressed()
        for jogador in self.jogadores:
            jogador.update(dt, teclas, self.arena)

    def desenhar(self, tela: pygame.Surface) -> None:
        tela.fill(cfg.PRETO)
        self.arena.desenhar(tela)
        for jogador in self.jogadores:
            jogador.desenhar(tela)
