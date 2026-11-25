"""Elementos de interface: botões e menus."""

from typing import Callable

import pygame

from src import configuracoes as cfg


class Botao:
    """Um retângulo com texto que executa uma ação quando é escolhido.

    A ação é uma função recebida na criação. Assim o botão não precisa saber
    o que ela faz, e a mesma classe serve para qualquer botão do jogo.
    """

    LARGURA, ALTURA = 280, 56

    def __init__(self, texto: str, centro: tuple[int, int], acao: Callable[[], None]):
        self.texto = texto
        self.acao = acao
        self.rect = pygame.Rect(0, 0, self.LARGURA, self.ALTURA)
        self.rect.center = centro

    def desenhar(self, tela: pygame.Surface, fonte: pygame.font.Font,
                 selecionado: bool) -> None:
        cor = cfg.AMARELO if selecionado else cfg.BRANCO
        pygame.draw.rect(tela, cor, self.rect, 3)
        texto = fonte.render(self.texto, True, cor)
        tela.blit(texto, texto.get_rect(center=self.rect.center))


class MenuBotoes:
    """Uma lista de botões que funciona com teclado e com mouse."""

    TECLAS_SUBIR = (pygame.K_UP, pygame.K_w)
    TECLAS_DESCER = (pygame.K_DOWN, pygame.K_s)
    TECLAS_CONFIRMAR = (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE)

    def __init__(self, botoes: list[Botao]):
        self.botoes = botoes
        self.selecionado = 0

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        if evento.type == pygame.KEYDOWN:
            self._tratar_tecla(evento.key)
        elif evento.type == pygame.MOUSEMOTION:
            indice = self._indice_em(evento.pos)
            if indice is not None:
                self.selecionado = indice
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            indice = self._indice_em(evento.pos)
            if indice is not None:
                self.selecionado = indice
                self.botoes[indice].acao()

    def _tratar_tecla(self, tecla: int) -> None:
        # O resto da divisão (%) faz a seleção "dar a volta" na lista
        if tecla in self.TECLAS_SUBIR:
            self.selecionado = (self.selecionado - 1) % len(self.botoes)
        elif tecla in self.TECLAS_DESCER:
            self.selecionado = (self.selecionado + 1) % len(self.botoes)
        elif tecla in self.TECLAS_CONFIRMAR:
            self.botoes[self.selecionado].acao()

    def _indice_em(self, posicao: tuple[int, int]) -> int | None:
        """Devolve o índice do botão que está sob a posição, se houver."""
        for indice, botao in enumerate(self.botoes):
            if botao.rect.collidepoint(posicao):
                return indice
        return None

    def desenhar(self, tela: pygame.Surface, fonte: pygame.font.Font) -> None:
        for indice, botao in enumerate(self.botoes):
            botao.desenhar(tela, fonte, indice == self.selecionado)
