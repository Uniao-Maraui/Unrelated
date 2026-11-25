"""Classe base das telas."""

from abc import ABC, abstractmethod

import pygame


class Cena(ABC):
    """Uma tela do jogo.

    É abstrata: não existe uma "cena genérica". Cada tela herda desta classe
    e é obrigada a implementar os três métodos abaixo.
    """

    def __init__(self, jogo):
        self.jogo = jogo

    @abstractmethod
    def tratar_evento(self, evento: pygame.event.Event) -> None:
        """Reage a um evento de teclado ou mouse."""

    @abstractmethod
    def atualizar(self, dt: float) -> None:
        """Avança a lógica da tela. dt é a duração do quadro em segundos."""

    @abstractmethod
    def desenhar(self, tela: pygame.Surface) -> None:
        """Desenha a tela."""
