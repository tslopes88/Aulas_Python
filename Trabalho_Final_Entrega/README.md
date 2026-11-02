# 📬 Trabalho Final — Central de Atendimento

Imagine uma equipe recebendo pedidos de ajuda durante o dia: quem chegou primeiro precisa ser atendido, mas também deve ser possível corrigir um atendimento feito por engano. Esta Central de Atendimento representa essa situação em um programa simples de terminal.

Ao usar o menu, você pode registrar chamados, atender pela ordem de chegada, desfazer o atendimento mais recente, organizar os pendentes por prioridade e procurar um chamado pelo protocolo. No relatório, a contagem por prioridade mostra a recursão em funcionamento.

🧩 O trabalho reúne conceitos estudados no módulo: fila (**FIFO**), pilha (**LIFO**), ordenação, busca binária e recursão. Os chamados são exemplos de estudo e ficam na memória somente enquanto o programa está aberto.

## Como executar

### Pelo navegador, usando GitHub Codespaces

Você pode abrir e executar o projeto sem instalar Python no seu computador:

1. Acesse [Aulas_Python no Codespaces](https://codespaces.new/tslopes88/Aulas_Python) e entre na sua conta GitHub.
2. Crie um Codespace para a branch `main` e espere o ambiente abrir.
3. No terminal do Codespace, entre na pasta do trabalho:

   ```bash
   cd Trabalho_Final_Entrega
   ```

4. Inicie o programa:

   ```bash
   python3 desafio_final.py
   ```

5. Escolha as opções no menu e digite as respostas no terminal. Para encerrar, escolha `0`.

O Codespaces tem franquia mensal de uso para contas pessoais; confira [os limites e detalhes de cobrança](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces).

### No computador

Com Python instalado, abra o terminal nesta pasta e rode:

```bash
python desafio_final.py
```

No Windows, você também pode usar:

```bash
py desafio_final.py
```

## Como executar os testes

Para executar os testes no Codespaces, estando dentro de `Trabalho_Final_Entrega`, rode:

```bash
python3 desafio_final_testes.py
```

No computador, rode os testes fornecidos para conferir as funções:

```bash
python desafio_final_testes.py
```

Quando os nove testes passarem, execute o programa e experimente as opções do menu. Os chamados ficam na memória enquanto o programa está aberto.

## Arquivos

- `desafio_final.py` — programa e funções completadas.
- `desafio_final_testes.py` — testes fornecidos junto com o enunciado.
