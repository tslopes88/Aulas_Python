# 📬 Trabalho Final — Central de Atendimento

Imagine uma equipe recebendo pedidos de ajuda durante o dia: quem chegou primeiro precisa ser atendido, mas também deve ser possível corrigir um atendimento feito por engano. Esta Central de Atendimento representa essa situação em um programa simples de terminal.

Ao usar o menu, você pode registrar chamados, atender pela ordem de chegada, desfazer o atendimento mais recente, organizar os pendentes por prioridade e procurar um chamado pelo protocolo. No relatório, a contagem por prioridade mostra a recursão em funcionamento.

🧩 O trabalho reúne conceitos estudados no módulo: fila (**FIFO**), pilha (**LIFO**), ordenação, busca binária e recursão. Os chamados são exemplos de estudo e ficam na memória somente enquanto o programa está aberto.

## Executar pelo navegador

O projeto roda no navegador com o GitHub Codespaces, sem precisar instalar Python no computador.

1. Abra [Aulas_Python no Codespaces](https://codespaces.new/tslopes88/Aulas_Python) e entre na sua conta GitHub.
2. Crie um Codespace usando a branch `main`. Na primeira vez, o GitHub prepara o ambiente; aguarde até aparecer o editor do projeto.
3. Abra o terminal integrado pelo menu **Terminal → New Terminal**. Os comandos abaixo devem ser digitados nesse terminal, não no campo de busca do GitHub.
4. Entre na pasta do trabalho final:

   ```bash
   cd Trabalho_Final_Entrega
   ```

5. Inicie a Central:

   ```bash
   python3 desafio_final.py
   ```

6. Quando aparecer o menu, digite o número da opção desejada e pressione Enter. Siga as perguntas para cadastrar, atender ou consultar chamados. Para sair do programa, escolha `0`.

### Conferir os testes

No mesmo terminal, ainda dentro da pasta `Trabalho_Final_Entrega`, execute:

```bash
python3 desafio_final_testes.py
```

O resultado esperado é **9/9 testes passaram**. Depois, você pode iniciar novamente `python3 desafio_final.py` para experimentar o menu.

### Encerrar o Codespace

Os chamados deste exercício ficam na memória e são apagados quando o programa termina. Ao acabar de estudar, feche o terminal e pare o Codespace na página [github.com/codespaces](https://github.com/codespaces). Contas pessoais têm uma franquia mensal de uso; consulte [os limites e detalhes de cobrança](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces).

## Arquivos

- `desafio_final.py` — programa e funções completadas.
- `desafio_final_testes.py` — testes fornecidos junto com o enunciado.
