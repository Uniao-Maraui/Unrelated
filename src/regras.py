"""Regras da partida, separadas da tela para ficarem fáceis de ler."""

import random
from dataclasses import dataclass

import pygame

from src.jogador import Jogador


@dataclass(frozen=True)
class ResultadoPartida:
    """O que sobra de uma partida para a tela de game over mostrar.

    É um dataclass congelado: guarda os dados e não pode ser alterado.
    """

    modo: str
    pontos: tuple[int, ...]
    vencedor: str | None
    sobrevivente: str | None


def calcular_resultado(modo: str, jogadores: list[Jogador]) -> ResultadoPartida:
    """Monta o resultado. Vencedor e bônus entram junto com o modo Versus."""
    pontos = tuple(int(jogador.pontos) for jogador in jogadores)
    return ResultadoPartida(modo, pontos, None, None)


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


def distribuir_coletaveis(jogadores: list[Jogador],
                          coletaveis: pygame.sprite.Group) -> list:
    """Entrega cada item tocado a um jogador e devolve os itens coletados.

    Se os dois encostarem no mesmo quadro, fica com quem estiver mais perto do
    centro do item. Se a distância for igual, há um sorteio.
    """
    coletados = []
    for item in list(coletaveis):
        candidatos = [jogador for jogador in jogadores
                      if jogador.vivo and pygame.sprite.collide_circle(jogador, item)]
        if not candidatos:
            continue
        distancias = [jogador.posicao.distance_to(item.rect.center)
                      for jogador in candidatos]
        menor = min(distancias)
        mais_proximos = [jogador for jogador, distancia in zip(candidatos, distancias)
                         if distancia == menor]
        item.aplicar(random.choice(mais_proximos))
        item.kill()
        coletados.append(item)
    return coletados
