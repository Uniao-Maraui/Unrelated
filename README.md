# Unrelated
Repositório destinado a deter os arquivos de um jogo feito em PyGame afim de entregar um trabalho de Programação Orientada a Objetos 2026.2

Unrelated é um jogo 2D de desviar de projéteis (bullet hell), feito em Python com a biblioteca `pygame-ce`.

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
| Mover o coração | WASD ou setas |
| Voltar ao menu durante a partida | ESC |
| Fechar o jogo | Botão X da janela |

Por enquanto, apenas o modo Solo está pronto. O botão "Versus" abre uma partida igual à do Solo.

## Problemas comuns

**O terminal diz que `python` não é reconhecido (Windows).** Troque o primeiro comando por `py -m venv .venv`. Se `py` também não funcionar, instale o Python, abra um terminal novo e tente de novo. Os outros comandos continuam iguais.

**Aparece `No module named 'pygame'`.** O jogo foi aberto com um Python que não tem a biblioteca. Use o comando completo que começa com `.venv`. No VS Code, o botão de executar também funciona depois de escolher o Python da pasta `.venv` em `Ctrl+Shift+P`, **Python: Select Interpreter**.

**A criação do ambiente falha no Ubuntu ou Debian.** Instale o suporte a ambientes virtuais com `sudo apt install python3-venv` e execute o primeiro comando novamente.

**A instalação da biblioteca falha.** Confira a conexão com a internet e a versão do Python com `python --version` (no Linux e no macOS, `python3 --version`).

**Sobre `pygame` e `pygame-ce`.** O projeto usa o `pygame-ce`, que no código é importado como `import pygame`. Não instale o pacote `pygame` no mesmo ambiente, pois os dois entram em conflito.
