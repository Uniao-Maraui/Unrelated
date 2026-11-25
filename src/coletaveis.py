"""Os itens que aparecem na caixa para serem coletados."""

import random
from abc import ABC, abstractmethod

import pygame

from src import configuracoes as cfg
from src.arena import Arena
from src.jogador import Jogador
from src.recursos import Recursos


class Coletavel(pygame.sprite.Sprite, ABC):
    """Base dos itens. Cada tipo define o que acontece com quem o pega."""

    nome_imagem: str
    nome_som: str

    def __init__(self, imagem: pygame.Surface, posicao: tuple[int, int]):
        super().__init__()
        self.image = imagem
        self.rect = imagem.get_rect(center=posicao)
        self.radius = cfg.RAIO_COLISAO_COLETAVEL
        self.tempo_restante = cfg.DURACAO_COLETAVEL

    def update(self, dt: float) -> None:
        self.tempo_restante -= dt
        if self.tempo_restante <= 0:
            self.kill()

    @abstractmethod
    def aplicar(self, jogador: Jogador) -> None:
        """Dá o efeito do item para o jogador."""


class ColetavelPontos(Coletavel):
    """Item comum: dá pontos."""

    nome_imagem = "item_pontos.png"
    nome_som = "coleta.wav"

    def aplicar(self, jogador: Jogador) -> None:
        jogador.adicionar_pontos(cfg.PONTOS_COLETAVEL)


class ColetavelCura(Coletavel):
    """Item raro: devolve uma vida."""

    nome_imagem = "item_cura.png"
    nome_som = "cura.wav"

    def aplicar(self, jogador: Jogador) -> None:
        jogador.curar()


class GeradorColetaveis:
    """Cria um item de tempos em tempos."""

    def __init__(self, recursos: Recursos):
        self.recursos = recursos
        self.cronometro = 0.0

    def update(self, dt: float, arena: Arena) -> Coletavel | None:
        """Devolve o item criado neste quadro, ou None."""
        self.cronometro += dt
        if self.cronometro < cfg.INTERVALO_COLETAVEL:
            return None
        self.cronometro -= cfg.INTERVALO_COLETAVEL

        if random.random() < cfg.CHANCE_CURA:
            tipo = ColetavelCura
        else:
            tipo = ColetavelPontos
        # Só onde a caixa está agora e vai continuar, longe das bordas
        area = arena.rect.clip(arena.rect_alvo).inflate(-40, -40)
        posicao = (random.randint(area.left, area.right),
                   random.randint(area.top, area.bottom))
        imagem = self.recursos.imagem(tipo.nome_imagem, cfg.TAMANHO_COLETAVEL)
        return tipo(imagem, posicao)
