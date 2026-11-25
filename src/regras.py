"""Regras da partida, separadas da tela para ficarem fáceis de ler."""

import pygame

from src.jogador import Jogador


def aplicar_danos(jogadores: list[Jogador],
                  projeteis: pygame.sprite.Group) -> list[Jogador]:
    """Aplica o dano de um quadro e devolve quem perdeu uma vida.

    Primeiro descobre todos os acertos e só depois remove os projéteis. Se um
    mesmo projétil tocar dois jogadores, os dois levam dano: quem é verificado
    primeiro não tem vantagem.
    """
    acertos = []
    for jogador in jogadores:
        if jogador.vivo and not jogador.invulneravel:
            tocados = pygame.sprite.spritecollide(
                jogador, projeteis, False, pygame.sprite.collide_circle)
            if tocados:
                acertos.append((jogador, tocados))

    atingidos = []
    for jogador, tocados in acertos:
        jogador.receber_dano()
        atingidos.append(jogador)
        for projetil in tocados:
            projetil.kill()
    return atingidos
