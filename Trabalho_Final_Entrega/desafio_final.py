"""
CENTRAL DE ATENDIMENTO DE SUPORTE TECNICO
Trabalho de Conclusao de Modulo - Escola de Programadores
Disciplina: Logica de Programacao e Estruturas de Dados em Python
Aluno: Thiago Lopes
Arquivo: desafio_final.py
"""

from collections import deque


# ===========================================================================
# 1. FUNCOES AUXILIARES DE VALIDACAO E PROTOCOLO
# ===========================================================================

def gerar_proximo_protocolo(todos: list) -> int:
    """Gera o proximo numero de protocolo sequencial (1, 2, 3...)."""
    return len(todos) + 1


def validar_prioridade(prioridade: int) -> int:
    """Valida se a prioridade e um inteiro entre 1 e 3."""
    if isinstance(prioridade, bool) or not isinstance(prioridade, int):
        raise TypeError("A prioridade deve ser um numero inteiro.")
    if prioridade not in (1, 2, 3):
        raise ValueError("A prioridade deve ser 1 (baixa), 2 (media) ou 3 (alta).")
    return prioridade


def validar_texto(texto: str, campo: str = "texto") -> str:
    """Valida se o texto nao e nulo nem vazio."""
    if not isinstance(texto, str):
        raise TypeError(f"O campo '{campo}' deve ser um texto.")
    limpo = texto.strip()
    if not limpo:
        raise ValueError(f"O campo '{campo}' nao pode ficar em branco.")
    return limpo


def criar_chamado(protocolo: int, nome: str, descricao: str, prioridade: int) -> dict:
    """Cria o dicionario que representa um chamado."""
    return {
        "protocolo": protocolo,
        "nome": validar_texto(nome, "nome"),
        "descricao": validar_texto(descricao, "descricao"),
        "prioridade": validar_prioridade(prioridade),
        "status": "pendente"
    }


# ===========================================================================
# 2. NIVEL 1 - FILA (FIFO: First In, First Out)
# ===========================================================================

def abrir_chamado(fila: deque, todos: list, nome: str, descricao: str, prioridade: int) -> dict:
    """
    Abre um novo chamado:
    - Gera protocolo sequencial.
    - Entra no fim da fila com append() (FIFO).
    - Guarda no historico geral 'todos'.
    """
    protocolo = gerar_proximo_protocolo(todos)
    chamado = criar_chamado(protocolo, nome, descricao, prioridade)
    todos.append(chamado)
    fila.append(chamado)
    return chamado


def atender_proximo(fila: deque, historico: list):
    """
    Atende o primeiro chamado da fila com popleft() (FIFO).
    Muda status para 'atendido' e adiciona na pilha de historico.
    Se a fila estiver vazia, retorna None.
    """
    if len(fila) == 0:
        return None
    chamado = fila.popleft()
    chamado["status"] = "atendido"
    historico.append(chamado)
    return chamado


# ===========================================================================
# 3. NIVEL 2 - PILHA (LIFO: Last In, First Out)
# ===========================================================================

def desfazer_atendimento(fila: deque, historico: list):
    """
    Desfaz o ultimo atendimento retirando do topo da pilha com pop() (LIFO).
    Muda status de volta para 'pendente' e devolve a frente da fila com appendleft().
    Se nao houver historico, retorna None.
    """
    if len(historico) == 0:
        return None
    chamado = historico.pop()
    chamado["status"] = "pendente"
    fila.appendleft(chamado)
    return chamado


def consultar_ultimo_atendido(historico: list):
    """Consulta o ultimo chamado atendido sem desempilhar."""
    if not historico:
        return None
    return historico[-1]


# ===========================================================================
# 4. NIVEL 3 - ORDENACAO POR PRIORIDADE (BUBBLE SORT MANUAL)
# ===========================================================================

def ordenar_por_prioridade(chamados) -> list:
    """
    Ordena os chamados por prioridade decrescente (3 -> 2 -> 1).
    Utiliza Bubble Sort manual com comparacao estrita (<) para manter a estabilidade.
    Opera sobre uma copia da fila, sem alterar a ordem original.
    """
    copia = list(chamados)
    n = len(copia)

    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if copia[j]["prioridade"] < copia[j + 1]["prioridade"]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
                trocou = True
        if not trocou:
            break

    return copia


# ===========================================================================
# 5. NIVEL 4 - BUSCA BINARIA E RECURSAO
# ===========================================================================

def buscar_protocolo(todos: list, protocolo: int):
    """
    Busca binaria em O(log n) pelo numero de protocolo.
    Como os chamados sao inseridos sequencialmente, 'todos' ja esta ordenado por protocolo.
    Retorna o chamado encontrado ou None se nao existir.
    """
    if not todos or isinstance(protocolo, bool) or not isinstance(protocolo, int) or protocolo < 1:
        return None

    inicio = 0
    fim = len(todos) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        p_atual = todos[meio]["protocolo"]

        if p_atual == protocolo:
            return todos[meio]
        elif p_atual < protocolo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None


def contar_por_prioridade(chamados: list, prioridade: int, i: int = 0) -> int:
    """
    Conta chamados de uma prioridade usando recursao pura (sem laco e sem sum).
    - Caso base: chegou ao final da lista (i >= len(chamados)), retorna 0.
    - Passo recursivo: soma 1 (se a prioridade bater) com a contagem do restante (i + 1).
    Nota: no CPython, chamadas recursivas sao limitadas a profundidade padrao (~1000 chamadas).
    """
    if not chamados or i >= len(chamados):
        return 0

    atual = 1 if chamados[i].get("prioridade") == prioridade else 0
    return atual + contar_por_prioridade(chamados, prioridade, i + 1)


# ===========================================================================
# 6. INTERFACE COM O USUARIO (MENU E ENTRADAS)
# ===========================================================================

def ler_inteiro(mensagem: str, minimo: int, maximo: int) -> int:
    """Le um numero inteiro digitado pelo usuario dentro de um intervalo valido."""
    while True:
        try:
            texto = input(mensagem).strip()
            if not texto:
                print("Entrada vazia. Digite um numero.")
                continue
            valor = int(texto)
            if minimo <= valor <= maximo:
                return valor
            print(f"Opcao invalida. Digite um numero entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada invalida. Digite um valor numerico inteiro.")


def ler_texto_usuario(mensagem: str) -> str:
    """Le um texto do usuario garantindo que nao fique em branco."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Este campo nao pode ficar em branco. Tente novamente.")


def mostrar_chamado(chamado: dict) -> None:
    """Exibe os dados de um chamado de forma organizada."""
    rotulos = {1: "1-Baixa", 2: "2-Media", 3: "3-Alta"}
    prio_str = rotulos.get(chamado.get("prioridade", 1), str(chamado.get("prioridade")))
    print(f"#{chamado['protocolo']:03d} | Prioridade: {prio_str:<7} | "
          f"Status: {chamado['status']:<8} | {chamado['nome']} - {chamado['descricao']}")


def pausar() -> None:
    """Pausa a tela para leitura antes de retornar ao menu."""
    input("\nPressione [ENTER] para voltar...")


def submenu_consultar(fila: deque, todos: list) -> None:
    """Submenu para visualizacao e busca de chamados."""
    while True:
        print("\n" + "-" * 40)
        print("          CONSULTAR CHAMADOS")
        print("-" * 40)
        print("1. Ver fila de espera")
        print("2. Ordenar por prioridade")
        print("3. Buscar por protocolo")
        print("4. Voltar")
        print("-" * 40)

        op = ler_inteiro("Escolha uma opcao: ", 1, 4)

        if op == 4:
            break

        elif op == 1:
            print("\n--- FILA DE ESPERA (ORDEM DE CHEGADA) ---")
            if not fila:
                print("A fila de espera esta vazia.")
            else:
                for c in fila:
                    mostrar_chamado(c)
            pausar()

        elif op == 2:
            print("\n--- PENDENTES ORDENADOS POR PRIORIDADE (BUBBLE SORT) ---")
            if not fila:
                print("A fila de espera esta vazia.")
            else:
                ordenados = ordenar_por_prioridade(fila)
                for c in ordenados:
                    mostrar_chamado(c)
            pausar()

        elif op == 3:
            print("\n--- BUSCAR CHAMADO POR PROTOCOLO (BUSCA BINARIA) ---")
            if not todos:
                print("Nenhum chamado foi registrado ate o momento.")
            else:
                total = len(todos)
                print(f"Dica: Os protocolos sao sequenciais (de 1 ate {total}).")
                print("Voce tambem pode consultar os numeros na opcao 1 (Ver fila de espera).")
                protocolo = ler_inteiro(f"Numero do protocolo (1 a {total}): ", 1, 10**6)
                chamado = buscar_protocolo(todos, protocolo)
                if chamado:
                    print("[OK] Chamado encontrado:")
                    mostrar_chamado(chamado)
                else:
                    print(f"Protocolo #{protocolo} nao encontrado.")
            pausar()


def guia_visao_geral() -> None:
    """Explica a visao geral e as estruturas de dados do sistema."""
    print("\n" + "=" * 55)
    print("      1. VISAO GERAL E FLUXO DO SISTEMA")
    print("=" * 55)
    print("O que e o sistema:")
    print("  E uma Central de Atendimento que gerencia chamados de")
    print("  suporte tecnico utilizando estruturas de dados e")
    print("  algoritmos fundamentais em Python.")
    print("\nComo os dados estao organizados:")
    print("  * Lista Geral ('todos'): guarda o historico completo de")
    print("    todos os chamados registrados em ordem cronologica.")
    print("  * Fila de Espera ('fila'): guarda quem aguarda atendimento")
    print("    utilizando collections.deque no padrao FIFO.")
    print("  * Pilha de Atendidos ('historico'): guarda os atendimentos")
    print("    concluidos no padrao LIFO, permitindo desfazer se necessario.")
    print("=" * 55)
    pausar()


def guia_abrir_chamados() -> None:
    """Explica como abrir chamados e como funcionam os protocolos."""
    print("\n" + "=" * 55)
    print("      2. COMO ABRIR CHAMADOS E PROTOCOLOS")
    print("=" * 55)
    print("Como registrar um chamado (Opcao 1 do menu):")
    print("  1. Digite o Nome do cliente (obrigatorio, nao pode ser vazio).")
    print("  2. Digite a Descricao do problema relatado.")
    print("  3. Informe a Prioridade de atendimento:")
    print("     * 1 = Baixa  (solicitacoes rotineiras)")
    print("     * 2 = Media  (duvidas e problemas moderados)")
    print("     * 3 = Alta   (paradas de sistema, urgencias criticas)")
    print("\nComo funcionam os Protocolos:")
    print("  * O protocolo e gerado automaticamente na sequencia (1, 2, 3...).")
    print("  * O primeiro chamado e #001, o segundo e #002, e assim por diante.")
    print("  * O numero de protocolo aparece:")
    print("    - No comprovante exibido logo apos abrir o chamado.")
    print("    - Na opcao de consultar a fila (Opcao 4 -> 1).")
    print("    - Na opcao de listar por prioridade (Opcao 4 -> 2).")
    print("=" * 55)
    pausar()


def guia_atendimento_e_desfazer() -> None:
    """Explica como atender chamados e desfazer atendimentos."""
    print("\n" + "=" * 55)
    print("      3. ATENDIMENTO (FILA) E DESFAZER (PILHA)")
    print("=" * 55)
    print("Atender Proximo Chamado (Opcao 2 do menu):")
    print("  * Utiliza o conceito de FILA (FIFO: Primeiro a Entrar,")
    print("    Primeiro a Sair via deque.popleft()).")
    print("  * O cliente que esta ha mais tempo aguardando e atendido.")
    print("  * Seu status passa de 'pendente' para 'atendido' e ele vai")
    print("    para a pilha de historico de atendimentos.")
    print("\nDesfazer Ultimo Atendimento (Opcao 3 do menu):")
    print("  * Utiliza o conceito de PILHA (LIFO: Ultimo a Entrar,")
    print("    Primeiro a Sair via list.pop()).")
    print("  * Se o operador atendeu o chamado errado, essa opcao")
    print("    cancela o atendimento mais recente.")
    print("  * O chamado volta para o status 'pendente' e e colocado")
    print("    de volta na FRENTE da fila (via deque.appendleft()).")
    print("=" * 55)
    pausar()


def guia_consultas() -> None:
    """Explica as opcoes de consulta: fila, bubble sort e busca binaria."""
    print("\n" + "=" * 55)
    print("   4. CONSULTAS: FILA, BUBBLE SORT E BUSCA BINARIA")
    print("=" * 55)
    print("Submenu Consultar Chamados (Opcao 4 do menu):")
    print("\n1. Ver Fila de Espera:")
    print("   * Mostra os chamados que aguardam atendimento na ordem")
    print("     exata em que chegaram (ordem cronologica).")
    print("\n2. Ordenar por Prioridade (Bubble Sort Manual):")
    print("   * Algoritmo de ordenacao manual que coloca chamados")
    print("     urgentes no topo (3-Alta primeiro, depois 2-Media, depois 1-Baixa).")
    print("   * Estabilidade: Se dois chamados tem a mesma prioridade,")
    print("     a ordem de chegada deles e rigorosamente preservada.")
    print("   * A fila original de atendimento NAO e alterada.")
    print("\n3. Buscar por Protocolo (Busca Binaria):")
    print("   * Algoritmo de busca rapida em O(log n).")
    print("   * Divide a lista pela metade a cada comparacao para achar")
    print("     o chamado pelo numero do protocolo instantaneamente.")
    print("=" * 55)
    pausar()


def guia_relatorio() -> None:
    """Explica o relatorio geral e o funcionamento da recursao pura."""
    print("\n" + "=" * 55)
    print("      5. RELATORIO GERAL E CONTAGEM RECURSIVA")
    print("=" * 55)
    print("Relatorio Geral (Opcao 5 do menu):")
    print("  * Total de Chamados: quantidade total cadastrada no sistema.")
    print("  * Aguardando Atendimento: tamanho atual da fila de espera.")
    print("  * Atendimentos Concluidos: quantidade de chamados ja atendidos.")
    print("\nContagem por Prioridade via Recursao Pura:")
    print("  * O calculo de quantos chamados existem de cada prioridade")
    print("    e feito por uma funcao recursiva, sem lacos (for/while)")
    print("    e sem funcoes prontas (sum).")
    print("  * Caso Base: se o indice chegar ao final da lista, retorna 0.")
    print("  * Passo Indutivo: soma 1 (se a prioridade bater) com a")
    print("    chamada recursiva do proximo elemento.")
    print("=" * 55)
    pausar()


def guia_manual_completo() -> None:
    """Exibe o resumo completo de todos os recursos de uma vez."""
    print("\n" + "=" * 55)
    print("       MANUAL COMPLETO DA CENTRAL DE ATENDIMENTO")
    print("=" * 55)
    print("1. OBJETIVO: Gerenciar o atendimento ao cliente usando Python.")
    print("2. ABERTURA (Opcao 1): Cadastra cliente com Nome, Descricao e")
    print("   Prioridade (1 a 3). O protocolo e gerado automaticamente (1, 2, 3...).")
    print("3. ATENDIMENTO (Opcao 2): Atende o primeiro da fila (FIFO).")
    print("4. DESFAZER (Opcao 3): Cancela o ultimo atendimento e devolve o")
    print("   chamado a frente da fila (LIFO).")
    print("5. CONSULTAR (Opcao 4):")
    print("   - Fila de espera na ordem de chegada.")
    print("   - Ordenacao decrescente estavel por prioridade (Bubble Sort).")
    print("   - Busca rapida de chamado por protocolo (Busca Binaria).")
    print("6. RELATORIO (Opcao 5): Estatisticas gerais e contagem por prioridade")
    print("   calculada por funcao recursiva pura.")
    print("=" * 55)
    pausar()


def submenu_guia() -> None:
    """Submenu interativo com o guia completo de uso do sistema."""
    while True:
        print("\n" + "-" * 50)
        print("          GUIA COMPLETO DE USO DO SISTEMA")
        print("-" * 50)
        print("1. Visao geral e fluxo do atendimento")
        print("2. Como abrir chamados e entender protocolos")
        print("3. Como atender (Fila) e desfazer (Pilha)")
        print("4. Como consultar: Fila, Bubble Sort e Busca")
        print("5. Como funciona o relatorio e a recursao")
        print("6. Ver resumo completo de uma vez")
        print("7. Voltar ao menu principal")
        print("-" * 50)

        op = ler_inteiro("Escolha um topico do guia: ", 1, 7)

        if op == 7:
            break
        elif op == 1:
            guia_visao_geral()
        elif op == 2:
            guia_abrir_chamados()
        elif op == 3:
            guia_atendimento_e_desfazer()
        elif op == 4:
            guia_consultas()
        elif op == 5:
            guia_relatorio()
        elif op == 6:
            guia_manual_completo()


def menu(fila: deque = None, todos: list = None, historico: list = None) -> None:
    """Menu principal da Central de Atendimento."""
    if fila is None:
        fila = deque()
    if todos is None:
        todos = []
    if historico is None:
        historico = []

    while True:
        print("\n" + "=" * 45)
        print("     CENTRAL DE ATENDIMENTO AO CLIENTE")
        print("=" * 45)
        print("1. Abrir chamado")
        print("2. Atender proximo chamado")
        print("3. Desfazer atendimento")
        print("4. Consultar chamados")
        print("5. Relatorio")
        print("6. Guia de uso")
        print("7. Sair")
        print("=" * 45)

        op = ler_inteiro("Escolha uma opcao: ", 1, 7)

        if op == 7:
            print("\nEncerrando a Central de Atendimento. Ate logo!")
            break

        elif op == 1:
            print("\n--- ABRIR NOVO CHAMADO ---")
            nome = ler_texto_usuario("Nome do cliente: ")
            descricao = ler_texto_usuario("Descricao do problema: ")
            print("Prioridade: 1=Baixa, 2=Media, 3=Alta")
            prioridade = ler_inteiro("Prioridade (1-3): ", 1, 3)
            chamado = abrir_chamado(fila, todos, nome, descricao, prioridade)
            print("\n[OK] Chamado registrado com sucesso!")
            mostrar_chamado(chamado)
            pausar()

        elif op == 2:
            print("\n--- ATENDER PROXIMO CHAMADO ---")
            chamado = atender_proximo(fila, historico)
            if chamado:
                print("[OK] Chamado atendido:")
                mostrar_chamado(chamado)
            else:
                print("A fila esta vazia. Nenhum chamado para atender.")
            pausar()

        elif op == 3:
            print("\n--- DESFAZER ULTIMO ATENDIMENTO ---")
            chamado = desfazer_atendimento(fila, historico)
            if chamado:
                print("[OK] Atendimento desfeito. Chamado devolvido a frente da fila:")
                mostrar_chamado(chamado)
            else:
                print("Historico vazio. Nada para desfazer.")
            pausar()

        elif op == 4:
            submenu_consultar(fila, todos)

        elif op == 5:
            print("\n--- RELATORIO GERAL ---")
            print(f"Total de chamados registrados: {len(todos)}")
            print(f"Aguardando atendimento:        {len(fila)}")
            print(f"Atendimentos concluidos:       {len(historico)}")
            print("-" * 40)
            print("Contagem por prioridade (calculada via recursao):")
            for p, rotulo in ((3, "Alta (3) "), (2, "Media (2)"), (1, "Baixa (1)")):
                total_prio = contar_por_prioridade(todos, p)
                print(f"  * Prioridade {rotulo}: {total_prio} chamado(s)")
            pausar()

        elif op == 6:
            submenu_guia()


if __name__ == "__main__":
    menu()
