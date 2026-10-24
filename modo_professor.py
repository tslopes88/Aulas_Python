from pathlib import Path


LISTA = {
    "1": {
        "titulo": "Boas-vindas / IMC / Média / Funções",
        "arquivo": "boas_vindas.py",
        "nivel": "Iniciante",
        "categoria": "Fundamentos",
        "objetivo": "Introduzir variáveis, entrada, cálculos e funções simples.",
        "explicacao": "Este é um conjunto de exercícios iniciais. O objetivo é mostrar como receber entrada do usuário, trabalhar com variáveis, calcular valores, e usar funções simples em Python."
    },
    "2": {
        "titulo": "Sistema de notas da turma",
        "arquivo": "sistema_notas_turma.py",
        "nivel": "Iniciante",
        "categoria": "Lógica",
        "objetivo": "Calcular médias, validar dados e tomar decisões.",
        "explicacao": "Aqui o aluno aprende a validar dados, somar notas, calcular média, identificar maior e menor valor e contar aprovados e reprovados. É um excelente exercício para praticar loops e condicionais."
    },
    "3": {
        "titulo": "Loteria",
        "arquivo": "loteria.py",
        "nivel": "Intermediário",
        "categoria": "Aleatoriedade",
        "objetivo": "Gerar sorteios, comparar listas e descobrir acertos.",
        "explicacao": "Este exercício ensina como gerar números aleatórios, comparar listas e verificar acertos. Também trabalha com estruturas de decisão e sorteio."
    },
    "4": {
        "titulo": "Conversor de temperatura",
        "arquivo": "conversor_temperatura.py",
        "nivel": "Iniciante",
        "categoria": "Cálculo",
        "objetivo": "Transformar valores entre Celsius e Fahrenheit.",
        "explicacao": "Você usa entrada do usuário, condicionais e fórmulas matemáticas para transformar Celsius em Fahrenheit e vice-versa."
    },
    "5": {
        "titulo": "Média de notas",
        "arquivo": "media_notas.py",
        "nivel": "Iniciante",
        "categoria": "Estruturas",
        "objetivo": "Ler várias notas, calcular média e exibir a situação final.",
        "explicacao": "Este programa mostra como ler várias notas, calcular a média e exibir a situação final do aluno, usando estrutura de repetição e condição."
    },
    "6": {
        "titulo": "Jogo da adivinhação",
        "arquivo": "jogo_adivinhacao.py",
        "nivel": "Intermediário",
        "categoria": "Jogo",
        "objetivo": "Usar aleatoriedade e repetição para adivinhar um número.",
        "explicacao": "Aqui o aluno aprende a usar números aleatórios e tentar adivinhar um valor em um número limitado de tentativas. É um ótimo exemplo de loop com controle de erros."
    },
    "7": {
        "titulo": "Cadastro de alunos",
        "arquivo": "cadastro_alunos.py",
        "nivel": "Intermediário",
        "categoria": "Dados",
        "objetivo": "Trabalhar com dicionários e informações estruturadas.",
        "explicacao": "Esse exercício introduz dicionários, que são estruturas de dados muito usadas para armazenar informações em chave e valor, como nome e média."
    },
    "8": {
        "titulo": "Agenda de contatos",
        "arquivo": "agenda_contatos.py",
        "nivel": "Intermediário",
        "categoria": "Dados",
        "objetivo": "Organizar contatos com listas e menus interativos.",
        "explicacao": "Uma agenda demonstra como trabalhar com listas de dicionários, menu interativo e armazenamento temporário em memória."
    },
    "9": {
        "titulo": "Controle de estoque",
        "arquivo": "controle_estoque.py",
        "nivel": "Intermediário",
        "categoria": "Sistema",
        "objetivo": "Gerenciar produtos, preços e quantidades.",
        "explicacao": "Este exercício mostra como registrar produtos, quantidades e preços, além de buscar itens no estoque. A ideia é praticar dicionários e estruturas de repetição."
    },
    "10": {
        "titulo": "Sistema bancário",
        "arquivo": "sistema_bancario.py",
        "nivel": "Intermediário",
        "categoria": "Sistema",
        "objetivo": "Simular operações bancárias e validações de saldo.",
        "explicacao": "O aluno aprende a simular operações bancárias com saldo, depósito e saque. Também é um ótimo caso para trabalhar com controle de fluxo e validações."
    },
    "11": {
        "titulo": "Jogo da forca",
        "arquivo": "jogo_forca.py",
        "nivel": "Avançado",
        "categoria": "Jogo",
        "objetivo": "Combinar lógica, listas, condicionais e controle de erros.",
        "explicacao": "Esse projeto é mais avançado: combina listas, condições, letras descobertas e contagem de erros. É um ótimo treino para lógica e tomada de decisão."
    },
    "12": {
        "titulo": "Biblioteca",
        "arquivo": "biblioteca.py",
        "nivel": "Intermediário",
        "categoria": "Sistema",
        "objetivo": "Cadastrar, buscar e manter registros de livros.",
        "explicacao": "A biblioteca ensina a organizar dados com listas e dicionários, além de fazer buscas e cadastrar registros com menu."
    },
    "13": {
        "titulo": "Calculadora",
        "arquivo": "calculadora.py",
        "nivel": "Iniciante",
        "categoria": "Operações",
        "objetivo": "Criar um menu de opções e executar operações matemáticas.",
        "explicacao": "Esse exercício é clássico. O aluno aprende a usar menu de opções, validar entrada e aplicar operações matemáticas básicas."
    },
    "14": {
        "titulo": "Par ou ímpar",
        "arquivo": "par_ou_impar.py",
        "nivel": "Intermediário",
        "categoria": "Jogo",
        "objetivo": "Usar módulo e aleatoriedade para verificar paridade.",
        "explicacao": "Aqui é demonstrado como usar aleatoriedade e módulo para verificar paridade, além de criar um jogo simples contra o computador."
    },
    "15": {
        "titulo": "Lista de tarefas",
        "arquivo": "lista_tarefas.py",
        "nivel": "Intermediário",
        "categoria": "Organização",
        "objetivo": "Adicionar, listar e remover itens de uma lista.",
        "explicacao": "Este exercício ensina a manipular listas para adicionar, listar e remover itens. É uma boa base para construir aplicativos mais completos no futuro."
    },
}


def mostrar_pontos_chave(nome_arquivo):
    if "imc" in nome_arquivo or "media" in nome_arquivo or "notas" in nome_arquivo:
        return [
            "Entrada de dados do usuário",
            "Cálculos com números",
            "Estruturas condicionais",
            "Saída final para o aluno",
        ]
    if "loteria" in nome_arquivo or "adivinhacao" in nome_arquivo or "par" in nome_arquivo:
        return [
            "Números aleatórios",
            "Comparação de valores",
            "Laços de repetição",
            "Decisões para vencer ou perder",
        ]
    if "agenda" in nome_arquivo or "estoque" in nome_arquivo or "biblioteca" in nome_arquivo or "tarefas" in nome_arquivo:
        return [
            "Listas e dicionários",
            "Menu interativo",
            "Cadastro e busca de dados",
            "Organização do sistema",
        ]
    if "funcao" in nome_arquivo or "boas" in nome_arquivo or "operacoes" in nome_arquivo or "tipos" in nome_arquivo:
        return [
            "Variáveis",
            "Funções",
            "Operadores matemáticos",
            "Tipos de dados",
        ]
    if "bancario" in nome_arquivo or "calculadora" in nome_arquivo:
        return [
            "Menu do usuário",
            "Validação de entradas",
            "Operações matemáticas",
            "Controle de fluxo",
        ]
    return [
        "Entrada de dados",
        "Processamento",
        "Estrutura condicional",
        "Saída ao usuário",
    ]


def descricao_linha(linha):
    texto = linha.strip()
    if not texto or texto.startswith("#"):
        return "Comentário ou estrutura auxiliar do código."
    if "input(" in texto:
        return "Recebe uma entrada do usuário e guarda em uma variável."
    if "print(" in texto:
        return "Exibe uma mensagem ou resultado para o aluno ou usuário."
    if "if " in texto:
        return "Cria uma condição: se a expressão for verdadeira, executa um bloco."
    if "for " in texto:
        return "Repete uma ação várias vezes, geralmente para percorrer itens ou números."
    if "while " in texto:
        return "Executa um bloco repetidamente enquanto a condição continuar verdadeira."
    if "def " in texto:
        return "Define uma função, criando um bloco reutilizável de código."
    if "random" in texto:
        return "Usa aleatoriedade para gerar números ou escolhas imprevisíveis."
    if "append(" in texto or "remove(" in texto:
        return "Altera a lista, adicionando ou removendo itens."
    if "sorted(" in texto or "len(" in texto:
        return "Organiza ou calcula informações para analisar o resultado."
    if "=" in texto:
        return "Armazena um valor em uma variável para ser usado depois."
    return "Parte importante da lógica do programa que ajuda a resolver o problema."


def mostrar_aula_professor(info):
    caminho = Path(__file__).with_name(info["arquivo"])
    linhas = caminho.read_text(encoding="utf-8").splitlines()

    print(f"\n=== {info['titulo']} ===")
    print("\nResumo da aula:")
    print(f"- Nível: {info['nivel']}")
    print(f"- Categoria: {info['categoria']}")
    print(f"- Objetivo: {info['objetivo']}")
    print(f"- Contexto: {info['explicacao']}")

    print("\nObjetivo didático do professor:")
    print("1. Explicar o problema antes do código.")
    print("2. Mostrar o que entra, o que processa e o que sai.")
    print("3. Destacar as ideias principais de programação envolvidas.")
    print("4. Pedir que o aluno tente prever a resposta antes de executar.")

    print("\nConceitos trabalhados:")
    for item in mostrar_pontos_chave(info["arquivo"]):
        print(f"- {item}")

    print("\nCódigo com explicação:")
    print("-" * 80)
    for numero, linha in enumerate(linhas, start=1):
        print(f"{numero:02d} | {linha}")
    print("-" * 80)

    print("\nExplicação linha a linha:")
    for numero, linha in enumerate(linhas, start=1):
        if not linha.strip():
            continue
        print(f"{numero:02d} - {descricao_linha(linha)}")

    print("\nRoteiro de apresentação para a aula:")
    print("- Primeiro, leia o enunciado em voz alta.")
    print("- Depois, explique quais entradas o programa precisa receber.")
    print("- Em seguida, mostre o processamento e a lógica principal.")
    print("- Finalize mostrando a saída esperada e comparando com a execução real.")
    print("- Pergunte ao aluno: 'Por que esse trecho foi usado aqui?'")

    print("\nDesafio para o aluno:")
    print("1. Qual é a entrada do programa?")
    print("2. Qual parte do código decide o resultado?")
    print("3. O que acontece se o usuário digitar um valor inesperado?")
    print("4. Como você melhoraria este programa?")


def mostrar_guia_professor():
    while True:
        try:
            print("\n" + "═" * 80)
            print("                 MODO PROFESSOR")
            print("═" * 80)
            print("Escolha um exercício para aprender passo a passo:\n")

            for codigo, info in LISTA.items():
                print(f"[{codigo}] {info['titulo']}  ({info['nivel']})")
            print("[0] Voltar")
            print("─" * 80)

            escolha = input("\nSua escolha: ").strip()
        except EOFError:
            print("\nEntrada encerrada. Voltando ao menu principal...")
            break

        if escolha == "0":
            print("Voltando ao menu principal...")
            break

        if escolha not in LISTA:
            print("Opção inválida.")
            continue

        mostrar_aula_professor(LISTA[escolha])

        try:
            input("\nPressione Enter para continuar no mesmo menu do professor...")
        except EOFError:
            print("\nEntrada encerrada. Voltando ao menu principal...")
            break
