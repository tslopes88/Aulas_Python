# Aulas de Python — Escola de Programação

Projeto de aprendizagem em Python para estudar e praticar com meus amigos e colegas. Reúne exercícios, jogos, um menu interativo e um curso guiado por desafios, do básico a pequenos sistemas.

## Executar no navegador

Também dá para praticar sem instalar Python no computador, usando o GitHub Codespaces:

1. Abra [Aulas_Python no Codespaces](https://codespaces.new/tslopes88/Aulas_Python) e entre na sua conta GitHub.
2. Crie um Codespace para a branch `main` e aguarde o ambiente abrir no navegador.
3. No terminal do Codespace, execute:

   ```bash
   python3 menu_exercicios.py
   ```

4. Escolha o curso guiado no menu e responda aos desafios pelo terminal.

Cada pessoa pode criar seu próprio ambiente Codespaces. O GitHub oferece uma franquia mensal para contas pessoais; confira [os limites e detalhes de cobrança](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces) antes de usar, pois o uso além da franquia pode gerar cobrança conforme as configurações da conta.

## O que você vai encontrar

- **Curso guiado:** aulas rápidas, desafios com novas tentativas e dicas.
- **Menu de exercícios:** escolha exemplos por nível ou tema.
- **Modo professor:** consulte objetivos e explicações dos exercícios.
- **Projetos para praticar:** calculadora, jogos, agenda, biblioteca e outros programas de terminal.
- **Progresso local:** o programa salva quais atividades você concluiu no seu computador.

## Como baixar o projeto

1. Abra a página do repositório no GitHub: <https://github.com/tslopes88/Aulas_Python>.
2. Clique em **Code** e escolha **Download ZIP**; ou clone pelo terminal:

   ```bash
   git clone https://github.com/tslopes88/Aulas_Python.git
   ```

3. Se baixou o ZIP, extraia a pasta para um local fácil de encontrar.
4. Abra o Prompt de Comando ou PowerShell dentro da pasta `Aulas_Python`.

## Preparar o Python

Instale o Python 3 no computador, se ainda não tiver. No Windows, durante a instalação, habilite a opção para adicionar o Python ao PATH.

Confira a instalação no terminal:

```bash
py --version
```

Se o comando `py` não estiver disponível, tente:

```bash
python --version
```

Este projeto usa apenas a biblioteca padrão do Python; não é necessário instalar pacotes adicionais para iniciar os exercícios.

## Iniciar o programa

No Windows, dê dois cliques em `executar_menu.bat`.

Ou abra o terminal na pasta do projeto e execute:

```bash
py menu_exercicios.py
```

Se você usa `python` em vez de `py`:

```bash
python menu_exercicios.py
```

No menu, escolha a opção **1** para começar ou continuar o curso guiado. Leia a aula rápida e digite sua resposta quando o desafio aparecer. Se precisar, use `/dica`; para pausar, digite `/sair`.

## Executar um exercício separado

Você também pode abrir um arquivo diretamente pelo terminal, por exemplo:

```bash
py boas_vindas.py
py calculadora.py
py jogo_adivinhacao.py
```

Troque o nome do arquivo por outro exercício que queira praticar. No Windows, também é possível abrir um arquivo `.py` pelo editor de código e executá-lo por lá.

## Executar os testes

Com o Python instalado, rode os testes a partir da pasta do projeto:

```bash
py -m unittest test_projeto.py -v
```

Os testes usam somente a biblioteca padrão e arquivos temporários.

## Arquivos de progresso

O progresso do curso e dos exercícios é salvo localmente em arquivos `progresso_*.json`. Esses arquivos são pessoais e não precisam ser publicados. Se quiser começar do zero, feche o programa e remova os arquivos de progresso da sua cópia local.

## Estrutura principal

- `menu_exercicios.py` — menu, trilhas e registro de exercícios.
- `curso_guiado.py` — aulas rápidas, desafios, dicas e progresso do curso.
- `modo_professor.py` — explicações e objetivos dos exercícios.
- `test_projeto.py` — testes automatizados do menu e do curso guiado.
- `executar_menu.bat` — atalho para iniciar o menu no Windows.
- Os demais arquivos `.py` — exercícios e pequenos projetos.

## Para quem está começando

1. Comece pelo curso guiado ou pelos exercícios de nível iniciante.
2. Tente resolver cada atividade antes de consultar a resposta.
3. Leia as mensagens e explicações do programa para entender o conceito.
4. Altere os exemplos e observe como o resultado muda.
5. Avance para os projetos intermediários quando estiver confortável com variáveis, condições, repetições e funções.

Este repositório é material de estudo. Os exemplos de cadastro, banco e estoque são exercícios didáticos, não sistemas para armazenar dados reais.
