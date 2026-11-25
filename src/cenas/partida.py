"""A tela em que a partida acontece."""

import pygame

from src import configuracoes as cfg
from src.arena import Arena
from src.cenas.cena import Cena
from src.coletaveis import GeradorColetaveis
from src.inimigos import TIPOS_INIMIGOS
from src.interface import HUD
from src.jogador import Jogador
from src.ondas import GerenciadorOndas
from src.regras import aplicar_danos, calcular_resultado, distribuir_coletaveis


class CenaPartida(Cena):
    """Reúne tudo o que existe numa partida e coordena cada quadro."""

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
        self.ondas = GerenciadorOndas(TIPOS_INIMIGOS, jogo.recursos, self.arena)
        self.projeteis = pygame.sprite.Group()
        self.gerador = GeradorColetaveis(jogo.recursos)
        self.coletaveis = pygame.sprite.Group()
        self.hud = HUD(pygame.font.Font(None, 32))

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            self.jogo.ir_para_menu()

    def atualizar(self, dt: float) -> None:
        teclas = pygame.key.get_pressed()
        self.arena.update(dt)
        for jogador in self.jogadores:
            jogador.update(dt, teclas, self.arena)
            if jogador.vivo:
                jogador.adicionar_pontos(cfg.PONTOS_POR_SEGUNDO * dt)
        self._criar_ataques(dt)
        self.projeteis.update(dt)
        self._atualizar_coletaveis(dt)
        # O dano vem antes: quem perdeu a última vida não coleta uma cura
        aplicar_danos(self.jogadores, self.projeteis)
        distribuir_coletaveis(self.jogadores, self.coletaveis)
        self._verificar_fim()

    def _criar_ataques(self, dt: float) -> None:
        vivos = [jogador for jogador in self.jogadores if jogador.vivo]
        self.projeteis.add(self.ondas.update(dt, vivos, len(self.projeteis)))

    def _atualizar_coletaveis(self, dt: float) -> None:
        novo = self.gerador.update(dt, self.arena)
        if novo is not None:
            self.coletaveis.add(novo)
        self.coletaveis.update(dt)
        for item in self.coletaveis:
            # Se a caixa encolher, o item é empurrado para dentro dela
            item.rect.clamp_ip(self.arena.rect)

    def _verificar_fim(self) -> None:
        """A partida acaba quando alguém perde todas as vidas."""
        if not all(jogador.vivo for jogador in self.jogadores):
            resultado = calcular_resultado(self.modo, self.jogadores)
            self.jogo.mostrar_game_over(resultado)

    def desenhar(self, tela: pygame.Surface) -> None:
        tela.fill(cfg.PRETO)
        self.ondas.inimigos.draw(tela)
        self.arena.desenhar(tela)
        self.coletaveis.draw(tela)
        self.projeteis.draw(tela)
        for jogador in self.jogadores:
            jogador.desenhar(tela)
        self.hud.desenhar(tela, self.jogadores)
