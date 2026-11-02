# Guia de Uso da Central de Atendimento

Este guia explica como usar a **Central de Atendimento ao Cliente**, apresenta as estruturas de dados do trabalho e traz um roteiro curto para demonstrar o programa.

---

## 1. Visão Geral do Sistema

A Central de Atendimento gerencia os pedidos de suporte técnico dos clientes por meio de linha de comando (CLI), aplicando conceitos fundamentais de lógica de programação, estruturas de dados e algoritmos ensinados em aula.

### As 3 Estruturas de Dados do Sistema:
1. **Lista Geral (`todos`):**
   - É uma lista Python tradicional (`list`) que armazena todos os chamados registrados desde o início.
   - Os chamados entram em ordem estritamente cronológica, garantindo que estejam sempre ordenados pelos números de protocolo (1, 2, 3...).
2. **Fila de Espera (`fila`):**
   - Implementada com `collections.deque` no modelo **FIFO** (*First In, First Out*).
   - O primeiro cliente que chega é o primeiro a ser atendido.
3. **Pilha de Histórico (`historico`):**
   - Implementada com uma lista Python (`list`) operando no modelo **LIFO** (*Last In, First Out*).
   - Registra os atendimentos finalizados. Se houver necessidade de desfazer uma ação, o último atendimento concluído é retirado do topo da pilha.

---

## 2. O Ciclo de Vida do Atendimento

A jornada de um chamado técnico dentro da aplicação segue este fluxo visual:

```text
               [ Chegada do Cliente ]
                         │
                         ▼
             1. ABRIR CHAMADO (Opção 1)
             - Informa: Nome, Problema, Prioridade
             - Protocolo sequencial gerado automaticamente
             - Entra no final da FILA (append)
                         │
                         ▼
            2. ATENDER PRÓXIMO (Opção 2)
            - Sai do início da FILA (popleft)
            - Status muda de "pendente" para "atendido"
            - Entra no topo da PILHA de histórico (append)
                         │
         ┌───────────────┴───────────────┐
         │                               │
         ▼                               ▼
    [ Atendimento Concluído ]    3. DESFAZER ATENDIMENTO (Opção 3)
                                 - Sai do topo da PILHA (pop)
                                 - Status volta para "pendente"
                                 - Retorna à FRENTE da FILA (appendleft)
```

---

## 3. Passo a Passo Completo das Opções do Menu

Ao executar `python desafio_final.py`, você terá à disposição o menu principal com 7 opções:

```text
=============================================
     CENTRAL DE ATENDIMENTO AO CLIENTE
=============================================
1. Abrir chamado
2. Atender proximo chamado
3. Desfazer atendimento
4. Consultar chamados
5. Relatorio
6. Guia de uso
7. Sair
=============================================
```

---

### Opção 1: Abrir Chamado
Permite registrar um novo chamado no sistema.

1. **O que é solicitado:**
   - **Nome do cliente:** texto obrigatório (o sistema rejeita entradas em branco).
   - **Descrição do problema:** texto obrigatório explicando o defeito (ex: *Computador travando na inicialização*).
   - **Prioridade de atendimento:** número inteiro de 1 a 3:
     - `1` = Baixa (dúvidas simples, pedidos de rotina).
     - `2` = Média (defeitos que não paralisam a operação).
     - `3` = Alta (servidores fora do ar, paradas críticas).
2. **Como o sistema processa:**
   - O protocolo é gerado de forma automática e sequencial: se o sistema tem 0 chamados, gera o `1`; se tem 3, gera o `4`.
   - O chamado entra no final da fila de espera (`fila.append()`).
   - O comprovante com o número do protocolo `#001` é exibido na tela.
3. **Pausa:** Pressione `[ENTER]` para retornar ao menu principal.

---

### Opção 2: Atender Próximo Chamado
Realiza o atendimento seguindo o conceito de **Fila FIFO**.

1. **Como funciona:**
   - O cliente que está aguardando há mais tempo é retirado da frente da fila (`fila.popleft()`).
   - Seu status é alterado de `pendente` para `atendido`.
   - O chamado é arquivado no histórico de atendimentos (`historico.append()`).
2. **Fila vazia:** Se não houver ninguém na fila, o sistema informa educadamente: *"A fila esta vazia. Nenhum chamado para atender."*
3. **Pausa:** Pressione `[ENTER]` para retornar ao menu principal.

---

### Opção 3: Desfazer Atendimento
Permite cancelar um atendimento realizado por engano, utilizando o conceito de **Pilha LIFO**.

1. **Como funciona:**
   - Retira o atendimento mais recente do topo da pilha de histórico (`historico.pop()`).
   - O status do chamado retorna para `pendente`.
   - O chamado é devolvido para a **frente da fila de espera** (`fila.appendleft()`), garantindo que ele será o próximo a ser chamado novamente.
2. **Histórico vazio:** Se nenhum atendimento tiver sido feito, o sistema avisa: *"Historico vazio. Nada para desfazer."*
3. **Pausa:** Pressione `[ENTER]` para retornar ao menu principal.

---

### Opção 4: Consultar Chamados (Submenu)
Abre um submenu com 4 opções dedicadas de visualização e busca:

```text
----------------------------------------
          CONSULTAR CHAMADOS
----------------------------------------
1. Ver fila de espera
2. Ordenar por prioridade
3. Buscar por protocolo
4. Voltar
----------------------------------------
```

* **1. Ver fila de espera:**
  Lista todos os clientes que ainda não foram atendidos, na ordem cronológica exata em que chegaram. Mostra o protocolo `#001`, prioridade, status e dados do cliente.
* **2. Ordenar por prioridade (Bubble Sort Manual):**
  Executa o algoritmo manual de ordenação Bubble Sort sem usar `sort()` ou `sorted()`. Organiza os chamados em ordem decrescente de urgência (3-Alta no topo, depois 2-Média, depois 1-Baixa).
  *Estabilidade:* Se dois clientes tiverem a mesma prioridade, quem chegou primeiro continua na frente. A fila original de atendimento não é alterada.
* **3. Buscar por protocolo (Busca Binária):**
  Utiliza o algoritmo de Busca Binária ($O(\log n)$) para encontrar qualquer chamado registrado no sistema.
  - O sistema informa os limites existentes (ex: de 1 até o total cadastrado).
  - Digite o número do protocolo desejado.
  - O chamado é localizado e exibido imediatamente com seu status atual (`pendente` ou `atendido`).
* **4. Voltar:**
  Retorna imediatamente ao menu principal.

---

### Opção 5: Relatório Geral
Apresenta o painel de estatísticas da central:

1. **Indicadores exibidos:**
   - Total de chamados cadastrados desde o início.
   - Quantidade de chamados aguardando atendimento na fila.
   - Quantidade de atendimentos concluídos.
2. **Contagem por Prioridade (Recursão Pura):**
   - Calcula quantos chamados de prioridade Alta (3), Média (2) e Baixa (1) foram abertos.
   - O cálculo é feito por uma **função recursiva pura**, sem laços `for` ou `while` e sem a função `sum()`, percorrendo a lista elemento por elemento.
3. **Pausa:** Pressione `[ENTER]` para retornar ao menu principal.

---

### Opção 6: Guia de Uso (Manual Interativo no Terminal)
Abre o submenu interativo de ajuda diretamente no terminal:

```text
--------------------------------------------------
          GUIA COMPLETO DE USO DO SISTEMA
--------------------------------------------------
1. Visao geral e fluxo do atendimento
2. Como abrir chamados e entender protocolos
3. Como atender (Fila) e desfazer (Pilha)
4. Como consultar: Fila, Bubble Sort e Busca
5. Como funciona o relatorio e a recursao
6. Ver resumo completo de uma vez
7. Voltar ao menu principal
--------------------------------------------------
```
Permite ler explicações didáticas de cada parte do sistema sem precisar sair do programa.

---

### Opção 7: Sair
Encerra a execução da aplicação com mensagem de encerramento amigável.

---

## 4. O que é o Protocolo e Como Conseguir o Seu Número

O **protocolo** é o identificador único gerado para cada chamado. Ele é gerado sequencialmente pelo sistema a partir do número **1**.

Você pode saber o protocolo de um chamado de 3 maneiras:
1. **No comprovante de abertura:** Assim que um chamado é aberto na Opção 1, o sistema imprime `#001`, `#002`, etc.
2. **Na consulta da fila:** Na Opção 4 -> 1, o protocolo aparece no início de cada linha.
3. **Na lista ordenada por prioridade:** Na Opção 4 -> 2, os protocolos também são exibidos.

---

## 5. Roteiro de Apresentação

Use este roteiro para mostrar as principais operações do programa:

1. **Cadastrar 3 chamados (Opção 1):**
   - Chamado 1: Nome `Carlos`, Problema `Mouse quebrado`, Prioridade `1-Baixa` (Protocolo gerado: 1).
   - Chamado 2: Nome `Beatriz`, Problema `Servidor caiu`, Prioridade `3-Alta` (Protocolo gerado: 2).
   - Chamado 3: Nome `Andre`, Problema `Impressora travada`, Prioridade `2-Media` (Protocolo gerado: 3).

2. **Demonstrar Consultas, Bubble Sort e Busca Binária (Opção 4):**
   - Escolha `1` (Ver fila): mostre que Carlos é o primeiro, pois chegou primeiro (**FIFO**).
   - Escolha `2` (Ordenar por prioridade): mostre que Beatriz subiu para o topo por ter prioridade 3 (**Bubble Sort manual estável**).
   - Escolha `3` (Buscar por protocolo): digite `2` e mostre a **Busca Binária** localizando a Beatriz.
   - Escolha `4` para voltar.

3. **Demonstrar o Atendimento (Opção 2):**
   - Realize o atendimento: Carlos é atendido primeiro, confirmando a regra da fila.

4. **Demonstrar o Desfazer Atendimento (Opção 3):**
   - Desfaça o atendimento: Carlos é retirado do histórico e devolvido à frente da fila (**Pilha LIFO**).

5. **Demonstrar o Relatório com Recursão (Opção 5):**
   - Exiba o relatório: mostre a contagem de cada prioridade calculada por função recursiva pura.

6. **Demonstrar o Guia de Uso Embutido (Opção 6):**
   - Mostre que o sistema possui um menu completo de ajuda para os usuários.
