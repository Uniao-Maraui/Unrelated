# Unrelated - Plano de Execução

> **Para agentes de código:** SUB-SKILL OBRIGATÓRIA: use `superpowers:executing-plans` para executar este plano, uma etapa por vez. Os passos usam caixas de seleção (`- [ ]`). Pare ao fim de cada etapa e espere a aprovação da dupla.

**Objetivo:** criar um arcade bullet hell 2D em Pygame, no estilo das batalhas de Undertale e Deltarune, com modos Solo e Versus local, que atenda a todos os requisitos do Trabalho Final de POO (UFPI).

**Arquitetura:** uma classe para cada tela (`CenaMenu`, `CenaPartida`, `CenaGameOver`), todas herdando de `Cena`. A classe `Jogo` mantém o laço principal e é a única que conhece todas as telas. Os elementos da partida ficam em classes e módulos separados.

**Tecnologias:** Python 3.15, `pygame-ce` 2.5.8 e `unittest` (biblioteca padrão do Python).

**Especificação:** Parte 1 deste documento. O enunciado original é o arquivo "Especificação do Trabalho Final - Pygame.pdf".

---

# Parte 1 - Descrição do jogo

## 1.1 Contexto e intenção

Trabalho final da disciplina de Programação Orientada a Objetos (2026.2), feito em dupla, com prazo de até 2 semanas. A avaliação é uma apresentação presencial, com o jogo funcionando, e a análise do código junto à dupla para verificar POO e modularização. As duas pessoas precisam dominar todo o código.

O jogo usa apenas a parte de desviar de projéteis das batalhas de Undertale e Deltarune, sem aventura e sem turnos.

## 1.2 Objetivos e limites

**Objetivos**
- Atender aos 8 requisitos do PDF.
- Ter modo Solo e modo Versus local.
- Ter código simples o bastante para a dupla explicar na apresentação.

**Fora do escopo**
- História, exploração e combate por turnos.
- Modo cooperativo, controle (gamepad) e jogo online.
- Habilidades (dash, movimento lento, graze, modo com gravidade).
- Recordes salvos em arquivo.
- Telas de pausa, "como jogar" e opções.

**O que faria o projeto falhar, mesmo funcionando**
- Código complexo demais para explicar.
- Uso de imagens ou músicas originais de Undertale ou Deltarune.
- Ataques injustos com frequência, sem espaço para desviar.

## 1.3 Requisitos do PDF

| # | Exigência | Como o jogo atende | Etapa |
|---|---|---|---|
| 1 | Equipe de até 2 alunos que dominam todo o código | Cada etapa termina com explicação e perguntas de estudo para as duas pessoas | Todas |
| 2 | POO para jogador, inimigos, projéteis e interface | `Jogador`, `Inimigo` e subclasses, `Projetil`, `Botao`, `MenuBotoes`, `HUD` | 2 a 8 |
| 3 | Código separado em módulos | `main.py`, `configuracoes.py`, `jogador.py`, `inimigos.py` e demais módulos | 1 em diante |
| 4 | Progresso na tela em tempo real | Pontuação no HUD | 5 |
| 5 | Tela inicial com título e botão de início | Título "Unrelated" e botão "Iniciar" | 2 |
| 6 | Vidas ou HP e fim de jogo | 3 corações e tela de game over com "Jogar Novamente" | 4 e 5 |
| 7 | No mínimo 2 sprites (jogador e inimigo) | Arquivos PNG carregados com `pygame.image.load` | 3 e 4 |
| 8 | `pygame.time.Clock` e caminhos relativos | 60 quadros por segundo; caminhos calculados a partir da pasta do projeto | 1 e 3 |

Ao fim da Etapa 5, a versão Solo já deve atender aos requisitos 2 a 8.

## 1.4 Regras do jogo

### Telas
- **Menu:** título "Unrelated" e botão "Iniciar", que leva à escolha entre "Solo", "Versus" e "Voltar". Funciona com mouse e teclado (setas ou W/S para escolher; Enter ou Espaço para confirmar).
- **Partida:** caixa central, inimigos acima da caixa e HUD com corações e pontos na parte de baixo.
- **Game over:** botões "Jogar Novamente" (mesmo modo) e "Menu". No Versus, mostra o resultado, os dois placares e quem recebeu o bônus.
- **ESC:** durante a partida, abandona o jogo e volta ao menu inicial.

### Jogadores
- 3 corações. Cada hit tira 1.
- Após um hit, o personagem fica invulnerável por 2 segundos e pisca.
- O movimento é livre e sempre dentro da caixa.
- No Versus, o jogador 1 usa WASD e o jogador 2 usa as setas, no mesmo teclado. Um coração atravessa o outro.

### Arena
- A caixa é sempre um retângulo centralizado.
- A cada nova onda, a largura e a altura mudam suavemente para outro tamanho pré-definido. Não há rotação nem formas irregulares.

### Inimigos e ataques
- Três tipos iniciais, que ainda podem mudar:
  - `InimigoChuva`: projéteis caem do alto.
  - `InimigoLateral`: projéteis vêm dos lados.
  - `InimigoMira`: projéteis miram em um coração. No Versus, o alvo é sorteado.
- Os ataques vêm em ondas que se somam: a primeira e a segunda têm 1 inimigo, a terceira tem 2 e, da quarta em diante, os 3 atacam juntos.
- Desde o início há também projéteis soltos, com origem e direção aleatórias. Começam raros e ficam mais frequentes com o tempo.
- A dificuldade não tem fim. Depois que os 3 tipos atacam juntos, os ataques ficam mais rápidos e frequentes, até um limite.
- Para reduzir situações impossíveis, os projéteis surgem fora da caixa, e a velocidade e a quantidade têm limites máximos. Isso reduz o risco, mas não garante que ele nunca aconteça.
- Um projétil que causa dano desaparece. Um projétil atravessa quem está invulnerável.

### Pontos, coletáveis e vitória
- Cada jogador ganha pontos por segundo vivo e ao pegar itens.
- Item comum: dá pontos.
- Item raro: cura 1 coração, até o máximo de 3. Com 3 corações, o item é consumido sem efeito, o que permite negá-lo ao adversário.
- No Versus, o item fica com quem encostar primeiro.
- A partida acaba quando alguém perde os 3 corações.
- No Versus, quem sobreviveu recebe um bônus. Vence quem tiver mais pontos.
- Pontos iguais dão empate. Se os dois perderem o último coração ao mesmo tempo, ninguém recebe o bônus.

### Imagens e som
- O visual ainda está em decisão: uma mistura de imagens geradas pelo Claude, desenhadas pela dupla e sprites gratuitos.
- O projeto começa com PNGs provisórios gerados por um script. Para trocar uma imagem, basta substituir o arquivo mantendo o nome.
- Haverá efeitos sonoros e música.
- Para qualquer imagem ou som baixado da internet, conferir se a licença permite o uso e anotar a fonte no `README.md`.

## 1.5 Abordagens de arquitetura consideradas

| Abordagem | Vantagem | Desvantagem | Decisão |
|---|---|---|---|
| A. Uma classe para cada tela | Cada tela cuida de si; deixa POO e modularização claras | Mais arquivos; é preciso entender a troca de telas | **Escolhida** |
| B. Um único laço com `if`/`elif` para o estado | Mais direta de entender no começo | A classe `Jogo` cresce e mistura as telas | Não escolhida |
| C. Personagens montados com componentes | Muito flexível | Difícil de explicar e exagerada para o prazo | Descartada |

## 1.6 Decisões tomadas ao escrever o plano (a dupla deve conferir)

Estes pontos não foram discutidos antes. Qualquer um pode ser alterado.

1. Valores iniciais de tempo, velocidade e pontos: os listados em 2.3. Todos ficam em `configuracoes.py` e serão ajustados com testes.
2. Cada onda dura 20 segundos, como no exemplo aprovado. A quantidade de inimigos segue o exemplo (1, 1, 2, 3), mas os tipos são sorteados.
3. No Solo, WASD e setas funcionam.
4. Fora da partida, ESC volta da escolha de modo para o menu inicial e do game over para o menu.
5. Se os dois encostarem no mesmo item no mesmo quadro, fica com quem estiver mais perto do centro do item. Se a distância for igual, há sorteio.
6. Há testes automáticos simples na pasta `testes/`. Eles não fazem parte do jogo e servem para conferir cada etapa.
7. O código usa apenas recursos que também existem no Pygame clássico. Assim, se o professor não aceitar o `pygame-ce`, a troca de biblioteca deve exigir pouca ou nenhuma mudança no código.
8. O script de imagens e sons provisórios nunca sobrescreve um arquivo existente.

## 1.7 O que fica a critério de quem implementar

Cores, tamanhos de fonte, espaçamento dos textos, desenho das imagens provisórias e melodia dos sons provisórios.

---

# Parte 2 - Plano de execução

## 2.1 Restrições globais

- Biblioteca: `pygame-ce==2.5.8`, importada com `import pygame`. O pacote para Python 3.15 no Windows foi conferido em 25/11/2026. As duas pessoas devem usar a mesma versão.
- Usar apenas recursos que também existem no Pygame clássico (não usar `pygame.FRect`, por exemplo).
- Janela de 800 x 600, 60 quadros por segundo, com `pygame.time.Clock`.
- Nenhum caminho absoluto escrito no código. Imagens e sons são localizados a partir de `Path(__file__)`, o que mantém os caminhos relativos à pasta do projeto, de onde quer que o jogo seja executado.
- Textos do jogo e nomes no código em português, sem acentos nos nomes de arquivos, classes, métodos e variáveis.
- Valores ajustáveis ficam somente em `src/configuracoes.py`.
- Somente `src/jogo.py` importa as telas concretas. Uma tela pede a troca chamando um método de `Jogo`. Isso evita importação circular.
- Sprites usam o método `update()`, nome que o Pygame espera. Telas usam `tratar_evento()`, `atualizar()` e `desenhar()`.
- Não usar imagens, sons ou músicas originais de Undertale ou Deltarune.
- Testes: `python -m unittest discover -s testes -t . -v`.
- Pelo menos um commit por etapa. Enviar ao GitHub após a aprovação da etapa pela dupla.

## 2.2 Pontos de atenção

Falhas que o plano precisa evitar, cada uma coberta por testes na etapa indicada.

| Situação | Comportamento esperado | Etapa |
|---|---|---|
| A janela é arrastada ou o computador trava por um instante | O passo de tempo é limitado a 0,05 s, para os projéteis não saltarem por cima dos corações | 1 |
| Os dois jogadores são atingidos no mesmo quadro, até pelo mesmo projétil | Ambos levam dano; o fim da partida é avaliado depois | 4 e 8 |
| Os dois encostam no mesmo item no mesmo quadro | O jogador 1 não tem preferência: vale a distância e, em empate, sorteio | 7 |
| A caixa muda de tamanho | Nenhum projétil nasce dentro dela e os itens continuam alcançáveis | 6 e 7 |
| O computador não tem áudio, ou uma imagem é trocada por outra de tamanho diferente | O jogo roda sem som; a imagem é redimensionada | 3 e 9 |

## 2.3 Valores iniciais (`src/configuracoes.py`)

```python
# Tela
LARGURA_TELA, ALTURA_TELA = 800, 600
FPS = 60
DT_MAXIMO = 0.05
TITULO = "Unrelated"

# Cores
PRETO, BRANCO = (0, 0, 0), (255, 255, 255)
AMARELO, CINZA = (255, 220, 0), (120, 120, 120)

# Modos e controles
MODO_SOLO, MODO_VERSUS = "solo", "versus"
TECLAS_P1 = {"cima": pygame.K_w, "baixo": pygame.K_s,
             "esquerda": pygame.K_a, "direita": pygame.K_d}
TECLAS_P2 = {"cima": pygame.K_UP, "baixo": pygame.K_DOWN,
             "esquerda": pygame.K_LEFT, "direita": pygame.K_RIGHT}

# Jogador (velocidades em pixels por segundo, tempos em segundos)
VIDAS_MAXIMAS = 3
TEMPO_INVULNERAVEL = 2.0
INTERVALO_PISCAR = 0.1
VELOCIDADE_JOGADOR = 220
TAMANHO_JOGADOR = (24, 24)
RAIO_COLISAO_JOGADOR = 8

# Arena
CENTRO_ARENA = (400, 330)
TAMANHOS_ARENA = [(480, 300), (360, 260), (600, 220), (300, 300)]
VELOCIDADE_TRANSICAO_ARENA = 200
ESPESSURA_BORDA_ARENA = 4

# Projéteis
RAIO_PROJETIL = 6
VELOCIDADE_PROJETIL = 150
VELOCIDADE_MAXIMA_PROJETIL = 260
MARGEM_SURGIMENTO = 90
MAXIMO_PROJETEIS = 60

# Inimigos
TAMANHO_INIMIGO = (64, 64)
POSICOES_INIMIGOS = [(400, 70), (230, 70), (570, 70)]
INTERVALO_CHUVA, INTERVALO_LATERAL, INTERVALO_MIRA = 0.7, 1.1, 1.4
QUANTIDADE_CHUVA = 2

# Ondas e dificuldade
DURACAO_ONDA = 20.0
INIMIGOS_POR_ONDA = [1, 1, 2, 3]          # da 4a onda em diante, 3
AUMENTO_VELOCIDADE_POR_ONDA = 0.08
AUMENTO_FREQUENCIA_POR_ONDA = 0.10
MULTIPLICADOR_VELOCIDADE_MAXIMO = 1.6
MULTIPLICADOR_FREQUENCIA_MAXIMO = 1.8
INTERVALO_SOLTO_INICIAL = 3.0
INTERVALO_SOLTO_MINIMO = 0.6
REDUCAO_INTERVALO_SOLTO = 0.03            # por segundo de partida

# Pontos e coletáveis
PONTOS_POR_SEGUNDO = 10
PONTOS_COLETAVEL = 50
BONUS_SOBREVIVENCIA = 200
INTERVALO_COLETAVEL = 4.0
DURACAO_COLETAVEL = 6.0
CHANCE_CURA = 0.15
TAMANHO_COLETAVEL = (20, 20)
RAIO_COLISAO_COLETAVEL = 10
```

## 2.4 Estrutura de arquivos

```
Unrelated/
|-- main.py                  inicia o jogo
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- src/
|   |-- __init__.py
|   |-- configuracoes.py     valores ajustáveis
|   |-- jogo.py              Jogo: laço principal e troca de telas
|   |-- recursos.py          Recursos: carrega imagens e sons
|   |-- interface.py         Botao, MenuBotoes, HUD
|   |-- arena.py             Arena
|   |-- jogador.py           Jogador
|   |-- projetil.py          Projetil
|   |-- inimigos.py          Inimigo e os 3 tipos
|   |-- coletaveis.py        Coletavel, os 2 tipos e GeradorColetaveis
|   |-- ondas.py             GerenciadorOndas
|   |-- regras.py            dano, coleta e resultado
|   `-- cenas/
|       |-- __init__.py
|       |-- cena.py          Cena (classe base)
|       |-- menu.py          CenaMenu
|       |-- partida.py       CenaPartida
|       `-- game_over.py     CenaGameOver
|-- assets/
|   |-- imagens/
|   `-- sons/
|-- ferramentas/
|   |-- __init__.py
|   `-- gerar_recursos.py    cria imagens e sons provisórios
|-- testes/
`-- documentacao/
```

## 2.5 Onde os conceitos de POO aparecem

| Conceito | Onde |
|---|---|
| Herança | `Cena` -> 3 telas; `Inimigo` -> 3 tipos; `Coletavel` -> 2 tipos; `pygame.sprite.Sprite` -> sprites |
| Polimorfismo | `cena.atualizar()`, `inimigo.atacar()`, `item.aplicar()` |
| Abstração | `Cena`, `Inimigo` e `Coletavel` usam `ABC` e `@abstractmethod` |
| Encapsulamento | Vidas e pontos do `Jogador` são lidos por propriedades e alterados só por métodos |
| Composição | `CenaPartida` é formada por arena, jogadores, projéteis, itens, ondas e HUD |

Todos os projéteis usam a mesma classe `Projetil` e andam em linha reta. Entre os ataques, mudam apenas o ponto de partida e a velocidade (direção e rapidez).

## 2.6 Cronograma

Os dias são contados a partir do início da implementação.

| Dias | Etapas | Resultado |
|---|---|---|
| 1 e 2 | 1 e 2 | Janela e menu |
| 3 a 5 | 3, 4 e 5 | **Marco:** Solo atende aos requisitos 2 a 8 |
| 6 a 8 | 6 e 7 | Ondas, 3 inimigos e coletáveis |
| 9 e 10 | 8 | Versus |
| 11 | 9 | Som |
| 12 a 14 | 10 | Revisão, estudo e folga para imprevistos |

**Se o prazo apertar**, cortar nesta ordem, com o aval da dupla: artes finais (ficam as provisórias), música e transição suave da caixa (a troca passa a ser imediata).

## 2.7 Ciclo de cada etapa

1. Claude escreve os testes e confirma que falham.
2. Claude implementa e confirma que todos os testes passam, inclusive os anteriores.
3. Claude explica as classes e os métodos da etapa.
4. A dupla executa o jogo, lê o código e responde às perguntas de estudo. Sugestão: uma pessoa explica para a outra, alternando a cada etapa.
5. Com a aprovação da dupla, o commit é enviado ao GitHub e começa a próxima etapa.

---

## Etapa 1: Janela, laço principal e base das telas

**Arquivos:**
- Criar: `requirements.txt`, `.gitignore`, `main.py`, `src/__init__.py`, `src/configuracoes.py`, `src/jogo.py`, `src/cenas/__init__.py`, `src/cenas/cena.py`, `src/cenas/menu.py`
- Testes: `testes/__init__.py`, `testes/test_jogo.py`

**Interfaces produzidas:**
- `Cena(ABC)`: `__init__(self, jogo)`; métodos abstratos `tratar_evento(evento)`, `atualizar(dt: float)`, `desenhar(tela: pygame.Surface)`.
- `Jogo`: atributos `tela`, `relogio`, `cena`, `rodando`; `calcular_dt(milissegundos: int) -> float` (estático); `trocar_cena(nova: Cena)`; `ir_para_menu()`; `executar()`.
- `CenaMenu(Cena)`: nesta etapa, apenas desenha o título.
- `configuracoes.py`: todos os valores da seção 2.3.

- [ ] **Passo 1: Preparar o ambiente.** `requirements.txt` com `pygame-ce==2.5.8`; `.gitignore` com `__pycache__/`, `*.pyc` e `.venv/`. Executar `python -m pip install -r requirements.txt`.
- [ ] **Passo 2: Escrever os testes.**

`testes/__init__.py`:

```python
import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame

pygame.init()
pygame.display.set_mode((800, 600))
```

`testes/test_jogo.py`:

```python
class TesteJogo(unittest.TestCase):
    def test_passo_de_tempo_normal(self):
        self.assertAlmostEqual(Jogo.calcular_dt(16), 0.016)

    def test_passo_de_tempo_limitado_quando_a_janela_trava(self):
        self.assertEqual(Jogo.calcular_dt(2000), cfg.DT_MAXIMO)
```

- [ ] **Passo 3: Executar os testes.** Esperado: falha, porque `src.jogo` não existe.
- [ ] **Passo 4: Implementar.** O laço de `executar()` segue a ordem: `dt = calcular_dt(relogio.tick(FPS))`, eventos (`QUIT` põe `rodando = False`; os demais vão para `cena.tratar_evento`), `cena.atualizar(dt)`, `cena.desenhar(tela)`, `pygame.display.flip()`. Ao sair do laço, chamar `pygame.quit()`. `main.py` cria `Jogo()` e chama `executar()` dentro de `if __name__ == "__main__":`.
- [ ] **Passo 5: Executar os testes.** Esperado: todos passam.
- [ ] **Passo 6: Conferir manualmente.** `python main.py` abre uma janela 800 x 600 com o título; o X fecha sem erro.
- [ ] **Passo 7: Commit.** `feat: janela, laco principal e base das telas`

**A dupla deve saber explicar:** O que o `Clock` faz? O que é `dt` e por que é limitado? Por que `Cena` é uma classe abstrata?

---

## Etapa 2: Menu inicial

**Arquivos:**
- Criar: `src/interface.py`, `testes/apoio.py`, `testes/test_menu.py`
- Modificar: `src/cenas/menu.py`, `src/jogo.py`

**Interfaces:**
- Consome: `Cena`, `Jogo`.
- Produz:
  - `Botao(texto: str, centro: tuple[int, int], acao: Callable[[], None])`: atributo `rect`; `desenhar(tela, fonte, selecionado: bool)`.
  - `MenuBotoes(botoes: list[Botao])`: atributo `selecionado: int`; `tratar_evento(evento)`; `desenhar(tela, fonte)`.
  - `CenaMenu`: atributo `pagina` (`"inicial"` ou `"modo"`).
  - `Jogo.iniciar_partida(modo: str)`: nesta etapa, ainda não faz nada.
  - `testes/apoio.py`: `evento_tecla(tecla) -> pygame.event.Event`, que cria um evento `KEYDOWN`.

- [ ] **Passo 1: Escrever os testes** (`testes/test_menu.py`).

```python
class TesteMenuBotoes(unittest.TestCase):
    def setUp(self):
        self.chamadas = []
        self.menu = MenuBotoes([
            Botao("A", (400, 300), lambda: self.chamadas.append("A")),
            Botao("B", (400, 380), lambda: self.chamadas.append("B")),
        ])

    def test_navega_com_setas_e_confirma_com_enter(self):
        self.menu.tratar_evento(evento_tecla(pygame.K_DOWN))
        self.menu.tratar_evento(evento_tecla(pygame.K_RETURN))
        self.assertEqual(self.chamadas, ["B"])

    def test_navegacao_da_a_volta(self):
        self.menu.tratar_evento(evento_tecla(pygame.K_UP))
        self.assertEqual(self.menu.selecionado, 1)

    def test_clique_no_botao(self):
        self.menu.tratar_evento(pygame.event.Event(
            pygame.MOUSEBUTTONDOWN, pos=(400, 380), button=1))
        self.assertEqual(self.chamadas, ["B"])

    def test_clique_fora_nao_faz_nada(self):
        self.menu.tratar_evento(pygame.event.Event(
            pygame.MOUSEBUTTONDOWN, pos=(10, 10), button=1))
        self.assertEqual(self.chamadas, [])


class TesteCenaMenu(unittest.TestCase):
    def setUp(self):
        self.jogo = Mock()
        self.cena = CenaMenu(self.jogo)

    def test_iniciar_abre_a_escolha_de_modo(self):
        self.cena.tratar_evento(evento_tecla(pygame.K_RETURN))
        self.assertEqual(self.cena.pagina, "modo")
        self.jogo.iniciar_partida.assert_not_called()

    def test_solo_inicia_a_partida(self):
        self.cena.tratar_evento(evento_tecla(pygame.K_RETURN))
        self.cena.tratar_evento(evento_tecla(pygame.K_RETURN))
        self.jogo.iniciar_partida.assert_called_once_with(cfg.MODO_SOLO)

    def test_esc_volta_para_o_menu_inicial(self):
        self.cena.tratar_evento(evento_tecla(pygame.K_RETURN))
        self.cena.tratar_evento(evento_tecla(pygame.K_ESCAPE))
        self.assertEqual(self.cena.pagina, "inicial")
```

- [ ] **Passo 2: Executar os testes.** Esperado: falha por falta de `src.interface`.
- [ ] **Passo 3: Implementar.** Setas ou W/S mudam a seleção (circular, com `%`). Enter, Enter do teclado numérico ou Espaço executam o botão selecionado. Passar o mouse seleciona; o clique esquerdo dentro do `rect` executa. Fontes: `pygame.font.Font(None, tamanho)`.
- [ ] **Passo 4: Executar os testes.** Esperado: todos passam.
- [ ] **Passo 5: Conferir manualmente.** O menu mostra "Unrelated" e "Iniciar"; a escolha de modo funciona com mouse e com teclado.
- [ ] **Passo 6: Commit.** `feat: menu inicial com mouse e teclado`

**A dupla deve saber explicar:** Por que `Botao` recebe uma função (`acao`)? Por que a navegação fica em `MenuBotoes`, e não em cada tela?

---

## Etapa 3: Coração na arena

**Arquivos:**
- Criar: `ferramentas/__init__.py`, `ferramentas/gerar_recursos.py`, `src/recursos.py`, `src/arena.py`, `src/jogador.py`, `src/cenas/partida.py`, `assets/imagens/*.png`
- Modificar: `src/jogo.py`, `testes/apoio.py`
- Testes: `testes/test_recursos.py`, `testes/test_jogador.py`, `testes/test_partida.py`

**Interfaces produzidas:**
- `gerar_imagens(pasta: Path) -> list[Path]`: cria somente os arquivos que faltam e devolve os criados. Nomes: `jogador1.png`, `jogador2.png`, `inimigo_chuva.png`, `inimigo_lateral.png`, `inimigo_mira.png`, `item_pontos.png`, `item_cura.png`. Imagens em pixel art de 16 x 16, com fundo transparente.
- `recursos.py`: `PASTA_PROJETO = Path(__file__).resolve().parent.parent`, `PASTA_IMAGENS`, `PASTA_SONS`; `Recursos(pasta_imagens=PASTA_IMAGENS, pasta_sons=PASTA_SONS)` com `imagem(nome: str, tamanho: tuple[int, int]) -> pygame.Surface`.
- `Arena(centro, tamanhos, rng: random.Random | None = None)`: atributo `rect`; `desenhar(tela)`. Começa com `tamanhos[0]`.
- `Jogador(pygame.sprite.Sprite)`: `__init__(nome: str, imagem, posicao, controles: list[dict[str, int]])`; atributos `nome`, `image`, `rect`, `posicao: Vector2`, `radius`, `controles`; `calcular_direcao(teclas) -> Vector2`; `update(dt, teclas, arena)`; `desenhar(tela)`.
- `CenaPartida(jogo, modo: str)`: atributos `modo`, `jogadores: list[Jogador]`, `arena`. Usa `jogo.recursos`.
- `Jogo.recursos` (criado depois de `set_mode`) e `Jogo.iniciar_partida(modo)` funcionando.
- `testes/apoio.py`: `teclas(*pressionadas)`, que devolve `defaultdict(bool, {...: True})`, e `criar_jogador(nome="Jogador 1", posicao=cfg.CENTRO_ARENA, controles=None)`, que usa uma `Surface` vazia como imagem e `[cfg.TECLAS_P1]` por padrão.

- [ ] **Passo 1: Escrever os testes.**

```python
# test_recursos.py
class TesteRecursos(unittest.TestCase):
    def test_imagem_de_outro_tamanho_e_redimensionada(self):
        with tempfile.TemporaryDirectory() as pasta:
            pygame.image.save(pygame.Surface((100, 50)), str(Path(pasta) / "grande.png"))
            recursos = Recursos(pasta_imagens=Path(pasta))
            self.assertEqual(recursos.imagem("grande.png", (24, 24)).get_size(), (24, 24))

    def test_imagem_ausente_informa_o_nome(self):
        with self.assertRaisesRegex(FileNotFoundError, "nao_existe.png"):
            Recursos().imagem("nao_existe.png", (24, 24))

    def test_gerador_nao_sobrescreve_arquivos(self):
        with tempfile.TemporaryDirectory() as pasta:
            gerar_imagens(Path(pasta))
            arquivo = Path(pasta) / "jogador1.png"
            arquivo.write_bytes(b"desenho da dupla")
            self.assertEqual(gerar_imagens(Path(pasta)), [])
            self.assertEqual(arquivo.read_bytes(), b"desenho da dupla")


# test_jogador.py
class TesteMovimento(unittest.TestCase):
    def setUp(self):
        self.arena = Arena(cfg.CENTRO_ARENA, cfg.TAMANHOS_ARENA)
        self.jogador = criar_jogador()

    def test_diagonal_nao_e_mais_rapida(self):
        direcao = self.jogador.calcular_direcao(teclas(pygame.K_w, pygame.K_d))
        self.assertAlmostEqual(direcao.length(), 1.0)

    def test_teclas_opostas_se_anulam(self):
        direcao = self.jogador.calcular_direcao(teclas(pygame.K_a, pygame.K_d))
        self.assertEqual(direcao.length(), 0)

    def test_ignora_as_teclas_do_outro_jogador(self):
        direcao = self.jogador.calcular_direcao(teclas(pygame.K_UP))
        self.assertEqual(direcao.length(), 0)

    def test_aceita_dois_conjuntos_de_teclas(self):
        jogador = criar_jogador(controles=[cfg.TECLAS_P1, cfg.TECLAS_P2])
        self.assertEqual(jogador.calcular_direcao(teclas(pygame.K_UP)).y, -1)

    def test_nao_sai_da_arena(self):
        for _ in range(200):
            self.jogador.update(0.05, teclas(pygame.K_a), self.arena)
        self.assertTrue(self.arena.rect.contains(self.jogador.rect))


# test_partida.py
class TestePartida(unittest.TestCase):
    def setUp(self):
        self.jogo = Mock(recursos=Recursos())
        self.cena = CenaPartida(self.jogo, cfg.MODO_SOLO)

    def test_esc_volta_ao_menu(self):
        self.cena.tratar_evento(evento_tecla(pygame.K_ESCAPE))
        self.jogo.ir_para_menu.assert_called_once()
```

- [ ] **Passo 2: Executar os testes.** Esperado: os testes novos falham.
- [ ] **Passo 3: Implementar.** Gerar as imagens a partir de matrizes de texto no script e executar `python ferramentas/gerar_recursos.py`. `Recursos.imagem` carrega com `convert_alpha()`, sempre redimensiona com `pygame.transform.scale`, guarda em um dicionário e, se o arquivo faltar, lança `FileNotFoundError` com o nome. O `Jogador` guarda a posição em `Vector2` e atualiza o `rect` com valores arredondados. Para mantê-lo na caixa, comparar o `rect` com `rect.clamp(arena.rect)` e corrigir em `posicao` apenas o eixo que mudou. No Solo, o jogador usa os dois conjuntos de teclas e começa no centro. Até a Etapa 8, o botão "Versus" abre a mesma partida do Solo.
- [ ] **Passo 4: Executar os testes.** Esperado: todos passam.
- [ ] **Passo 5: Conferir manualmente.** O coração anda com WASD e setas, não sai da caixa e ESC volta ao menu. Executar também de fora da pasta (`python Unrelated/main.py`) para conferir os caminhos.
- [ ] **Passo 6: Commit.** `feat: coracao se movendo dentro da arena`

**A dupla deve saber explicar:** Por que a diagonal precisa ser normalizada? Como o jogo encontra as imagens sem caminho absoluto no código? Por que a posição usa `Vector2` além do `Rect`?

---

## Etapa 4: Projéteis, primeiro inimigo e vidas

**Arquivos:**
- Criar: `src/projetil.py`, `src/inimigos.py`, `src/regras.py`
- Modificar: `src/jogador.py`, `src/interface.py`, `src/cenas/partida.py`, `testes/apoio.py`, `testes/test_jogador.py`
- Testes: `testes/test_projetil.py`, `testes/test_inimigos.py`, `testes/test_regras.py`

**Interfaces produzidas:**
- `Projetil(posicao, velocidade)`: atributos `posicao: Vector2`, `velocidade: Vector2`, `radius`, `image`, `rect`; `update(dt)`. É desenhado como círculo e se remove ao sair do retângulo da tela ampliado com `inflate(200, 200)`.
- `Inimigo(pygame.sprite.Sprite, ABC)`: atributos de classe `nome_imagem` e `intervalo`; `__init__(imagem, posicao, rng=None)`; `atualizar_ataque(dt, arena, alvos, velocidade, frequencia=1.0) -> list[Projetil]`; método abstrato `atacar(arena, alvos, velocidade) -> list[Projetil]`.
- `InimigoChuva(Inimigo)`.
- `Jogador`: propriedades `vidas`, `vivo`, `invulneravel`, `visivel`; atributo `tempo_invulneravel`; `receber_dano() -> bool`.
- `aplicar_danos(jogadores, projeteis: pygame.sprite.Group) -> list[Jogador]`: devolve quem levou dano.
- `HUD(fonte)`: `desenhar(tela, jogadores)`, com um coração por vida.
- `testes/apoio.py`: `eliminar(jogador)`, que repete `receber_dano()` e zera `tempo_invulneravel` até o jogador não estar vivo.

- [ ] **Passo 1: Escrever os testes.**

```python
# test_projetil.py
class TesteProjetil(unittest.TestCase):
    def test_anda_em_linha_reta(self):
        projetil = Projetil((100, 100), (60, 0))
        projetil.update(0.5)
        self.assertEqual(projetil.posicao, pygame.math.Vector2(130, 100))

    def test_some_quando_sai_da_tela(self):
        projetil = Projetil((850, 100), (1000, 0))
        pygame.sprite.Group(projetil)
        projetil.update(0.5)
        self.assertFalse(projetil.alive())


# test_inimigos.py
class TesteInimigos(unittest.TestCase):
    def setUp(self):
        self.arena = Arena(cfg.CENTRO_ARENA, cfg.TAMANHOS_ARENA)

    def test_chuva_nasce_fora_da_caixa_e_cai(self):
        inimigo = InimigoChuva(pygame.Surface((64, 64)), (400, 70), random.Random(1))
        projeteis = inimigo.atacar(self.arena, [], 150)
        self.assertEqual(len(projeteis), cfg.QUANTIDADE_CHUVA)
        for projetil in projeteis:
            self.assertFalse(self.arena.rect.colliderect(projetil.rect))
            self.assertEqual(projetil.velocidade, pygame.math.Vector2(0, 150))


# test_jogador.py
class TesteVidas(unittest.TestCase):
    def setUp(self):
        self.arena = Arena(cfg.CENTRO_ARENA, cfg.TAMANHOS_ARENA)
        self.jogador = criar_jogador()

    def test_hit_tira_uma_vida_e_da_invulnerabilidade(self):
        self.assertTrue(self.jogador.receber_dano())
        self.assertFalse(self.jogador.receber_dano())
        self.assertEqual(self.jogador.vidas, 2)

    def test_invulnerabilidade_dura_2_segundos(self):
        self.jogador.receber_dano()
        for _ in range(39):
            self.jogador.update(0.05, teclas(), self.arena)
        self.assertTrue(self.jogador.invulneravel)
        for _ in range(2):
            self.jogador.update(0.05, teclas(), self.arena)
        self.assertFalse(self.jogador.invulneravel)


# test_regras.py
class TesteDano(unittest.TestCase):
    def test_mesmo_projetil_atinge_os_dois(self):
        jogadores = [criar_jogador("Jogador 1"), criar_jogador("Jogador 2")]
        projeteis = pygame.sprite.Group(Projetil(cfg.CENTRO_ARENA, (0, 0)))
        self.assertEqual(aplicar_danos(jogadores, projeteis), jogadores)
        self.assertEqual([j.vidas for j in jogadores], [2, 2])
        self.assertEqual(len(projeteis), 0)

    def test_projetil_atravessa_quem_esta_invulneravel(self):
        jogador = criar_jogador()
        jogador.receber_dano()
        projeteis = pygame.sprite.Group(Projetil(cfg.CENTRO_ARENA, (0, 0)))
        self.assertEqual(aplicar_danos([jogador], projeteis), [])
        self.assertEqual(len(projeteis), 1)
```

- [ ] **Passo 2: Executar os testes.** Esperado: os testes novos falham.
- [ ] **Passo 3: Implementar.**
  - `atualizar_ataque` soma `dt * frequencia` a um cronômetro; ao atingir `intervalo`, subtrai o intervalo e chama `atacar`.
  - `InimigoChuva.atacar`: `x` sorteado dentro da largura da caixa, `y = arena.rect.top - MARGEM_SURGIMENTO`.
  - `aplicar_danos` usa `spritecollide(..., False, pygame.sprite.collide_circle)`. Primeiro reúne os acertos de **todos** os jogadores vivos e vulneráveis; depois aplica o dano e remove os projéteis. Essa ordem evita favorecer o jogador 1.
  - Piscar: `visivel` alterna a cada `INTERVALO_PISCAR` enquanto o jogador está invulnerável.
  - Sem vidas, a partida chama `jogo.ir_para_menu()`. A Etapa 5 substitui isso pelo game over.
- [ ] **Passo 4: Executar os testes.** Esperado: todos passam.
- [ ] **Passo 5: Conferir manualmente.** O inimigo aparece como imagem, a chuva cai, cada hit tira um coração, o personagem pisca por 2 s e, sem corações, volta ao menu.
- [ ] **Passo 6: Commit.** `feat: projeteis, inimigo de chuva e vidas`

**A dupla deve saber explicar:** O que `InimigoChuva` herda e o que implementa? Como funciona a colisão por círculos? Por que as vidas só mudam por métodos?

---

## Etapa 5: Pontuação e game over (marco)

**Arquivos:**
- Criar: `src/cenas/game_over.py`, `testes/test_game_over.py`
- Modificar: `src/jogador.py`, `src/regras.py`, `src/interface.py`, `src/cenas/partida.py`, `src/jogo.py`, `testes/test_partida.py`, `testes/test_regras.py`

**Interfaces produzidas:**
- `Jogador`: propriedade `pontos`; `adicionar_pontos(valor: float)`.
- `ResultadoPartida`, um `dataclass(frozen=True)`: `modo: str`, `pontos: tuple[int, ...]`, `vencedor: str | None`, `sobrevivente: str | None`.
- `calcular_resultado(modo, jogadores) -> ResultadoPartida`. Não altera os jogadores. No Solo, `vencedor` e `sobrevivente` são `None`.
- `CenaGameOver(jogo, resultado)`.
- `Jogo.mostrar_game_over(resultado)`.

- [ ] **Passo 1: Escrever os testes.**

```python
# test_regras.py
class TesteResultadoSolo(unittest.TestCase):
    def test_resultado_usa_pontos_inteiros(self):
        jogador = criar_jogador()
        jogador.adicionar_pontos(123.9)
        resultado = calcular_resultado(cfg.MODO_SOLO, [jogador])
        self.assertEqual(resultado.pontos, (123,))
        self.assertIsNone(resultado.vencedor)


# test_partida.py (novos métodos em TestePartida)
    def test_ganha_pontos_por_tempo(self):
        for _ in range(20):
            self.cena.atualizar(0.05)
        self.assertAlmostEqual(self.cena.jogadores[0].pontos, 10, places=5)

    def test_sem_vidas_vai_para_o_game_over(self):
        eliminar(self.cena.jogadores[0])
        self.cena.atualizar(0.016)
        self.jogo.mostrar_game_over.assert_called_once()
        resultado = self.jogo.mostrar_game_over.call_args[0][0]
        self.assertEqual(resultado.modo, cfg.MODO_SOLO)


# test_game_over.py
class TesteGameOver(unittest.TestCase):
    def setUp(self):
        self.jogo = Mock()
        resultado = ResultadoPartida(cfg.MODO_VERSUS, (1, 2), "Jogador 2", None)
        self.cena = CenaGameOver(self.jogo, resultado)

    def test_jogar_novamente_mantem_o_modo(self):
        self.cena.tratar_evento(evento_tecla(pygame.K_RETURN))
        self.jogo.iniciar_partida.assert_called_once_with(cfg.MODO_VERSUS)

    def test_botao_menu(self):
        self.cena.tratar_evento(evento_tecla(pygame.K_DOWN))
        self.cena.tratar_evento(evento_tecla(pygame.K_RETURN))
        self.jogo.ir_para_menu.assert_called_once()

    def test_esc_volta_ao_menu(self):
        self.cena.tratar_evento(evento_tecla(pygame.K_ESCAPE))
        self.jogo.ir_para_menu.assert_called_once()
```

- [ ] **Passo 2: Executar os testes.** Esperado: os testes novos falham.
- [ ] **Passo 3: Implementar.** Cada jogador vivo ganha `PONTOS_POR_SEGUNDO * dt`. O HUD mostra `int(jogador.pontos)`. O fim da partida é verificado no final de `atualizar`, depois de todo o dano do quadro. O game over mostra "Game Over", a pontuação e os dois botões, reaproveitando `MenuBotoes`.
- [ ] **Passo 4: Executar os testes.** Esperado: todos passam.
- [ ] **Passo 5: Conferir o marco.** Com o jogo aberto, marcar os requisitos 2 a 8 da tabela 1.3.
- [ ] **Passo 6: Commit.** `feat: pontuacao e game over`

**A dupla deve saber explicar:** Como uma tela pede a troca para outra sem importá-la? Por que o resultado é um objeto separado?

---

## Etapa 6: Três inimigos, ondas e arena variável

**Arquivos:**
- Criar: `src/ondas.py`, `testes/test_ondas.py`, `testes/test_arena.py`
- Modificar: `src/inimigos.py`, `src/arena.py`, `src/cenas/partida.py`, `testes/test_inimigos.py`

**Interfaces produzidas:**
- `InimigoLateral`, `InimigoMira` e `TIPOS_INIMIGOS = [InimigoChuva, InimigoLateral, InimigoMira]`. Para adicionar ou retirar um tipo, altera-se essa lista.
- `Arena`: atributo `rect_alvo` (destino da transição; `update` lê o tamanho dele a cada quadro); `mudar_tamanho()` (sorteia um tamanho diferente do alvo atual); `update(dt)`; `area_de_surgimento() -> pygame.Rect`, a união de `rect` e `rect_alvo` ampliada em `2 * MARGEM_SURGIMENTO` na largura e na altura.
- `GerenciadorOndas(tipos, recursos, arena, rng=None)`: atributos `indice_onda`, `tempo_total`, `inimigos: pygame.sprite.Group`; `quantidade_inimigos(indice) -> int`; `multiplicadores(indice) -> tuple[float, float]` (velocidade, frequência); `intervalo_solto(tempo) -> float`; `criar_projetil_solto(velocidade: float) -> Projetil`; `update(dt, alvos, total_projeteis: int) -> list[Projetil]`.

- [ ] **Passo 1: Escrever os testes.**

```python
# test_ondas.py
class TesteOndas(unittest.TestCase):
    def setUp(self):
        self.arena = Arena(cfg.CENTRO_ARENA, cfg.TAMANHOS_ARENA, random.Random(1))
        self.ondas = GerenciadorOndas(TIPOS_INIMIGOS, Recursos(), self.arena, random.Random(2))

    def test_quantidade_de_inimigos_por_onda(self):
        quantidades = [self.ondas.quantidade_inimigos(i) for i in range(7)]
        self.assertEqual(quantidades, [1, 1, 2, 3, 3, 3, 3])

    def test_funciona_com_um_unico_tipo(self):
        ondas = GerenciadorOndas([InimigoChuva], Recursos(), self.arena)
        self.assertEqual(ondas.quantidade_inimigos(10), 1)

    def test_dificuldade_tem_limite(self):
        self.assertEqual(self.ondas.multiplicadores(0), (1.0, 1.0))
        self.assertEqual(self.ondas.multiplicadores(100),
                         (cfg.MULTIPLICADOR_VELOCIDADE_MAXIMO,
                          cfg.MULTIPLICADOR_FREQUENCIA_MAXIMO))

    def test_projeteis_soltos_ficam_mais_frequentes(self):
        self.assertEqual(self.ondas.intervalo_solto(0), 3.0)
        self.assertAlmostEqual(self.ondas.intervalo_solto(20), 2.4)
        self.assertEqual(self.ondas.intervalo_solto(1000), cfg.INTERVALO_SOLTO_MINIMO)

    def test_respeita_o_maximo_de_projeteis(self):
        novos = self.ondas.update(5.0, [criar_jogador()], cfg.MAXIMO_PROJETEIS)
        self.assertEqual(novos, [])

    def test_projetil_solto_nasce_fora_e_cruza_a_caixa(self):
        for _ in range(50):
            projetil = self.ondas.criar_projetil_solto(150)
            self.assertFalse(self.arena.rect.collidepoint(projetil.posicao))
            entrou = False
            for _ in range(600):
                projetil.update(0.01)
                entrou = entrou or self.arena.rect.collidepoint(projetil.posicao)
            self.assertTrue(entrou)


# test_arena.py
class TesteArena(unittest.TestCase):
    def setUp(self):
        self.arena = Arena(cfg.CENTRO_ARENA, cfg.TAMANHOS_ARENA, random.Random(1))

    def test_chega_ao_novo_tamanho_sem_sair_do_centro(self):
        antes = self.arena.rect.copy()
        self.arena.mudar_tamanho()
        for _ in range(100):
            self.arena.update(0.05)
        self.assertNotEqual(self.arena.rect.size, antes.size)
        self.assertEqual(self.arena.rect, self.arena.rect_alvo)
        self.assertEqual(self.arena.rect.center, cfg.CENTRO_ARENA)

    def test_surgimento_fica_fora_durante_a_transicao(self):
        self.arena.mudar_tamanho()
        area = self.arena.area_de_surgimento()
        folga = 2 * cfg.MARGEM_SURGIMENTO
        self.assertTrue(area.contains(self.arena.rect.inflate(folga, folga)))
        self.assertTrue(area.contains(self.arena.rect_alvo.inflate(folga, folga)))


# test_inimigos.py (novos métodos em TesteInimigos)
    def test_lateral_nasce_fora_e_anda_na_horizontal(self):
        inimigo = InimigoLateral(pygame.Surface((64, 64)), (400, 70), random.Random(1))
        for projetil in inimigo.atacar(self.arena, [], 150):
            self.assertFalse(self.arena.rect.colliderect(projetil.rect))
            self.assertEqual((abs(projetil.velocidade.x), projetil.velocidade.y), (150, 0))

    def test_mira_sem_alvo_nao_atira(self):
        inimigo = InimigoMira(pygame.Surface((64, 64)), (400, 70))
        self.assertEqual(inimigo.atacar(self.arena, [], 150), [])

    def test_mira_aponta_para_o_alvo(self):
        inimigo = InimigoMira(pygame.Surface((64, 64)), (400, 70))
        alvo = criar_jogador(posicao=(500, 370))
        projetil = inimigo.atacar(self.arena, [alvo], 150)[0]
        esperado = (alvo.posicao - pygame.math.Vector2(400, 70)).normalize() * 150
        self.assertAlmostEqual(projetil.velocidade.distance_to(esperado), 0, places=4)
```

- [ ] **Passo 2: Executar os testes.** Esperado: os testes novos falham.
- [ ] **Passo 3: Implementar.**
  - A partir de agora, todos os ataques usam `area_de_surgimento()` como ponto de partida, inclusive a chuva (`y = area.top`). `InimigoMira` sorteia um alvo entre os jogadores vivos recebidos e atira a partir da própria posição, acima da caixa.
  - `InimigoLateral`: sorteia o lado e a altura dentro da caixa.
  - A cada `DURACAO_ONDA`: avançar `indice_onda`, chamar `arena.mudar_tamanho()` e sortear os tipos sem repetir dentro da onda. Se nem todos os tipos forem usados, não repetir o mesmo conjunto da onda anterior. Os inimigos ocupam `POSICOES_INIMIGOS` em ordem.
  - Nível extra: `max(0, indice_onda - 3)`. Cada multiplicador é `min(1 + aumento * nivel, máximo)`.
  - Velocidade: `min(VELOCIDADE_PROJETIL * multiplicador, VELOCIDADE_MAXIMA_PROJETIL)`.
  - Intervalo dos soltos: `max(mínimo, inicial - redução * tempo_total)`.
  - Projétil solto: origem em um ponto sorteado de uma das 4 bordas de `area_de_surgimento()`, mirando em um ponto sorteado dentro de `rect.inflate(-10, -10)`. A rapidez é sorteada entre 60% de `VELOCIDADE_PROJETIL` e a velocidade da onda.
  - `update` nunca devolve mais que `max(0, MAXIMO_PROJETEIS - total_projeteis)` projéteis.
  - `CenaPartida` troca o inimigo fixo pelo `GerenciadorOndas` e atualiza a arena antes dos jogadores.
- [ ] **Passo 4: Executar os testes.** Esperado: todos passam.
- [ ] **Passo 5: Conferir manualmente.** Jogar por mais de 80 s (se preciso, reduzir `DURACAO_ONDA` temporariamente e restaurar depois): as ondas se somam, a caixa muda sem travar o coração e há espaço para desviar.
- [ ] **Passo 6: Commit.** `feat: tres inimigos, ondas e arena variavel`

**A dupla deve saber explicar:** Como o gerenciador usa os três tipos sem usar `if` para cada um? O que precisa mudar para criar um quarto inimigo? Como a dificuldade cresce?

---

## Etapa 7: Coletáveis

**Arquivos:**
- Criar: `src/coletaveis.py`, `testes/test_coletaveis.py`
- Modificar: `src/jogador.py`, `src/regras.py`, `src/cenas/partida.py`, `testes/test_partida.py`

**Interfaces produzidas:**
- `Coletavel(pygame.sprite.Sprite, ABC)`: atributos de classe `nome_imagem` e `nome_som`; `__init__(imagem, posicao)`; `radius`; `update(dt)`, que remove o item após `DURACAO_COLETAVEL`; método abstrato `aplicar(jogador)`.
- `ColetavelPontos` (`item_pontos.png`, `coleta.wav`) e `ColetavelCura` (`item_cura.png`, `cura.wav`).
- `GeradorColetaveis(recursos, rng=None)`: `update(dt, arena) -> Coletavel | None`.
- `Jogador.curar()`.
- `distribuir_coletaveis(jogadores, coletaveis: pygame.sprite.Group, rng) -> list[Coletavel]`: devolve os itens coletados.
- `CenaPartida.coletaveis: pygame.sprite.Group`.

- [ ] **Passo 1: Escrever os testes.**

```python
# test_coletaveis.py
def novo_item(classe, posicao=cfg.CENTRO_ARENA):
    return classe(pygame.Surface(cfg.TAMANHO_COLETAVEL), posicao)


class TesteColetaveis(unittest.TestCase):
    def test_item_de_pontos(self):
        jogador = criar_jogador()
        novo_item(ColetavelPontos).aplicar(jogador)
        self.assertEqual(jogador.pontos, cfg.PONTOS_COLETAVEL)

    def test_cura_ate_o_maximo_de_3(self):
        jogador = criar_jogador()
        jogador.receber_dano()
        novo_item(ColetavelCura).aplicar(jogador)
        novo_item(ColetavelCura).aplicar(jogador)
        self.assertEqual(jogador.vidas, 3)

    def test_item_some_depois_do_tempo(self):
        item = novo_item(ColetavelPontos)
        pygame.sprite.Group(item)
        item.update(cfg.DURACAO_COLETAVEL - 0.1)
        self.assertTrue(item.alive())
        item.update(0.2)
        self.assertFalse(item.alive())

    def test_o_mais_proximo_fica_com_o_item(self):
        longe = criar_jogador("Jogador 1", posicao=(408, 330))
        perto = criar_jogador("Jogador 2", posicao=(402, 330))
        itens = pygame.sprite.Group(novo_item(ColetavelPontos))
        distribuir_coletaveis([longe, perto], itens, random.Random(0))
        self.assertEqual((longe.pontos, perto.pontos), (0, cfg.PONTOS_COLETAVEL))
        self.assertEqual(len(itens), 0)

    def test_distancia_igual_e_sorteada(self):
        rng = random.Random(0)
        vencedores = set()
        for _ in range(100):
            jogadores = [criar_jogador("Jogador 1"), criar_jogador("Jogador 2")]
            distribuir_coletaveis(jogadores, pygame.sprite.Group(novo_item(ColetavelPontos)), rng)
            vencedores.update(j.nome for j in jogadores if j.pontos > 0)
        self.assertEqual(vencedores, {"Jogador 1", "Jogador 2"})


# test_partida.py (novo método em TestePartida)
    def test_item_continua_na_caixa_quando_ela_encolhe(self):
        arena = self.cena.arena
        self.cena.jogadores[0].tempo_invulneravel = 999
        item = ColetavelPontos(pygame.Surface(cfg.TAMANHO_COLETAVEL),
                               (arena.rect.left + 15, arena.rect.centery))
        self.cena.coletaveis.add(item)
        arena.rect_alvo = pygame.Rect(0, 0, 300, 300)
        arena.rect_alvo.center = cfg.CENTRO_ARENA
        for _ in range(40):
            self.cena.atualizar(0.05)
        self.assertTrue(item.alive())
        self.assertTrue(arena.rect.contains(item.rect))
```

- [ ] **Passo 2: Executar os testes.** Esperado: os testes novos falham.
- [ ] **Passo 3: Implementar.** Um item a cada `INTERVALO_COLETAVEL`, com `CHANCE_CURA` de ser de cura, em um ponto sorteado dentro de `arena.rect.clip(arena.rect_alvo).inflate(-40, -40)`. A cada quadro, a partida chama `item.rect.clamp_ip(arena.rect)`. Em `distribuir_coletaveis`, só jogadores vivos contam; entre os que encostam, vence a menor distância e, em empate, `rng.choice`. O dano é aplicado antes da coleta.
- [ ] **Passo 4: Executar os testes.** Esperado: todos passam.
- [ ] **Passo 5: Conferir manualmente.** Os itens aparecem na caixa, somem após 6 s, dão pontos ou curam.
- [ ] **Passo 6: Commit.** `feat: itens de pontos e de cura`

**A dupla deve saber explicar:** Como `item.aplicar(jogador)` faz coisas diferentes sem a partida saber o tipo do item? Como o jogo decide quem pegou o item?

---

## Etapa 8: Modo Versus

**Arquivos:**
- Criar: `testes/test_versus.py`
- Modificar: `src/regras.py`, `src/cenas/partida.py`, `src/cenas/game_over.py`, `src/interface.py`

**Interfaces:**
- Consome: `Jogador`, `aplicar_danos`, `distribuir_coletaveis`, `ResultadoPartida`.
- Produz: `calcular_resultado` completo para o Versus e HUD com dois jogadores (jogador 1 à esquerda, jogador 2 à direita).

- [ ] **Passo 1: Escrever os testes.**

```python
class TesteVersus(unittest.TestCase):
    def jogadores(self, pontos1, pontos2, morto1=False, morto2=False):
        lista = [criar_jogador("Jogador 1"), criar_jogador("Jogador 2")]
        for jogador, pontos, morto in zip(lista, (pontos1, pontos2), (morto1, morto2)):
            jogador.adicionar_pontos(pontos)
            if morto:
                eliminar(jogador)
        return lista

    def resultado(self, *args, **kwargs):
        return calcular_resultado(cfg.MODO_VERSUS, self.jogadores(*args, **kwargs))

    def test_sobrevivente_recebe_bonus(self):
        r = self.resultado(500, 400, morto1=True)
        self.assertEqual(r.pontos, (500, 600))
        self.assertEqual((r.vencedor, r.sobrevivente), ("Jogador 2", "Jogador 2"))

    def test_eliminado_pode_vencer_nos_pontos(self):
        r = self.resultado(900, 400, morto1=True)
        self.assertEqual(r.vencedor, "Jogador 1")

    def test_ambos_eliminados_nao_recebem_bonus(self):
        r = self.resultado(500, 450, morto1=True, morto2=True)
        self.assertEqual(r.pontos, (500, 450))
        self.assertIsNone(r.sobrevivente)

    def test_empate_compara_pontos_inteiros(self):
        r = self.resultado(500.9, 500.1, morto1=True, morto2=True)
        self.assertIsNone(r.vencedor)

    def test_empate_com_bonus(self):
        r = self.resultado(700, 500, morto1=True)
        self.assertEqual(r.pontos, (700, 700))
        self.assertIsNone(r.vencedor)

    def test_partida_versus_tem_controles_separados(self):
        cena = CenaPartida(Mock(recursos=Recursos()), cfg.MODO_VERSUS)
        self.assertEqual([j.controles for j in cena.jogadores],
                         [[cfg.TECLAS_P1], [cfg.TECLAS_P2]])
```

- [ ] **Passo 2: Executar os testes.** Esperado: os testes novos falham.
- [ ] **Passo 3: Implementar.** No Versus, os jogadores usam `jogador1.png` e `jogador2.png` e começam 60 px à esquerda e à direita do centro. O bônus só existe quando há exatamente um sobrevivente. O game over mostra "Jogador 1 venceu!", "Jogador 2 venceu!" ou "Empate!", os dois placares e, se houver, o bônus.
- [ ] **Passo 4: Executar os testes.** Esperado: todos passam.
- [ ] **Passo 5: Conferir manualmente, com as duas pessoas no mesmo teclado.** Apertar várias teclas ao mesmo tempo, inclusive diagonais dos dois lados. Alguns teclados não registram muitas teclas simultâneas; testar no computador da apresentação.
- [ ] **Passo 6: Commit.** `feat: modo versus local`

**A dupla deve saber explicar:** Como a mesma classe `Jogador` serve para os dois? Como são decididos o bônus, o vencedor e o empate?

---

## Etapa 9: Efeitos sonoros e música

**Arquivos:**
- Modificar: `ferramentas/gerar_recursos.py`, `src/recursos.py`, `src/jogo.py`, `src/cenas/partida.py`, `src/cenas/game_over.py`, `src/configuracoes.py`, `testes/test_recursos.py`
- Criar: `assets/sons/*.wav`

**Interfaces produzidas:**
- `gerar_sons(pasta: Path) -> list[Path]`: cria somente os que faltam entre `dano.wav`, `coleta.wav`, `cura.wav`, `game_over.wav` e `musica.wav`, usando os módulos `wave` e `math`.
- `Recursos`: atributo `audio_disponivel: bool`; `tocar(nome: str)`; `iniciar_musica()`.
- `configuracoes.py`: `ARQUIVO_MUSICA = "musica.wav"`, `VOLUME_MUSICA = 0.4`, `VOLUME_EFEITOS = 0.7`.

- [ ] **Passo 1: Escrever os testes.**

```python
# test_recursos.py (novos métodos em TesteRecursos)
    def test_funciona_sem_audio(self):
        recursos = Recursos()
        recursos.audio_disponivel = False
        recursos.tocar("dano.wav")
        recursos.iniciar_musica()

    def test_som_ausente_nao_quebra_o_jogo(self):
        with tempfile.TemporaryDirectory() as pasta:
            recursos = Recursos(pasta_sons=Path(pasta))
            recursos.tocar("dano.wav")
            recursos.iniciar_musica()

    def test_gerador_de_sons_nao_sobrescreve(self):
        with tempfile.TemporaryDirectory() as pasta:
            self.assertEqual(len(gerar_sons(Path(pasta))), 5)
            self.assertEqual(gerar_sons(Path(pasta)), [])
```

- [ ] **Passo 2: Executar os testes.** Esperado: os testes novos falham.
- [ ] **Passo 3: Implementar.** `audio_disponivel` reflete `pygame.mixer.get_init()`. Sem áudio ou sem o arquivo, `tocar` e `iniciar_musica` não fazem nada; erros `pygame.error` de som são tratados. A música repete em laço (`play(-1)`). Tocar um som em cada dano, coleta e cura e ao abrir o game over.
- [ ] **Passo 4: Executar os testes.** Esperado: todos passam.
- [ ] **Passo 5: Conferir manualmente.** Os quatro efeitos tocam nos momentos certos e a música continua entre as telas.
- [ ] **Passo 6: Commit.** `feat: efeitos sonoros e musica`

**A dupla deve saber explicar:** Por que a falta de som é tolerada, mas a falta de uma imagem gera erro?

---

## Etapa 10: Revisão final e apresentação

**Arquivos:**
- Modificar: `README.md`, `src/configuracoes.py`, `assets/`
- Criar: `documentacao/guia_de_estudo.md`

- [ ] **Passo 1: Artes e sons finais.** Substituir os arquivos escolhidos mantendo os nomes. Para músicas em outro formato, mudar `ARQUIVO_MUSICA`.
- [ ] **Passo 2: Balanceamento.** A dupla joga Solo e Versus e ajusta somente `configuracoes.py`. Rodar os testes depois; alguns conferem valores iniciais (invulnerabilidade, intervalo dos soltos, quantidade por onda, pontos por segundo e bônus) e devem acompanhar uma mudança proposital.
- [ ] **Passo 3: README.** Descrever o jogo, a instalação, a execução, os controles, a estrutura de pastas e a fonte e licença de cada recurso baixado.
- [ ] **Passo 4: Guia de estudo.** Para cada módulo: função, classes, métodos principais e relação com os conceitos da seção 2.5. Incluir as perguntas das etapas e uma ordem de leitura do código.
- [ ] **Passo 5: Verificação final.**
  - Todos os testes passam.
  - Os 8 requisitos da tabela 1.3 foram conferidos um a um.
  - O jogo abre a partir de outra pasta.
  - O jogo roda nos computadores das duas pessoas e no da apresentação.
  - O Versus foi testado no teclado da apresentação.
  - Nenhum caminho absoluto aparece no código.
- [ ] **Passo 6: Ensaio.** Cada pessoa apresenta o jogo e explica o código inteiro para a outra.
- [ ] **Passo 7: Commit.** `docs: README e guia de estudo`
