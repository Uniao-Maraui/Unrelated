# Unrelated - Plano de Execução

> **Para agentes de código:** SUB-SKILL OBRIGATÓRIA: use `superpowers:executing-plans` para executar este plano, uma etapa por vez. Os passos usam caixas de seleção (`- [ ]`). Pare ao fim de cada etapa e espere a aprovação da dupla.

**Objetivo:** criar um arcade bullet hell 2D em Pygame, no estilo das batalhas de Undertale e Deltarune, com modos Solo e Versus local, que atenda a todos os requisitos do Trabalho Final de POO (UFPI).

**Arquitetura:** uma classe para cada tela (`CenaMenu`, `CenaPartida`, `CenaGameOver`), todas herdando de `Cena`. A classe `Jogo` mantém o laço principal e é a única que conhece todas as telas. Os elementos da partida ficam em classes e módulos separados.

**Tecnologias:** Python 3.15 e `pygame-ce` 2.5.8.

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

1. Valores iniciais de tempo, velocidade e pontos: os listados em 2.3. Todos ficam em `configuracoes.py` e serão ajustados depois que a dupla jogar.
2. Cada onda dura 20 segundos, como no exemplo aprovado. A quantidade de inimigos segue o exemplo (1, 1, 2, 3), mas os tipos são sorteados.
3. No Solo, WASD e setas funcionam.
4. Fora da partida, ESC volta da escolha de modo para o menu inicial e do game over para o menu.
5. Se os dois encostarem no mesmo item no mesmo quadro, fica com quem estiver mais perto do centro do item. Se a distância for igual, há sorteio.
6. O código usa apenas recursos que também existem no Pygame clássico. Assim, se o professor não aceitar o `pygame-ce`, a troca de biblioteca deve exigir pouca ou nenhuma mudança no código.
7. O script de imagens e sons provisórios nunca sobrescreve um arquivo existente.

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
- Não usar funções `lambda`. Quando uma função precisar ser passada como argumento, usar um método com nome.
- Somente `src/jogo.py` importa as telas concretas. Uma tela pede a troca chamando um método de `Jogo`. Isso evita importação circular.
- Sprites usam o método `update()`, nome que o Pygame espera. Telas usam `tratar_evento()`, `atualizar()` e `desenhar()`.
- Não usar imagens, sons ou músicas originais de Undertale ou Deltarune.
- Pelo menos um commit por etapa. Enviar ao GitHub após a aprovação da etapa pela dupla.

## 2.2 Pontos de atenção

Falhas que o plano precisa evitar. Cada uma deve ser conferida na etapa indicada, jogando ou revisando o código.

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
|   `-- gerar_recursos.py    cria imagens e sons provisórios
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

1. Claude implementa a etapa e confere que o jogo abre sem erros e que o comportamento descrito funciona.
2. Claude explica as classes e os métodos da etapa.
3. A dupla executa o jogo, lê o código e responde às perguntas de estudo. Sugestão: uma pessoa explica para a outra, alternando a cada etapa.
4. Com a aprovação da dupla, o commit é enviado ao GitHub e começa a próxima etapa.

---

## Etapa 1: Janela, laço principal e base das telas

**Arquivos:**
- Criar: `requirements.txt`, `.gitignore`, `main.py`, `src/__init__.py`, `src/configuracoes.py`, `src/jogo.py`, `src/cenas/__init__.py`, `src/cenas/cena.py`, `src/cenas/menu.py`

**Interfaces produzidas:**
- `Cena(ABC)`: `__init__(self, jogo)`; métodos abstratos `tratar_evento(evento)`, `atualizar(dt: float)`, `desenhar(tela: pygame.Surface)`.
- `Jogo`: atributos `tela`, `relogio`, `cena`, `rodando`; `trocar_cena(nova: Cena)`; `ir_para_menu()`; `executar()`.
- `CenaMenu(Cena)`: nesta etapa, apenas desenha o título.
- `configuracoes.py`: todos os valores da seção 2.3.

- [ ] **Passo 1: Preparar o ambiente.** `requirements.txt` com `pygame-ce==2.5.8`; `.gitignore` com `__pycache__/`, `*.pyc` e `.venv/`. Executar `python -m pip install -r requirements.txt`.
- [ ] **Passo 2: Implementar.** O laço de `executar()` segue a ordem: `dt = min(relogio.tick(FPS) / 1000, DT_MAXIMO)`, eventos (`QUIT` põe `rodando = False`; os demais vão para `cena.tratar_evento`), `cena.atualizar(dt)`, `cena.desenhar(tela)`, `pygame.display.flip()`. Ao sair do laço, chamar `pygame.quit()`. `main.py` cria `Jogo()` e chama `executar()` dentro de `if __name__ == "__main__":`.
- [ ] **Passo 3: Conferir.** `python main.py` abre uma janela 800 x 600 com o título. Arrastar a janela por alguns segundos não causa erro. O X fecha sem erro.
- [ ] **Passo 4: Commit.** `feat: janela, laco principal e base das telas`

**A dupla deve saber explicar:** O que o `Clock` faz? O que é `dt` e por que é limitado? Por que `Cena` é uma classe abstrata?

---

## Etapa 2: Menu inicial

**Arquivos:**
- Criar: `src/interface.py`
- Modificar: `src/cenas/menu.py`, `src/jogo.py`

**Interfaces:**
- Consome: `Cena`, `Jogo`.
- Produz:
  - `Botao(texto: str, centro: tuple[int, int], acao: Callable[[], None])`: atributo `rect`; `desenhar(tela, fonte, selecionado: bool)`.
  - `MenuBotoes(botoes: list[Botao])`: atributo `selecionado: int`; `tratar_evento(evento)`; `desenhar(tela, fonte)`.
  - `CenaMenu`: atributo `pagina` (`"inicial"` ou `"modo"`).
  - `Jogo.iniciar_partida(modo: str)`: nesta etapa, ainda não faz nada.

- [ ] **Passo 1: Implementar.**
  - Setas ou W/S mudam a seleção (circular, com `%`). Enter, Enter do teclado numérico ou Espaço executam o botão selecionado. Passar o mouse seleciona; o clique esquerdo dentro do `rect` executa, e o clique fora não faz nada.
  - Na `CenaMenu`, "Iniciar" muda `pagina` para `"modo"`, sem começar a partida. "Solo" e "Versus" chamam `jogo.iniciar_partida` com o modo. "Voltar" ou ESC retornam à página `"inicial"`.
  - Cada página começa com o primeiro botão selecionado. Fontes: `pygame.font.Font(None, tamanho)`.
- [ ] **Passo 2: Conferir.** O menu mostra "Unrelated" e "Iniciar". A escolha de modo funciona com mouse e teclado, a seleção dá a volta na lista, o clique fora não faz nada, e "Voltar" e ESC retornam ao menu inicial.
- [ ] **Passo 3: Commit.** `feat: menu inicial com mouse e teclado`

**A dupla deve saber explicar:** Por que `Botao` recebe uma função (`acao`)? Por que a navegação fica em `MenuBotoes`, e não em cada tela?

---

## Etapa 3: Coração na arena

**Arquivos:**
- Criar: `ferramentas/gerar_recursos.py`, `src/recursos.py`, `src/arena.py`, `src/jogador.py`, `src/cenas/partida.py`, `assets/imagens/*.png`
- Modificar: `src/jogo.py`

**Interfaces produzidas:**
- `gerar_imagens(pasta: Path)`: cria somente os arquivos que faltam. Nomes: `jogador1.png`, `jogador2.png`, `inimigo_chuva.png`, `inimigo_lateral.png`, `inimigo_mira.png`, `item_pontos.png`, `item_cura.png`. Imagens em pixel art de 16 x 16, com fundo transparente.
- `recursos.py`: `PASTA_PROJETO = Path(__file__).resolve().parent.parent`, `PASTA_IMAGENS`, `PASTA_SONS`; `Recursos()` com `imagem(nome: str, tamanho: tuple[int, int]) -> pygame.Surface`.
- `Arena(centro, tamanhos)`: atributo `rect`; `desenhar(tela)`. Começa com `tamanhos[0]`.
- `Jogador(pygame.sprite.Sprite)`: `__init__(nome: str, imagem, posicao, controles: list[dict[str, int]])`; atributos `nome`, `image`, `rect`, `posicao: Vector2`, `radius`, `controles`; `calcular_direcao(teclas) -> Vector2`; `update(dt, teclas, arena)`; `desenhar(tela)`.
- `CenaPartida(jogo, modo: str)`: atributos `modo`, `jogadores: list[Jogador]`, `arena`. Usa `jogo.recursos`.
- `Jogo.recursos` (criado depois de `set_mode`) e `Jogo.iniciar_partida(modo)` funcionando.

- [ ] **Passo 1: Implementar.**
  - Gerar as imagens a partir de matrizes de texto no script e executar `python ferramentas/gerar_recursos.py`.
  - `Recursos.imagem` carrega com `convert_alpha()`, sempre redimensiona com `pygame.transform.scale`, guarda em um dicionário e, se o arquivo faltar, lança `FileNotFoundError` com o nome.
  - `calcular_direcao` considera apenas os controles do próprio jogador. Teclas opostas se anulam, e o vetor é normalizado para a diagonal não ser mais rápida.
  - O `Jogador` guarda a posição em `Vector2` e atualiza o `rect` com valores arredondados. Para mantê-lo na caixa, comparar o `rect` com `rect.clamp(arena.rect)` e corrigir em `posicao` apenas o eixo que mudou.
  - No Solo, o jogador usa os dois conjuntos de teclas e começa no centro. Até a Etapa 8, o botão "Versus" abre a mesma partida do Solo.
  - Na partida, ESC chama `jogo.ir_para_menu()`.
- [ ] **Passo 2: Conferir.**
  - O coração anda com WASD e setas, não sai da caixa e ESC volta ao menu.
  - A diagonal não é mais rápida, e teclas opostas deixam o coração parado.
  - O jogo abre também de fora da pasta (`python Unrelated/main.py`).
  - Uma imagem de outro tamanho é redimensionada. Depois de conferir, restaurar a imagem original.
  - Executar o script de novo não sobrescreve nenhum arquivo existente.
- [ ] **Passo 3: Commit.** `feat: coracao se movendo dentro da arena`

**A dupla deve saber explicar:** Por que a diagonal precisa ser normalizada? Como o jogo encontra as imagens sem caminho absoluto no código? Por que a posição usa `Vector2` além do `Rect`?

---

## Etapa 4: Projéteis, primeiro inimigo e vidas

**Arquivos:**
- Criar: `src/projetil.py`, `src/inimigos.py`, `src/regras.py`
- Modificar: `src/jogador.py`, `src/interface.py`, `src/cenas/partida.py`

**Interfaces produzidas:**
- `Projetil(posicao, velocidade)`: atributos `posicao: Vector2`, `velocidade: Vector2`, `radius`, `image`, `rect`; `update(dt)`. É desenhado como círculo e se remove ao sair do retângulo da tela ampliado com `inflate(200, 200)`.
- `Inimigo(pygame.sprite.Sprite, ABC)`: atributos de classe `nome_imagem` e `intervalo`; `__init__(imagem, posicao)`; `atualizar_ataque(dt, arena, alvos, velocidade, frequencia=1.0) -> list[Projetil]`; método abstrato `atacar(arena, alvos, velocidade) -> list[Projetil]`.
- `InimigoChuva(Inimigo)`.
- `Jogador`: propriedades `vidas`, `vivo`, `invulneravel`, `visivel`; atributo `tempo_invulneravel`; `receber_dano() -> bool`.
- `aplicar_danos(jogadores, projeteis: pygame.sprite.Group) -> list[Jogador]`: devolve quem levou dano.
- `HUD(fonte)`: `desenhar(tela, jogadores)`, com um coração por vida.

- [ ] **Passo 1: Implementar.**
  - A velocidade do projétil é medida em pixels por segundo; `update` soma `velocidade * dt` à posição.
  - `atualizar_ataque` soma `dt * frequencia` a um cronômetro; ao atingir `intervalo`, subtrai o intervalo e chama `atacar`.
  - `InimigoChuva.atacar` cria `QUANTIDADE_CHUVA` projéteis com `x` sorteado dentro da largura da caixa, `y = arena.rect.top - MARGEM_SURGIMENTO` e velocidade `(0, velocidade)`.
  - `receber_dano`: se o jogador estiver vivo e vulnerável, tira 1 vida, inicia `TEMPO_INVULNERAVEL` e devolve `True`; caso contrário, devolve `False`. `update` reduz o tempo de invulnerabilidade.
  - `aplicar_danos` usa `spritecollide(..., False, pygame.sprite.collide_circle)`. Primeiro reúne os acertos de **todos** os jogadores vivos e vulneráveis; depois aplica o dano e remove esses projéteis. Assim, o mesmo projétil pode atingir os dois, sem favorecer o jogador 1. Projéteis atravessam quem está invulnerável.
  - Piscar: `visivel` alterna a cada `INTERVALO_PISCAR` enquanto o jogador está invulnerável.
  - Sem vidas, a partida chama `jogo.ir_para_menu()`. A Etapa 5 substitui isso pelo game over.
- [ ] **Passo 2: Conferir.** O inimigo aparece como imagem e a chuva cai de fora da caixa. Cada hit tira um coração, o personagem pisca por 2 s e os projéteis o atravessam nesse tempo. Sem corações, o jogo volta ao menu.
- [ ] **Passo 3: Commit.** `feat: projeteis, inimigo de chuva e vidas`

**A dupla deve saber explicar:** O que `InimigoChuva` herda e o que implementa? Como funciona a colisão por círculos? Por que as vidas só mudam por métodos?

---

## Etapa 5: Pontuação e game over (marco)

**Arquivos:**
- Criar: `src/cenas/game_over.py`
- Modificar: `src/jogador.py`, `src/regras.py`, `src/interface.py`, `src/cenas/partida.py`, `src/jogo.py`

**Interfaces produzidas:**
- `Jogador`: propriedade `pontos`; `adicionar_pontos(valor: float)`.
- `ResultadoPartida`, um `dataclass(frozen=True)`: `modo: str`, `pontos: tuple[int, ...]`, `vencedor: str | None`, `sobrevivente: str | None`.
- `calcular_resultado(modo, jogadores) -> ResultadoPartida`. Não altera os jogadores. No Solo, `vencedor` e `sobrevivente` são `None`.
- `CenaGameOver(jogo, resultado)`.
- `Jogo.mostrar_game_over(resultado)`.

- [ ] **Passo 1: Implementar.**
  - Cada jogador vivo ganha `PONTOS_POR_SEGUNDO * dt`. O HUD mostra `int(jogador.pontos)`, e o resultado também converte os pontos com `int()`.
  - O fim da partida é verificado no final de `atualizar`, depois de todo o dano do quadro.
  - O game over mostra "Game Over", a pontuação e os botões "Jogar Novamente" (mantém `resultado.modo`) e "Menu", nessa ordem, reaproveitando `MenuBotoes`. ESC volta ao menu.
- [ ] **Passo 2: Conferir.** A pontuação sobe na tela. Ao perder os 3 corações, o game over mostra a pontuação. "Jogar Novamente" começa com 3 corações e 0 pontos; "Menu" e ESC voltam ao menu.
- [ ] **Passo 3: Conferir o marco.** Com o jogo aberto, marcar os requisitos 2 a 8 da tabela 1.3.
- [ ] **Passo 4: Commit.** `feat: pontuacao e game over`

**A dupla deve saber explicar:** Como uma tela pede a troca para outra sem importá-la? Por que o resultado é um objeto separado?

---

## Etapa 6: Três inimigos, ondas e arena variável

**Arquivos:**
- Criar: `src/ondas.py`
- Modificar: `src/inimigos.py`, `src/arena.py`, `src/cenas/partida.py`

**Interfaces produzidas:**
- `InimigoLateral`, `InimigoMira` e `TIPOS_INIMIGOS = [InimigoChuva, InimigoLateral, InimigoMira]`. Para adicionar ou retirar um tipo, altera-se essa lista.
- `Arena`: atributo `rect_alvo` (destino da transição); `mudar_tamanho()` (sorteia um tamanho diferente do alvo atual); `update(dt)`; `area_de_surgimento() -> pygame.Rect`, a união de `rect` e `rect_alvo` ampliada em `2 * MARGEM_SURGIMENTO` na largura e na altura.
- `GerenciadorOndas(tipos, recursos, arena)`: atributos `indice_onda`, `tempo_total`, `inimigos: pygame.sprite.Group`; `quantidade_inimigos(indice) -> int`; `multiplicadores(indice) -> tuple[float, float]` (velocidade, frequência); `intervalo_solto(tempo) -> float`; `criar_projetil_solto(velocidade: float) -> Projetil`; `update(dt, alvos, total_projeteis: int) -> list[Projetil]`.

- [ ] **Passo 1: Implementar.**
  - `Arena.update` aproxima a largura e a altura do tamanho de `rect_alvo` a `VELOCIDADE_TRANSICAO_ARENA` pixels por segundo, sem mudar o centro.
  - A partir de agora, todos os ataques surgem fora de `area_de_surgimento()` ou na borda dela, inclusive a chuva (`y = area.top`).
  - `InimigoLateral` cria um projétil por ataque: sorteia o lado e a altura dentro da caixa, e o projétil anda na horizontal em direção a ela.
  - `InimigoMira` cria um projétil por ataque: sorteia um alvo entre os jogadores vivos recebidos e atira a partir da própria posição, acima da caixa, com velocidade `(alvo.posicao - origem).normalize() * velocidade`. Sem alvos, não atira.
  - Quantidade de inimigos: `min(len(tipos), INIMIGOS_POR_ONDA[min(indice, 3)])`. Assim, o jogo funciona mesmo que a lista de tipos mude.
  - A cada `DURACAO_ONDA`: avançar `indice_onda`, chamar `arena.mudar_tamanho()` e sortear os tipos sem repetir dentro da onda. Se nem todos os tipos forem usados, não repetir o mesmo conjunto da onda anterior. Os inimigos ocupam `POSICOES_INIMIGOS` em ordem.
  - Nível extra: `max(0, indice_onda - 3)`. Cada multiplicador é `min(1 + aumento * nivel, máximo)`.
  - Velocidade: `min(VELOCIDADE_PROJETIL * multiplicador, VELOCIDADE_MAXIMA_PROJETIL)`.
  - Intervalo dos soltos: `max(mínimo, inicial - redução * tempo_total)`.
  - Projétil solto: origem em um ponto sorteado de uma das 4 bordas de `area_de_surgimento()`, mirando em um ponto sorteado dentro de `rect.inflate(-10, -10)`. A rapidez é sorteada entre 60% de `VELOCIDADE_PROJETIL` e a velocidade da onda.
  - `update` nunca devolve mais que `max(0, MAXIMO_PROJETEIS - total_projeteis)` projéteis.
  - `CenaPartida` troca o inimigo fixo pelo `GerenciadorOndas` e atualiza a arena antes dos jogadores.
- [ ] **Passo 2: Conferir.** Jogar por mais de 80 s (se preciso, reduzir `DURACAO_ONDA` temporariamente e restaurar depois). As ondas se somam, os projéteis soltos aparecem desde o início, a caixa muda sem travar o coração, nenhum projétil nasce dentro dela e há espaço para desviar.
- [ ] **Passo 3: Commit.** `feat: tres inimigos, ondas e arena variavel`

**A dupla deve saber explicar:** Como o gerenciador usa os três tipos sem usar `if` para cada um? O que precisa mudar para criar um quarto inimigo? Como a dificuldade cresce?

---

## Etapa 7: Coletáveis

**Arquivos:**
- Criar: `src/coletaveis.py`
- Modificar: `src/jogador.py`, `src/regras.py`, `src/cenas/partida.py`

**Interfaces produzidas:**
- `Coletavel(pygame.sprite.Sprite, ABC)`: atributos de classe `nome_imagem` e `nome_som`; `__init__(imagem, posicao)`; `radius`; `update(dt)`, que remove o item após `DURACAO_COLETAVEL`; método abstrato `aplicar(jogador)`.
- `ColetavelPontos` (`item_pontos.png`, `coleta.wav`) e `ColetavelCura` (`item_cura.png`, `cura.wav`).
- `GeradorColetaveis(recursos)`: `update(dt, arena) -> Coletavel | None`.
- `Jogador.curar()`.
- `distribuir_coletaveis(jogadores, coletaveis: pygame.sprite.Group) -> list[Coletavel]`: devolve os itens coletados.
- `CenaPartida.coletaveis: pygame.sprite.Group`.

- [ ] **Passo 1: Implementar.**
  - `ColetavelPontos.aplicar` soma `PONTOS_COLETAVEL`. `ColetavelCura.aplicar` chama `curar()`, que soma 1 vida sem passar de `VIDAS_MAXIMAS`.
  - Um item a cada `INTERVALO_COLETAVEL`, com `CHANCE_CURA` de ser de cura, em um ponto sorteado dentro de `arena.rect.clip(arena.rect_alvo).inflate(-40, -40)`.
  - A cada quadro, a partida chama `item.rect.clamp_ip(arena.rect)`, para o item continuar na caixa quando ela encolher.
  - Em `distribuir_coletaveis`, só jogadores vivos contam; entre os que encostam, vence a menor distância e, em empate, `random.choice`. O dano é aplicado antes da coleta.
- [ ] **Passo 2: Conferir.** Os itens aparecem na caixa, somem após 6 s e dão pontos ou curam, sem passar de 3 corações. Quando a caixa encolhe, continuam dentro dela. Revisar no código a regra de desempate.
- [ ] **Passo 3: Commit.** `feat: itens de pontos e de cura`

**A dupla deve saber explicar:** Como `item.aplicar(jogador)` faz coisas diferentes sem a partida saber o tipo do item? Como o jogo decide quem pegou o item?

---

## Etapa 8: Modo Versus

**Arquivos:**
- Modificar: `src/regras.py`, `src/cenas/partida.py`, `src/cenas/game_over.py`, `src/interface.py`

**Interfaces:**
- Consome: `Jogador`, `aplicar_danos`, `distribuir_coletaveis`, `ResultadoPartida`.
- Produz: `calcular_resultado` completo para o Versus e HUD com dois jogadores (jogador 1 à esquerda, jogador 2 à direita).

- [ ] **Passo 1: Implementar.**
  - No Versus, "Jogador 1" usa `[TECLAS_P1]` e `jogador1.png`; "Jogador 2" usa `[TECLAS_P2]` e `jogador2.png`. Eles começam 60 px à esquerda e à direita do centro.
  - O bônus é somado somente quando há exatamente um sobrevivente, sobre os pontos já convertidos com `int()`.
  - Vence a maior pontuação final, mesmo que seja de quem foi eliminado. Se forem iguais, `vencedor` é `None`.
  - O game over mostra "Jogador 1 venceu!", "Jogador 2 venceu!" ou "Empate!", os dois placares e, se houver, o bônus.
- [ ] **Passo 2: Conferir, com as duas pessoas no mesmo teclado.**
  - Cada pessoa move apenas o próprio coração.
  - A partida acaba quando alguém perde os 3 corações, e o resultado segue as regras da seção 1.4.
  - Revisar no código os casos difíceis de provocar: os dois atingidos no mesmo quadro e o empate.
  - Apertar várias teclas ao mesmo tempo, inclusive diagonais dos dois lados. Alguns teclados não registram muitas teclas simultâneas; conferir no computador da apresentação.
- [ ] **Passo 3: Commit.** `feat: modo versus local`

**A dupla deve saber explicar:** Como a mesma classe `Jogador` serve para os dois? Como são decididos o bônus, o vencedor e o empate?

---

## Etapa 9: Efeitos sonoros e música

**Arquivos:**
- Modificar: `ferramentas/gerar_recursos.py`, `src/recursos.py`, `src/jogo.py`, `src/cenas/partida.py`, `src/cenas/game_over.py`, `src/configuracoes.py`
- Criar: `assets/sons/*.wav`

**Interfaces produzidas:**
- `gerar_sons(pasta: Path)`: cria somente os que faltam entre `dano.wav`, `coleta.wav`, `cura.wav`, `game_over.wav` e `musica.wav`, usando os módulos `wave` e `math`.
- `Recursos`: atributo `audio_disponivel: bool`; `tocar(nome: str)`; `iniciar_musica()`.
- `configuracoes.py`: `ARQUIVO_MUSICA = "musica.wav"`, `VOLUME_MUSICA = 0.4`, `VOLUME_EFEITOS = 0.7`.

- [ ] **Passo 1: Implementar.** `audio_disponivel` reflete `pygame.mixer.get_init()`. Sem áudio ou sem o arquivo, `tocar` e `iniciar_musica` não fazem nada; erros `pygame.error` de som são tratados. A música repete em laço (`play(-1)`). Tocar um som em cada dano, coleta e cura e ao abrir o game over.
- [ ] **Passo 2: Conferir.** Os quatro efeitos tocam nos momentos certos e a música continua entre as telas. Com a pasta `assets/sons` renomeada temporariamente, o jogo roda sem erros. Revisar no código o caso sem dispositivo de áudio.
- [ ] **Passo 3: Commit.** `feat: efeitos sonoros e musica`

**A dupla deve saber explicar:** Por que a falta de som é tolerada, mas a falta de uma imagem gera erro?

---

## Etapa 10: Revisão final e apresentação

**Arquivos:**
- Modificar: `README.md`, `src/configuracoes.py`, `assets/`
- Criar: `documentacao/guia_de_estudo.md`

- [ ] **Passo 1: Artes e sons finais.** Substituir os arquivos escolhidos mantendo os nomes. Para músicas em outro formato, mudar `ARQUIVO_MUSICA`.
- [ ] **Passo 2: Balanceamento.** A dupla joga Solo e Versus e ajusta somente `configuracoes.py`.
- [ ] **Passo 3: README.** Descrever o jogo, a instalação, a execução, os controles, a estrutura de pastas e a fonte e licença de cada recurso baixado.
- [ ] **Passo 4: Guia de estudo.** Para cada módulo: função, classes, métodos principais e relação com os conceitos da seção 2.5. Incluir as perguntas das etapas e uma ordem de leitura do código.
- [ ] **Passo 5: Verificação final.**
  - Os 8 requisitos da tabela 1.3 foram conferidos um a um.
  - Os pontos de atenção da seção 2.2 foram conferidos.
  - O jogo abre a partir de outra pasta.
  - O jogo roda nos computadores das duas pessoas e no da apresentação.
  - O Versus foi conferido no teclado da apresentação.
  - Nenhum caminho absoluto aparece no código.
- [ ] **Passo 6: Ensaio.** Cada pessoa apresenta o jogo e explica o código inteiro para a outra.
- [ ] **Passo 7: Commit.** `docs: README e guia de estudo`
