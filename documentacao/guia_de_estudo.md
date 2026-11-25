# Unrelated - Guia de Estudo

O trabalho exige que as duas pessoas dominem todo o código. Use este guia junto com os arquivos abertos. Para cada pergunta, tente responder antes de ler a resposta.

## 1. Visão geral

```
main.py
  `-- Jogo                 janela, laço principal, troca de telas
        |-- Recursos       imagens e sons
        `-- cena atual     uma destas três (todas herdam de Cena):
              |-- CenaMenu          usa MenuBotoes e Botao
              |-- CenaPartida       usa Arena, Jogador, GerenciadorOndas,
              |                     Projetil, GeradorColetaveis, HUD e regras
              `-- CenaGameOver      usa MenuBotoes e ResultadoPartida
```

O laço principal está em `Jogo.executar()`. A cada quadro, 60 vezes por segundo, ele:

1. calcula `dt`, a duração do último quadro;
2. entrega os eventos para a tela atual (`tratar_evento`);
3. avança a lógica (`atualizar`);
4. desenha (`desenhar`) e mostra o resultado.

O `Jogo` não pergunta qual tela está aberta. Ele chama os mesmos métodos em qualquer uma.

### O que acontece em um quadro da partida

Está em `CenaPartida.atualizar()`. A ordem importa.

| Passo | O que faz |
|---|---|
| 1 | Lê o teclado |
| 2 | A arena avança na mudança de tamanho |
| 3 | Os jogadores se movem e ganham pontos por tempo |
| 4 | O gerenciador de ondas cria projéteis |
| 5 | Os projéteis se movem |
| 6 | Os itens surgem, envelhecem e são mantidos na caixa |
| 7 | O dano é aplicado |
| 8 | Os itens são distribuídos (depois do dano) |
| 9 | Os sons tocam |
| 10 | O jogo verifica se a partida acabou |

## 2. Ordem de leitura

1. `main.py`
2. `src/jogo.py`
3. `src/cenas/cena.py`
4. `src/interface.py` e `src/cenas/menu.py`
5. `src/arena.py` e `src/jogador.py`
6. `src/projetil.py`, `src/inimigos.py` e `src/ondas.py`
7. `src/coletaveis.py` e `src/regras.py`
8. `src/cenas/partida.py` e `src/cenas/game_over.py`
9. `src/recursos.py` e `src/configuracoes.py`

## 3. Módulo por módulo

| Arquivo | Classe ou função | Responsabilidade | Principais métodos |
|---|---|---|---|
| `jogo.py` | `Jogo` | Janela, laço e troca de telas | `executar`, `trocar_cena`, `ir_para_menu`, `iniciar_partida`, `mostrar_game_over` |
| `cenas/cena.py` | `Cena` | Base das telas | `tratar_evento`, `atualizar`, `desenhar` |
| `cenas/menu.py` | `CenaMenu` | Menu inicial e escolha do modo | `mostrar_inicial`, `mostrar_modos`, `jogar_solo`, `jogar_versus` |
| `cenas/partida.py` | `CenaPartida` | Junta os elementos e coordena a partida | `atualizar`, `desenhar` |
| `cenas/game_over.py` | `CenaGameOver` | Resultado e botões finais | `linhas_do_resultado`, `jogar_novamente` |
| `interface.py` | `Botao` | Um botão com texto e ação | `desenhar` |
| `interface.py` | `MenuBotoes` | Seleção por teclado e mouse | `tratar_evento`, `desenhar` |
| `interface.py` | `HUD` | Nome, corações e pontos | `desenhar` |
| `arena.py` | `Arena` | A caixa e sua mudança de tamanho | `mudar_tamanho`, `update`, `area_de_surgimento` |
| `jogador.py` | `Jogador` | Movimento, vidas e pontos | `update`, `calcular_direcao`, `receber_dano`, `curar`, `adicionar_pontos` |
| `projetil.py` | `Projetil` | Círculo que anda em linha reta | `update` |
| `inimigos.py` | `Inimigo` e 3 tipos | Ritmo e forma dos ataques | `atualizar_ataque`, `atacar` |
| `ondas.py` | `GerenciadorOndas` | Ondas, dificuldade e projéteis soltos | `update`, `multiplicadores`, `criar_projetil_solto` |
| `coletaveis.py` | `Coletavel` e 2 tipos | Efeito de cada item | `update`, `aplicar` |
| `coletaveis.py` | `GeradorColetaveis` | Cria itens de tempos em tempos | `update` |
| `regras.py` | `ResultadoPartida` e 3 funções | Resultado, dano e coleta | `calcular_resultado`, `aplicar_danos`, `distribuir_coletaveis` |
| `recursos.py` | `Recursos` | Carrega e guarda imagens e sons | `imagem`, `tocar`, `iniciar_musica` |
| `configuracoes.py` | Constantes | Valores ajustáveis | Não tem métodos |

## 4. Conceitos de POO no código

### Herança
Uma classe filha recebe o que a classe mãe já tem.
- `CenaMenu`, `CenaPartida` e `CenaGameOver` herdam de `Cena`.
- `InimigoChuva`, `InimigoLateral` e `InimigoMira` herdam de `Inimigo`.
- `ColetavelPontos` e `ColetavelCura` herdam de `Coletavel`.
- `Jogador`, `Projetil`, `Inimigo` e `Coletavel` herdam de `pygame.sprite.Sprite`.

`super().__init__()` chama o construtor da classe mãe, para ela preparar a parte que é dela.

### Polimorfismo
A mesma chamada produz comportamentos diferentes conforme o objeto.
- `self.cena.atualizar(dt)` em `Jogo`: cada tela atualiza de um jeito.
- `self.atacar(...)` em `Inimigo.atualizar_ataque`: cada inimigo ataca de um jeito.
- `item.aplicar(...)` em `distribuir_coletaveis`: um item dá pontos e o outro cura.

### Abstração
`Cena`, `Inimigo` e `Coletavel` herdam de `ABC` e têm métodos marcados com `@abstractmethod`. Não é possível criar um objeto delas, e cada classe filha precisa implementar esses métodos para ser criada.

### Encapsulamento
No `Jogador`, as vidas e os pontos ficam em `_vidas` e `_pontos`. De fora, eles são lidos pelas propriedades `vidas` e `pontos` (`@property`). Escrever `jogador.vidas = 99` gera erro. A mudança passa por `receber_dano`, `curar` ou `adicionar_pontos`, que aplicam as regras.

Atenção: em Python, o `_` no começo do nome é uma convenção. Ele avisa que o atributo é interno, mas não impede o acesso direto a `_vidas`. Nem todo atributo é protegido: `tempo_invulneravel`, por exemplo, é público.

### Composição
Um objeto é formado por outros. `CenaPartida` tem uma `Arena`, uma lista de `Jogador`, um `GerenciadorOndas`, um `GeradorColetaveis`, um `HUD` e grupos de projéteis e itens.

## 5. Onde está cada requisito do trabalho

| # | Requisito | Onde mostrar |
|---|---|---|
| 1 | Dupla que domina o código | Este guia e a explicação das duas pessoas |
| 2 | POO para jogador, inimigos, projéteis e interface | `jogador.py`, `inimigos.py`, `projetil.py`, `interface.py` |
| 3 | Organização em módulos | Pasta `src/` e `main.py` |
| 4 | Progresso em tempo real | `HUD.desenhar` |
| 5 | Tela inicial com título e botão | `CenaMenu` |
| 6 | Vidas e fim de jogo | `Jogador.receber_dano`, `CenaPartida._verificar_fim`, `CenaGameOver` |
| 7 | Pelo menos 2 sprites | `Recursos.imagem` e `assets/imagens` |
| 8 | `Clock` e caminhos relativos | `Jogo.executar` e o começo de `recursos.py` |

Os projéteis são círculos desenhados pelo código. As imagens exigidas no requisito 7 são as dos jogadores e dos inimigos.

## 6. Perguntas de estudo

### Janela e laço principal

**O que o `Clock` faz?**
`relogio.tick(60)` limita o jogo a 60 quadros por segundo e devolve quantos milissegundos se passaram desde o quadro anterior.

**O que é `dt` e por que é limitado?**
É a duração do quadro em segundos. Como `distância = velocidade x tempo`, o movimento depende do tempo, e não da quantidade de quadros. Se a janela travar, `dt` ficaria grande e um projétil poderia saltar por cima de um coração. Por isso ele não passa de 0,05 s.

**Por que `Cena` é abstrata?**
Não existe uma tela genérica. Ela define o que toda tela precisa ter.

### Menu

**Por que `Botao` recebe uma função (`acao`)?**
Para o botão não precisar saber o que ele faz. A mesma classe serve para "Iniciar", "Solo" ou "Menu". Passamos o método sem parênteses (`self.jogar_solo`), para ele ser chamado só quando o botão for escolhido.

**Por que a navegação fica em `MenuBotoes`?**
O menu e o game over precisam dela. Assim o código é escrito uma vez só.

### Coração e arena

**Por que a diagonal precisa ser normalizada?**
Somando 1 na horizontal e 1 na vertical, o vetor fica com comprimento de cerca de 1,41, e o coração andaria 41% mais rápido. `normalize_ip()` ajusta o comprimento para 1.

**Como o jogo acha as imagens sem caminho absoluto no código?**
`Path(__file__)` é o caminho do próprio `recursos.py`. Subindo duas pastas, chegamos ao projeto, e dali montamos `assets/imagens`.

**Por que usar `Vector2` além do `Rect`?**
O `Rect` guarda apenas números inteiros. O `Vector2` guarda as casas decimais, para o movimento não perder precisão.

**Como o coração fica dentro da caixa?**
`rect.clamp(arena.rect)` calcula onde o retângulo ficaria se estivesse dentro. Se um eixo mudou, a posição daquele eixo é corrigida.

### Projéteis, inimigos e vidas

**O que `InimigoChuva` herda e o que implementa?**
Herda o construtor, o cronômetro e `atualizar_ataque`. Define `nome_imagem`, `intervalo` e o método `atacar`.

**Como funciona a colisão por círculos?**
`collide_circle` compara a distância entre os centros com a soma dos atributos `radius`. O raio do jogador (8) é menor que a metade da imagem (12), o que torna a colisão mais justa.

**Por que as vidas só mudam por métodos?**
Os métodos garantem as regras: não perder vida durante a invulnerabilidade, não ficar abaixo de zero ao levar dano e não passar de 3 ao curar.

**Por que `aplicar_danos` tem dois laços?**
O primeiro descobre quem foi atingido. O segundo aplica o dano e remove os projéteis. Se removesse no primeiro, um projétil que toca os dois atingiria só o jogador 1.

**O que é um `Group`?**
Um conjunto de sprites. `group.update(dt)` chama o `update` de cada um, `group.draw(tela)` desenha usando `image` e `rect`, e `sprite.kill()` tira o sprite dos grupos.

### Pontuação e game over

**Como uma tela pede outra sem importá-la?**
Ela chama um método do `Jogo`, como `self.jogo.mostrar_game_over(resultado)`. Só `jogo.py` importa todas as telas, o que evita importação circular.

**Por que o resultado é um objeto separado?**
O game over recebe só os dados de que precisa, sem depender da partida. `@dataclass(frozen=True)` cria o construtor automaticamente e impede que os atributos sejam trocados.

### Ondas e dificuldade

**Como o gerenciador usa os três tipos sem um `if` para cada um?**
Ele recebe uma lista de classes, sorteia algumas, cria os objetos e chama o mesmo método em todos.

**O que mudar para criar um quarto inimigo?**
Criar uma classe que herda de `Inimigo`, com `nome_imagem`, `intervalo` e `atacar`; colocar a imagem em `assets/imagens`; e incluir a classe em `TIPOS_INIMIGOS`. O intervalo deve ir para `configuracoes.py`. Continuam aparecendo no máximo 3 de cada vez.

**Como a dificuldade cresce?**
Primeiro, aumentando a quantidade de inimigos (1, 1, 2, 3). Os projéteis soltos ficam mais frequentes desde o começo. Depois da quarta onda, velocidade e frequência aumentam a cada onda, até os máximos de `configuracoes.py`.

**Como se evita que um projétil nasça dentro da caixa?**
`area_de_surgimento()` junta o tamanho atual com o de destino e acrescenta uma margem. Os projéteis dos ataques laterais, da chuva e os soltos nascem na borda dessa área. O inimigo de mira atira de onde está, acima dela.

### Itens

**Como `item.aplicar(jogador)` faz coisas diferentes?**
É polimorfismo: cada subclasse escreveu o seu `aplicar`.

**Como o jogo decide quem pegou o item?**
Entre quem está encostando, vence quem estiver mais perto do centro do item. Com distâncias iguais, há sorteio.

### Versus

**Como a mesma classe `Jogador` serve para os dois?**
São dois objetos, cada um com o próprio nome, imagem, posição, controles, vidas e pontos.

**Como são decididos o bônus, o vencedor e o empate?**
Se exatamente um estiver vivo, recebe o bônus. Vence a maior pontuação inteira, mesmo que seja de quem foi eliminado. Pontuações iguais dão empate.

### Som

**Por que a falta de som é aceita, mas a falta de uma imagem gera erro?**
O som é um extra, e o jogo funciona sem ele. As imagens são obrigatórias no trabalho e necessárias para ver o jogo; o erro mostra o nome do arquivo que falta.

## 7. Roteiro para o ensaio

1. Demonstrar o menu, uma partida Solo e uma partida Versus.
2. Mostrar o game over e o botão "Jogar Novamente".
3. Abrir o código na ordem da seção 2.
4. Apontar um exemplo de cada conceito da seção 4.
5. Trocar de papel: cada pessoa deve conseguir explicar o código inteiro.

Sugestão de treino: mudar um valor em `configuracoes.py` e prever o que acontece antes de rodar o jogo.
