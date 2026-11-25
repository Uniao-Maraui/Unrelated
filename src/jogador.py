"""O personagem controlado por uma pessoa."""

import pygame

from src import configuracoes as cfg
from src.arena import Arena


class Jogador(pygame.sprite.Sprite):
    """Um coração que se move dentro da arena.

    controles é uma lista de conjuntos de teclas. No Solo o jogador recebe os
    dois conjuntos (WASD e setas).
    """

    def __init__(self, nome: str, imagem: pygame.Surface, posicao: tuple[float, float],
                 controles: list[dict[str, int]]):
        super().__init__()
        self.nome = nome
        self.image = imagem
        self.rect = imagem.get_rect(center=posicao)
        # O Rect só guarda números inteiros. A posição exata fica no Vector2.
        self.posicao = pygame.math.Vector2(posicao)
        # O nome "radius" é o que o Pygame procura na colisão por círculos
        self.radius = cfg.RAIO_COLISAO_JOGADOR
        self.controles = controles

    def _apertou(self, teclas, acao: str) -> bool:
        return any(teclas[conjunto[acao]] for conjunto in self.controles)

    def calcular_direcao(self, teclas) -> pygame.math.Vector2:
        """Direção do movimento, sempre com comprimento 1 (ou 0, se parado)."""
        direcao = pygame.math.Vector2(0, 0)
        if self._apertou(teclas, "esquerda"):
            direcao.x -= 1
        if self._apertou(teclas, "direita"):
            direcao.x += 1
        if self._apertou(teclas, "cima"):
            direcao.y -= 1
        if self._apertou(teclas, "baixo"):
            direcao.y += 1
        if direcao.length_squared() > 0:
            # Sem isto, andar na diagonal seria cerca de 41% mais rápido
            direcao.normalize_ip()
        return direcao

    def update(self, dt: float, teclas, arena: Arena) -> None:
        # distância = direção x velocidade x tempo
        self.posicao += self.calcular_direcao(teclas) * cfg.VELOCIDADE_JOGADOR * dt
        self._manter_na_arena(arena)

    def _manter_na_arena(self, arena: Arena) -> None:
        self.rect.center = (round(self.posicao.x), round(self.posicao.y))
        dentro = self.rect.clamp(arena.rect)
        # Corrige só o eixo que bateu na borda, para o outro não perder as casas decimais
        if dentro.x != self.rect.x:
            self.posicao.x = dentro.centerx
        if dentro.y != self.rect.y:
            self.posicao.y = dentro.centery
        self.rect = dentro

    def desenhar(self, tela: pygame.Surface) -> None:
        tela.blit(self.image, self.rect)
