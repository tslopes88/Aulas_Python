# Trabalho Final — Central de Atendimento

Este trabalho simula uma central simples para registrar chamados de suporte, organizar a fila e acompanhar os atendimentos. A ideia foi praticar as estruturas de dados e os algoritmos estudados no módulo.

## O que o programa faz

- Registra chamados com nome, descrição e prioridade.
- Atende pela ordem de chegada (fila FIFO).
- Permite desfazer o atendimento mais recente (pilha LIFO).
- Exibe os chamados pendentes por prioridade usando Bubble Sort.
- Localiza um chamado pelo protocolo usando busca binária.
- Mostra um relatório com a contagem recursiva por prioridade.

Os dados ficam na memória durante a execução. Ao encerrar o programa, os chamados são perdidos; não são usados dados reais de clientes.

## Como executar

É necessário ter Python 3 instalado. Abra o terminal nesta pasta e rode:

```bash
python desafio_final.py
```

No Windows, também pode ser necessário usar:

```bash
py desafio_final.py
```

Escolha uma opção no menu e siga as perguntas. Os protocolos são gerados automaticamente. Para ver uma demonstração de uso, consulte o [guia de uso](GUIA_DE_USO.md).

## Como executar os testes

Os testes usam apenas a biblioteca padrão do Python e dados fictícios:

```bash
python -m unittest -v desafio_final_testes.py
```

Ou, diretamente:

```bash
python test_desafio_final.py
```

## Organização dos arquivos

- `desafio_final.py` — programa principal e implementação das estruturas e algoritmos.
- `desafio_final_testes.py` — testes de operações, casos de borda e navegação pelo menu.
- `test_desafio_final.py` — ponto de entrada alternativo para os testes.
- `GUIA_DE_USO.md` — instruções e roteiro de demonstração.

## O que este trabalho pratica

O Bubble Sort organiza uma cópia da fila, sem mudar a ordem de atendimento. A busca binária usa os protocolos sequenciais para localizar um chamado na lista geral. A contagem recursiva percorre os chamados e soma os que têm cada prioridade. A fila e a busca assumem que os chamados são criados pela função do próprio programa e mantêm os protocolos em ordem.

Como a contagem é recursiva, ela serve para demonstrar o conceito em uma lista pequena; listas muito grandes podem atingir o limite de recursão do Python.
