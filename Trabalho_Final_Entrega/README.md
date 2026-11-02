# 📬 Trabalho Final — Central de Atendimento

Imagine uma equipe recebendo pedidos de ajuda durante o dia: quem chegou primeiro precisa ser atendido, mas também deve ser possível corrigir um atendimento feito por engano. Esta Central de Atendimento representa essa situação em um programa simples de terminal.

Ao usar o menu, você pode registrar chamados, atender pela ordem de chegada, desfazer o atendimento mais recente, organizar os pendentes por prioridade e procurar um chamado pelo protocolo. No relatório, a contagem por prioridade mostra a recursão em funcionamento.

🧩 O trabalho reúne conceitos estudados no módulo: fila (**FIFO**), pilha (**LIFO**), ordenação, busca binária e recursão. Os chamados são exemplos de estudo e ficam na memória somente enquanto o programa está aberto.

## Executar pelo navegador

O projeto roda no navegador com o GitHub Codespaces, sem precisar instalar Python no computador.

1. Abra [Aulas_Python no Codespaces](https://codespaces.new/tslopes88/Aulas_Python) e entre na sua conta GitHub.
2. Crie um Codespace usando a branch `main`. Na primeira vez, o GitHub prepara o ambiente; aguarde até aparecer o editor do projeto.
3. Abra o terminal integrado pelo menu **Terminal → New Terminal**.
4. Entre na pasta do trabalho:

   ```bash
   cd Trabalho_Final_Entrega
   ```

5. Inicie a Central:

   ```bash
   python3 desafio_final.py
   ```

6. Digite o número da opção desejada e pressione Enter. Para sair do programa, escolha `0`.

## Conferir os testes

No mesmo terminal, ainda dentro de `Trabalho_Final_Entrega`, execute os testes do enunciado:

```bash
python3 desafio_final_testes.py
```

O resultado esperado é **9/9 testes passaram**. Também há testes complementares para verificar casos de borda:

```bash
python3 desafio_final_testes_complementares.py
```

O resultado esperado é **11/11 testes complementares passaram**.

## Arquivos

- `desafio_final.py` — código principal com o menu e as funções do trabalho.
- `desafio_final_testes.py` — testes originais do enunciado.
- `desafio_final_testes_complementares.py` — testes adicionais de casos de borda e validação.

Os chamados ficam na memória e são apagados quando o programa termina. Contas pessoais do Codespaces têm franquia mensal de uso; consulte [os limites e detalhes de cobrança](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces).
