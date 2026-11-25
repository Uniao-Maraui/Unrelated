"""Controle das ondas de ataque e da dificuldade."""

import random

import pygame

from src import configuracoes as cfg
from src.arena import Arena
from src.inimigos import Inimigo
from src.projetil import Projetil
from src.recursos import Recursos


class GerenciadorOndas:
    """Decide quais inimigos atacam, e cria os projéteis soltos.

    Não sabe quais são os tipos de inimigo: recebe uma lista de classes e usa
    todas do mesmo jeito, chamando os métodos que vêm de Inimigo.
    """

    def __init__(self, tipos: list[type[Inimigo]], recursos: Recursos, arena: Arena):
        self.tipos = tipos
        self.recursos = recursos
        self.arena = arena
        self.indice_onda = 0  # a primeira onda é a de número 0
        self.tempo_total = 0.0
        self.tempo_na_onda = 0.0
        self.cronometro_solto = 0.0
        self.tipos_da_onda: list[type[Inimigo]] = []
        self.inimigos = pygame.sprite.Group()
        self._iniciar_onda()

    # Dificuldade

    def quantidade_inimigos(self, indice: int) -> int:
        posicao = min(indice, len(cfg.INIMIGOS_POR_ONDA) - 1)
        return min(len(self.tipos), cfg.INIMIGOS_POR_ONDA[posicao])

    def multiplicadores(self, indice: int) -> tuple[float, float]:
        """Devolve (velocidade, frequência). Crescem após a 4ª onda, até um limite."""
        nivel_extra = max(0, indice - (len(cfg.INIMIGOS_POR_ONDA) - 1))
        velocidade = min(1 + cfg.AUMENTO_VELOCIDADE_POR_ONDA * nivel_extra,
                         cfg.MULTIPLICADOR_VELOCIDADE_MAXIMO)
        frequencia = min(1 + cfg.AUMENTO_FREQUENCIA_POR_ONDA * nivel_extra,
                         cfg.MULTIPLICADOR_FREQUENCIA_MAXIMO)
        return velocidade, frequencia

    def velocidade_da_onda(self) -> float:
        multiplicador = self.multiplicadores(self.indice_onda)[0]
        return min(cfg.VELOCIDADE_PROJETIL * multiplicador, cfg.VELOCIDADE_MAXIMA_PROJETIL)

    def intervalo_solto(self, tempo: float) -> float:
        """Tempo entre projéteis soltos: diminui conforme a partida avança."""
        intervalo = cfg.INTERVALO_SOLTO_INICIAL - cfg.REDUCAO_INTERVALO_SOLTO * tempo
        return max(cfg.INTERVALO_SOLTO_MINIMO, intervalo)

    # Ondas

    def _sortear_tipos(self) -> list[type[Inimigo]]:
        quantidade = self.quantidade_inimigos(self.indice_onda)
        sorteados = random.sample(self.tipos, quantidade)  # sem repetir
        # Se há outras opções, não repete a formação da onda anterior
        while quantidade < len(self.tipos) and set(sorteados) == set(self.tipos_da_onda):
            sorteados = random.sample(self.tipos, quantidade)
        return sorteados

    def _iniciar_onda(self) -> None:
        self.tipos_da_onda = self._sortear_tipos()
        self.inimigos.empty()
        for tipo, posicao in zip(self.tipos_da_onda, cfg.POSICOES_INIMIGOS):
            imagem = self.recursos.imagem(tipo.nome_imagem, cfg.TAMANHO_INIMIGO)
            self.inimigos.add(tipo(imagem, posicao))

    def _avancar_onda(self) -> None:
        self.indice_onda += 1
        self.arena.mudar_tamanho()
        self._iniciar_onda()

    # Projéteis

    def criar_projetil_solto(self, velocidade: float) -> Projetil:
        """Nasce numa borda sorteada e atravessa um ponto sorteado da caixa."""
        area = self.arena.area_de_surgimento()
        lado = random.choice(("cima", "baixo", "esquerda", "direita"))
        if lado in ("cima", "baixo"):
            x = random.uniform(area.left, area.right)
            y = area.top if lado == "cima" else area.bottom
        else:
            x = area.left if lado == "esquerda" else area.right
            y = random.uniform(area.top, area.bottom)
        origem = pygame.math.Vector2(x, y)

        dentro = self.arena.rect.inflate(-10, -10)
        alvo = pygame.math.Vector2(random.uniform(dentro.left, dentro.right),
                                   random.uniform(dentro.top, dentro.bottom))
        rapidez = random.uniform(0.6 * cfg.VELOCIDADE_PROJETIL, velocidade)
        return Projetil(origem, (alvo - origem).normalize() * rapidez)

    def update(self, dt: float, alvos: list, total_projeteis: int) -> list[Projetil]:
        """Avança o tempo e devolve os projéteis criados neste quadro.

        total_projeteis é quantos já existem, para respeitar o limite máximo.
        """
        self.tempo_total += dt
        self.tempo_na_onda += dt
        if self.tempo_na_onda >= cfg.DURACAO_ONDA:
            self.tempo_na_onda -= cfg.DURACAO_ONDA
            self._avancar_onda()

        velocidade = self.velocidade_da_onda()
        frequencia = self.multiplicadores(self.indice_onda)[1]
        novos = []
        for inimigo in self.inimigos:
            novos.extend(inimigo.atualizar_ataque(
                dt, self.arena, alvos, velocidade, frequencia))

        self.cronometro_solto += dt
        if self.cronometro_solto >= self.intervalo_solto(self.tempo_total):
            self.cronometro_solto = 0.0
            novos.append(self.criar_projetil_solto(velocidade))

        vagas = max(0, cfg.MAXIMO_PROJETEIS - total_projeteis)
        return novos[:vagas]
