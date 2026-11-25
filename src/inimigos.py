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
        y = arena.area_de_surgimento().top
        projeteis = []
        for _ in range(cfg.QUANTIDADE_CHUVA):
            x = random.uniform(arena.rect.left + cfg.RAIO_PROJETIL,
                               arena.rect.right - cfg.RAIO_PROJETIL)
            projeteis.append(Projetil((x, y), (0, velocidade)))
        return projeteis


class InimigoLateral(Inimigo):
    """Atira na horizontal, vindo de um dos lados."""

    nome_imagem = "inimigo_lateral.png"
    intervalo = cfg.INTERVALO_LATERAL

    def atacar(self, arena: Arena, alvos: list, velocidade: float) -> list[Projetil]:
        area = arena.area_de_surgimento()
        y = random.uniform(arena.rect.top + cfg.RAIO_PROJETIL,
                           arena.rect.bottom - cfg.RAIO_PROJETIL)
        sentido = random.choice((1, -1))  # 1: vai para a direita; -1: para a esquerda
        x = area.left if sentido == 1 else area.right
        return [Projetil((x, y), (sentido * velocidade, 0))]


class InimigoMira(Inimigo):
    """Atira de onde está, mirando em um dos corações."""

    nome_imagem = "inimigo_mira.png"
    intervalo = cfg.INTERVALO_MIRA

    def atacar(self, arena: Arena, alvos: list, velocidade: float) -> list[Projetil]:
        if not alvos:
            return []
        alvo = random.choice(alvos)
        origem = pygame.math.Vector2(self.rect.center)
        caminho = alvo.posicao - origem
        if caminho.length_squared() == 0:
            return []
        # normalize() deixa o vetor com comprimento 1: sobra só a direção
        return [Projetil(origem, caminho.normalize() * velocidade)]


# Tipos que podem aparecer nas ondas. Para criar um inimigo novo, basta criar a
# classe (herdando de Inimigo) e colocá-la nesta lista.
TIPOS_INIMIGOS = [InimigoChuva, InimigoLateral, InimigoMira]
