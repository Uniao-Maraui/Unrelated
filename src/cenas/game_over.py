"""A tela de fim de jogo."""

import pygame

from src import configuracoes as cfg
from src.cenas.cena import Cena
from src.interface import Botao, MenuBotoes
from src.regras import ResultadoPartida


class CenaGameOver(Cena):
    """Mostra o resultado e oferece jogar de novo ou voltar ao menu."""

    def __init__(self, jogo, resultado: ResultadoPartida):
        super().__init__(jogo)
        self.resultado = resultado
        self.fonte_titulo = pygame.font.Font(None, 100)
        self.fonte_texto = pygame.font.Font(None, 44)
        self.fonte_botao = pygame.font.Font(None, 44)
        centro_x = cfg.LARGURA_TELA // 2
        self.menu = MenuBotoes([
            Botao("Jogar Novamente", (centro_x, 390), self.jogar_novamente),
            Botao("Menu", (centro_x, 466), jogo.ir_para_menu),
        ])
        jogo.recursos.tocar("game_over.wav")

    def linhas_do_resultado(self) -> list[str]:
        """Os textos que explicam como a partida terminou."""
        resultado = self.resultado
        if resultado.modo != cfg.MODO_VERSUS:
            return [f"Pontuação: {resultado.pontos[0]}"]

        if resultado.vencedor is None:
            linhas = ["Empate!"]
        else:
            linhas = [f"{resultado.vencedor} venceu!"]
        placares = [f"Jogador {numero}: {pontos}"
                    for numero, pontos in enumerate(resultado.pontos, start=1)]
        linhas.append("    ".join(placares))
        if resultado.sobrevivente is not None:
            linhas.append(f"Bônus de sobrevivência: +{cfg.BONUS_SOBREVIVENCIA} "
                          f"para {resultado.sobrevivente}")
        return linhas

    def jogar_novamente(self) -> None:
        self.jogo.iniciar_partida(self.resultado.modo)

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            self.jogo.ir_para_menu()
        else:
            self.menu.tratar_evento(evento)

    def atualizar(self, dt: float) -> None:
        pass

    def desenhar(self, tela: pygame.Surface) -> None:
        tela.fill(cfg.PRETO)
        self._escrever(tela, "Game Over", self.fonte_titulo, 130)
        for indice, linha in enumerate(self.linhas_do_resultado()):
            self._escrever(tela, linha, self.fonte_texto, 230 + indice * 50)
        self.menu.desenhar(tela, self.fonte_botao)

    def _escrever(self, tela: pygame.Surface, texto: str,
                  fonte: pygame.font.Font, y: int) -> None:
        """Escreve um texto centralizado na horizontal."""
        imagem = fonte.render(texto, True, cfg.BRANCO)
        tela.blit(imagem, imagem.get_rect(center=(cfg.LARGURA_TELA // 2, y)))
