# Unrelated
Repositório destinado a deter os arquivos de um jogo feito em PyGame afim de entregar um trabalho de Programação Orientada a Objetos 2026.2

Unrelated é um jogo 2D de desviar de projéteis (bullet hell), feito em Python com a biblioteca `pygame-ce`.

## Como jogar

Mantenha seu coração vivo, desviando dos projéteis dentro da caixa.

- Cada jogador tem 3 corações. Cada hit tira 1, e o coração pisca por 2 segundos, sem levar outro dano.
- A pontuação sobe com o tempo. A estrela dá pontos extras, e a cruz, mais rara, recupera 1 coração, até o máximo de 3.
- Os ataques vêm em ondas de 20 segundos. A cada onda, a caixa muda de tamanho.
- Os inimigos se somam: 1 nas duas primeiras ondas, 2 na terceira e 3 da quarta em diante. Depois disso, os ataques ficam mais rápidos e frequentes, até um limite.
- Também surgem projéteis soltos, cada vez com mais frequência.

**Solo:** a partida acaba quando os 3 corações terminam.

**Versus:** duas pessoas dividem a caixa e o teclado. A partida acaba quando uma delas perde os 3 corações. Quem sobreviveu ganha um bônus de 200 pontos, e vence quem tiver mais pontos. Pontos iguais dão empate.

## O que é preciso

- **Python 3.10 ou mais novo**, disponível em [python.org/downloads](https://www.python.org/downloads/). No Windows, se o instalador mostrar a opção "Add python.exe to PATH", marque-a.
- **Internet** na primeira instalação, para baixar a biblioteca.
- **Git** (opcional), para baixar o projeto pelo terminal.

O jogo foi testado no Windows com Python 3.15.2. Há pacotes do `pygame-ce` 2.5.8 para Python 3.10 a 3.15 no Windows 64 bits, no macOS e no Linux 64 bits, mas as outras combinações ainda não foram testadas com o jogo.

## 1. Baixar o projeto

Com Git:

```
git clone https://github.com/Uniao-Maraui/Unrelated.git
cd Unrelated
```

Sem Git: na página do repositório, clique em **Code** e depois em **Download ZIP**. Extraia o arquivo e abra um terminal na pasta que contém o `main.py`.

## 2. Instalar a biblioteca e rodar

Os comandos criam um ambiente virtual na pasta `.venv`. A biblioteca fica instalada dentro do projeto, sem misturar com as de outros programas. Execute os comandos na pasta que contém o `main.py`.

### Windows (PowerShell ou Prompt de Comando)

```
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe main.py
```

O primeiro comando cria o ambiente, o segundo baixa a biblioteca e o terceiro abre o jogo. Não é preciso ativar o ambiente virtual.

### Linux e macOS

```
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py
```

### Nas próximas vezes

Os dois primeiros comandos são necessários apenas uma vez em cada computador. Depois, basta o último:

- Windows: `.venv\Scripts\python.exe main.py`
- Linux e macOS: `.venv/bin/python main.py`

Se o arquivo `requirements.txt` mudar, execute o comando de instalação novamente.

A pasta `.venv` vale só para o computador em que foi criada. Não a copie para outro nem a envie ao GitHub (o `.gitignore` já a ignora).

## Controles

| Ação | Como fazer |
|---|---|
| Escolher uma opção no menu | Mouse, setas ou W e S |
| Confirmar | Clique, Enter ou Espaço |
| Mover o coração no Solo | WASD ou setas |
| Mover o coração no Versus | Jogador 1 (vermelho): WASD. Jogador 2 (azul): setas |
| Voltar ao menu durante a partida | ESC |
| Fechar o jogo | Botão X da janela |

Alguns teclados não registram muitas teclas apertadas ao mesmo tempo. Antes de jogar o Versus em um computador novo, confira se as duas pessoas conseguem se mover juntas, inclusive na diagonal.

## Trocar imagens e sons

Para trocar um arquivo, substitua-o mantendo **o mesmo nome**. O código não precisa mudar.

| Arquivo em `assets/imagens` | Uso | Tamanho no jogo |
|---|---|---|
| `jogador1.png` | Jogador 1 e seus ícones de vida | 27 x 27 |
| `jogador2.png` | Jogador 2 e seus ícones de vida | 27 x 27 |
| `inimigo_chuva.png` | Inimigo que faz projéteis caírem | 64 x 64 |
| `inimigo_lateral.png` | Inimigo que atira dos lados | 64 x 64 |
| `inimigo_mira.png` | Inimigo que mira nos corações | 64 x 64 |
| `projetil_chuva.png` | Projétil do inimigo da chuva | 24 x 24 |
| `projetil_lateral.png` | Projétil do inimigo lateral | 24 x 24 |
| `projetil_mira.png` | Projétil do inimigo que mira | 24 x 24 |
| `item_pontos.png` | Item de pontos | 32 x 32 |
| `item_cura.png` | Item de cura | 32 x 32 |

Prefira PNGs quadrados, com fundo transparente e pouca margem. O jogo redimensiona a imagem, então uma que não seja quadrada fica distorcida.

Os sons ficam em `assets/sons`: `dano.wav`, `coleta.wav`, `cura.wav`, `game_over.wav` e `musica.wav`. Para usar uma música em outro formato, como OGG, mude `ARQUIVO_MUSICA` em `src/configuracoes.py`.

Os projéteis soltos são círculos brancos desenhados pelo código. O dano e a coleta acontecem quando pixels visíveis se tocam; partes transparentes não contam. Por isso, um desenho maior também aumenta a área de acerto, e um fundo que não seja transparente contaria como parte do desenho. As imagens dos projéteis não giram, então prefira desenhos redondos ou, na chuva, que apontem para o sentido da queda.

O script `ferramentas/gerar_recursos.py` recria os arquivos que ele sabe desenhar e que estiverem faltando: os genéricos e o anel do projétil lateral. Ele nunca sobrescreve um arquivo existente e não cria os outros dois projéteis.

## Fontes e licenças

Quase todas as imagens usadas no jogo vêm de pacotes de outras pessoas. O projétil lateral foi desenhado neste projeto. Os sons ainda são genéricos, criados pelo script `ferramentas/gerar_recursos.py`.

Os arquivos de arte de terceiros pertencem aos seus autores. Eles estão aqui como parte deste jogo e não devem ser retirados do projeto para redistribuição ou revenda.

| Arquivos | Pacote e autoria | Endereço de origem | Termos | Alterações |
|---|---|---|---|---|
| `inimigo_chuva.png`, `inimigo_lateral.png`, `inimigo_mira.png` | RPG Battlers, de LimeZu | https://limezu.itch.io/21rpg-battlers | Uso gratuito ou comercial e modificação permitidos; redistribuição e revenda proibidas | Centralizados em um quadro de 32 x 32 |
| `jogador1.png`, `jogador2.png` | Retro UI Kit Lite, de Willosuna | https://willosuna.itch.io/retro-ui-kit-lite | Uso em jogos e modificação permitidos, crédito opcional; proibido redistribuir as imagens como pacote | Ampliados 3 vezes; o do jogador 2 foi pintado de azul |
| `projetil_chuva.png` | Pixel Spaceships & Shmup Kit Lite, de Willosuna | Página da versão completa, indicada no pacote: https://willosuna.itch.io/pixel-shmup-kit | Uso em jogos e modificação permitidos, crédito opcional; proibido redistribuir as imagens como pacote | Ampliado 2 vezes |
| `projetil_lateral.png` | Desenho criado neste projeto | `ferramentas/gerar_recursos.py`, função `criar_anel` | Não vem de pacote de outra pessoa | Nenhuma |
| `projetil_mira.png` | Amostra gratuita da Northleaf Studio; o leia-me informa uso de assistência de IA | https://northleafstudio.itch.io/space-shooter-sprites-pixel-art | Grátis em jogos pessoais e comerciais, pode ficar no repositório do jogo; proibido redistribuir como pacote de arte | Primeiro quadro, ampliado 2 vezes |
| `item_pontos.png`, `item_cura.png` | Pixel UI & Pickup FX (Pixel FX Series, pacote 8); autoria não informada no pacote | Não informado no pacote | Uso em jogos e modificação permitidos, crédito opcional; proibido redistribuir como arquivos avulsos ou pacote | Primeiro quadro da animação |

Ao usar um recurso de outra pessoa, confira se a licença permite o uso e registre aqui. Não use imagens, sons ou músicas originais de Undertale ou Deltarune.

## Estrutura de pastas

```
main.py            inicia o jogo
requirements.txt   biblioteca necessária
src/               código do jogo
src/cenas/         telas: menu, partida e game over
assets/            imagens e sons
ferramentas/       script que cria os recursos genéricos
documentacao/      enunciado, plano e guia de estudo
```

Os valores de velocidade, tempo e pontos ficam em `src/configuracoes.py`.

## Problemas comuns

**O terminal diz que `python` não é reconhecido (Windows).** Troque o primeiro comando por `py -m venv .venv`. Se `py` também não funcionar, instale o Python, abra um terminal novo e tente de novo. Os outros comandos continuam iguais.

**Aparece `No module named 'pygame'`.** O jogo foi aberto com um Python que não tem a biblioteca. Use o comando completo que começa com `.venv`. No VS Code, o botão de executar também funciona depois de escolher o Python da pasta `.venv` em `Ctrl+Shift+P`, **Python: Select Interpreter**.

**A criação do ambiente falha no Ubuntu ou Debian.** Instale o suporte a ambientes virtuais com `sudo apt install python3-venv` e execute o primeiro comando novamente.

**O jogo abre sem som.** Confira o volume e o dispositivo de áudio do computador e feche e abra o jogo. Sem áudio, o jogo continua funcionando em silêncio.

**A instalação da biblioteca falha.** Confira a conexão com a internet e a versão do Python com `python --version` (no Linux e no macOS, `python3 --version`).

**Sobre `pygame` e `pygame-ce`.** O projeto usa o `pygame-ce`, que no código é importado como `import pygame`. Não instale o pacote `pygame` no mesmo ambiente, pois os dois entram em conflito.
