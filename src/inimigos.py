"""Os inimigos, que criam os ataques."""

import random
from abc import ABC, abstractmethod

import pygame

from src import configuracoes as cfg
from src.arena import Arena
from src.projetil import Projetil


class Inimigo(pygame.sprite.Sprite, ABC):
    """Base de todos os inimigos.

    Cada tipo define a sua imagem (nome_imagem), o seu ritmo (intervalo) e o
    seu jeito de atacar (método atacar). O resto é herdado daqui.
    """

    nome_imagem: str
    intervalo: float

    def __init__(self, imagem: pygame.Surface, posicao: tuple[int, int]):
        super().__init__()
        self.image = imagem
        self.rect = imagem.get_rect(center=posicao)
        self.cronometro = 0.0

    def atualizar_ataque(self, dt: float, arena: Arena, alvos: list,
                         velocidade: float, frequencia: float = 1.0) -> list[Projetil]:
        """Conta o tempo e ataca quando chega a hora.

        Devolve os projéteis criados neste quadro (quase sempre nenhum).
        Quanto maior a frequencia, mais rápido o cronômetro anda.
        """
        self.cronometro += dt * frequencia
        if self.cronometro < self.intervalo:
            return []
        self.cronometro -= self.intervalo
        return self.atacar(arena, alvos, velocidade)

    @abstractmethod
    def atacar(self, arena: Arena, alvos: list, velocidade: float) -> list[Projetil]:
        """Cria os projéteis de um ataque."""


class InimigoChuva(Inimigo):
    """Faz projéteis caírem do alto."""

    nome_imagem = "inimigo_chuva.png"
    intervalo = cfg.INTERVALO_CHUVA

    def atacar(self, arena: Arena, alvos: list, velocidade: float) -> list[Projetil]:
        y = arena.rect.top - cfg.MARGEM_SURGIMENTO
        projeteis = []
        for _ in range(cfg.QUANTIDADE_CHUVA):
            x = random.uniform(arena.rect.left + cfg.RAIO_PROJETIL,
                               arena.rect.right - cfg.RAIO_PROJETIL)
            projeteis.append(Projetil((x, y), (0, velocidade)))
        return projeteis
