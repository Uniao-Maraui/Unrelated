"""Os projéteis dos ataques."""

import pygame

from src import configuracoes as cfg


class Projetil(pygame.sprite.Sprite):
    """Um círculo que anda em linha reta.

    Todos os ataques usam esta mesma classe. O que muda de um ataque para outro
    é onde o projétil nasce e qual é a sua velocidade.
    """

    # Um pouco maior que a tela: fora dele o projétil não volta mais
    LIMITE = pygame.Rect(0, 0, cfg.LARGURA_TELA, cfg.ALTURA_TELA).inflate(200, 200)

    def __init__(self, posicao: tuple[float, float], velocidade: tuple[float, float]):
        super().__init__()
        self.posicao = pygame.math.Vector2(posicao)
        self.velocidade = pygame.math.Vector2(velocidade)  # pixels por segundo
        self.radius = cfg.RAIO_PROJETIL  # usado na colisão por círculos
        diametro = 2 * cfg.RAIO_PROJETIL
        self.image = pygame.Surface((diametro, diametro), pygame.SRCALPHA)
        pygame.draw.circle(self.image, cfg.BRANCO,
                           (cfg.RAIO_PROJETIL, cfg.RAIO_PROJETIL), cfg.RAIO_PROJETIL)
        self.rect = self.image.get_rect()
        self._atualizar_rect()

    def _atualizar_rect(self) -> None:
        self.rect.center = (round(self.posicao.x), round(self.posicao.y))

    def update(self, dt: float) -> None:
        self.posicao += self.velocidade * dt
        self._atualizar_rect()
        if not self.LIMITE.colliderect(self.rect):
            self.kill()  # sai de todos os grupos e deixa de existir
