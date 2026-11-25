"""Carrega imagens e sons a partir da pasta do projeto."""

from pathlib import Path

import pygame

from src import configuracoes as cfg

# __file__ é este arquivo (src/recursos.py). Dois níveis acima fica a pasta do
# projeto. Assim nenhum caminho do computador fica escrito no código, e o jogo
# funciona de qualquer pasta em que for executado.
PASTA_PROJETO = Path(__file__).resolve().parent.parent
PASTA_IMAGENS = PASTA_PROJETO / "assets" / "imagens"
PASTA_SONS = PASTA_PROJETO / "assets" / "sons"


class Recursos:
    """Carrega cada arquivo uma única vez e o guarda para os próximos usos."""

    def __init__(self):
        self._imagens: dict[tuple, pygame.Surface] = {}
        self._sons: dict[str, pygame.mixer.Sound | None] = {}
        # Sem dispositivo de áudio o mixer não inicia, e o jogo fica em silêncio
        self.audio_disponivel = pygame.mixer.get_init() is not None

    def imagem(self, nome: str, tamanho: tuple[int, int]) -> pygame.Surface:
        """Devolve a imagem de assets/imagens já no tamanho pedido.

        Como ela é sempre redimensionada, um sprite trocado por outro de
        qualquer tamanho continua funcionando.
        """
        chave = (nome, tamanho)
        if chave not in self._imagens:
            caminho = PASTA_IMAGENS / nome
            if not caminho.is_file():
                raise FileNotFoundError(f"Imagem não encontrada: assets/imagens/{nome}")
            original = pygame.image.load(str(caminho)).convert_alpha()
            self._imagens[chave] = pygame.transform.scale(original, tamanho)
        return self._imagens[chave]

    # O som é um extra: ao contrário das imagens, se faltar, o jogo continua

    def tocar(self, nome: str) -> None:
        """Toca um efeito de assets/sons, se for possível."""
        if not self.audio_disponivel:
            return
        if nome not in self._sons:
            self._sons[nome] = self._carregar_som(nome)
        if self._sons[nome] is not None:
            self._sons[nome].play()

    def _carregar_som(self, nome: str) -> pygame.mixer.Sound | None:
        caminho = PASTA_SONS / nome
        if not caminho.is_file():
            return None
        try:
            som = pygame.mixer.Sound(str(caminho))
        except pygame.error:
            return None
        som.set_volume(cfg.VOLUME_EFEITOS)
        return som

    def iniciar_musica(self) -> None:
        """Toca a música de fundo em laço."""
        caminho = PASTA_SONS / cfg.ARQUIVO_MUSICA
        if not self.audio_disponivel or not caminho.is_file():
            return
        try:
            pygame.mixer.music.load(str(caminho))
            pygame.mixer.music.set_volume(cfg.VOLUME_MUSICA)
            pygame.mixer.music.play(-1)  # -1 repete para sempre
        except pygame.error:
            return
