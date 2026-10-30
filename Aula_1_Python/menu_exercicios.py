import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from modo_professor import mostrar_guia_professor
from curso_guiado import iniciar_curso_guiado


EXERCICIOS_1 = {
    "1": "boas_vindas.py",
    "2": "calculo_imc.py",
    "3": "media_numeros.py",
    "4": "funcao_simples.py",
    "5": "operacoes_matematicas.py",
    "6": "tipos_dados.py",
    "7": "bibliotecas_basicas.py",
}

EXERCICIOS_POR_NIVEL = {
    "iniciante": [
        {"titulo": "Boas-vindas", "arquivo": "boas_vindas.py", "objetivo": "Entender entrada e saída básica."},
        {"titulo": "Cálculo do IMC", "arquivo": "calculo_imc.py", "objetivo": "Trabalhar com variáveis e cálculo."},
        {"titulo": "Média de números", "arquivo": "media_numeros.py", "objetivo": "Somar e dividir valores."},
        {"titulo": "Função simples", "arquivo": "funcao_simples.py", "objetivo": "Entender funções e reutilização."},
        {"titulo": "Operações matemáticas", "arquivo": "operacoes_matematicas.py", "objetivo": "Praticar operadores e lógica."},
        {"titulo": "Tipos de dados", "arquivo": "tipos_dados.py", "objetivo": "Diferenciar textos, números e booleanos."},
        {"titulo": "Bibliotecas básicas", "arquivo": "bibliotecas_basicas.py", "objetivo": "Usar módulos do Python."},
        {"titulo": "Conversor de temperatura", "arquivo": "conversor_temperatura.py", "objetivo": "Aplicar fórmulas em programas reais."},
        {"titulo": "Média de notas", "arquivo": "media_notas.py", "objetivo": "Usar laços e condicionais na prática."},
        {"titulo": "Calculadora", "arquivo": "calculadora.py", "objetivo": "Organizar um menu e calcular operações."},
    ],
    "intermediario": [
        {"titulo": "Sistema de notas da turma", "arquivo": "sistema_notas_turma.py", "objetivo": "Validar notas, médias e aprovação."},
        {"titulo": "Jogo da adivinhação", "arquivo": "jogo_adivinhacao.py", "objetivo": "Combinar aleatoriedade e lógica."},
        {"titulo": "Cadastro de alunos", "arquivo": "cadastro_alunos.py", "objetivo": "Usar dicionários e cadastro de dados."},
        {"titulo": "Agenda de contatos", "arquivo": "agenda_contatos.py", "objetivo": "Gerenciar registros em memória."},
        {"titulo": "Controle de estoque", "arquivo": "controle_estoque.py", "objetivo": "Gerenciar quantidades e preços."},
        {"titulo": "Sistema bancário", "arquivo": "sistema_bancario.py", "objetivo": "Simular fluxo bancário com regras."},
        {"titulo": "Biblioteca", "arquivo": "biblioteca.py", "objetivo": "Organizar registros e busca de itens."},
        {"titulo": "Par ou ímpar", "arquivo": "par_ou_impar.py", "objetivo": "Usar módulo e cálculo lógico."},
        {"titulo": "Lista de tarefas", "arquivo": "lista_tarefas.py", "objetivo": "Manipular listas com ações do usuário."},
        {"titulo": "Loteria", "arquivo": "loteria.py", "objetivo": "Comparar apostas com sorteio e detectar acertos."},
    ],
    "avancado": [
        {"titulo": "Jogo da forca", "arquivo": "jogo_forca.py", "objetivo": "Integrar lógica, listas e fluxo complexos."},
    ],
}

EXERCICIOS_MENU = {
    "1": "Boas-vindas / IMC / Média / Funções",
    "2": "Sistema de notas da turma",
    "3": "Loteria",
    "4": "Conversor de temperatura",
    "5": "Média de notas",
    "6": "Jogo da adivinhação",
    "7": "Cadastro de alunos",
    "8": "Agenda de contatos",
    "9": "Controle de estoque",
    "10": "Sistema bancário",
    "11": "Jogo da forca",
    "12": "Biblioteca",
    "13": "Calculadora",
    "14": "Par ou ímpar",
    "15": "Lista de tarefas",
    "16": "Modo professor",
    "17": "Trilha por nível",
    "18": "Progresso do aluno",
    "19": "Curso em sequência",
    "20": "Próximo desafio",
    "21": "Curso guiado por desafios",
}

SEQUENCIA_CURSO = [
    {
        "etapa": 1,
        "titulo": "Fundamentos da lógica",
        "objetivo": "Entender entrada, saída, variáveis e operadores.",
        "arquivos": ["boas_vindas.py", "calculo_imc.py", "media_numeros.py", "funcao_simples.py", "operacoes_matematicas.py", "tipos_dados.py", "bibliotecas_basicas.py"],
    },
    {
        "etapa": 2,
        "titulo": "Estruturas de decisão e repetição",
        "objetivo": "Aplicar condicionais, laços e organização de dados.",
        "arquivos": ["sistema_notas_turma.py", "conversor_temperatura.py", "media_notas.py", "calculadora.py"],
    },
    {
        "etapa": 3,
        "titulo": "Projetos interativos e jogos",
        "objetivo": "Combinar lógica com experiências reais e desafios divertidos.",
        "arquivos": ["jogo_adivinhacao.py", "loteria.py", "par_ou_impar.py", "jogo_forca.py"],
    },
    {
        "etapa": 4,
        "titulo": "Sistemas e organização de dados",
        "objetivo": "Trabalhar com cadastro, agenda, estoque e gerenciamento.",
        "arquivos": ["cadastro_alunos.py", "agenda_contatos.py", "controle_estoque.py", "biblioteca.py", "lista_tarefas.py"],
    },
    {
        "etapa": 5,
        "titulo": "Aplicações do mundo real",
        "objetivo": "Simular operações de banco e sistemas mais completos.",
        "arquivos": ["sistema_bancario.py"],
    },
]


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def borda(texto, cor="\033[96m"):
    linha = "=" * 80
    print(f"\033[1;92m{linha}\033[0m")
    print(f"\033[1;97m{cor}{texto}\033[0m")
    print(f"\033[1;92m{linha}\033[0m")


def print_menu_header():
    print("\033[1;96m" + "═" * 80 + "\033[0m")
    print("\033[1;92m         ESCOLA DE PROGRAMAÇÃO - TRILHA PYTHON\033[0m")
    print("\033[1;96m" + "═" * 80 + "\033[0m")
    print("\033[1;93mSeus atalhos rápidos:\033[0m")
    print("\033[1;93m[ P ]\033[0m Modo professor   \033[1;93m[ N ]\033[0m Trilha por nível   \033[1;93m[ G ]\033[0m Progresso   \033[1;93m[ C ]\033[0m Curso   \033[1;93m[ A ]\033[0m Aula guiada")
    print("\033[1;96m" + "─" * 80 + "\033[0m")


def executar_arquivo(nome_arquivo):
    caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
    subprocess.run([sys.executable, caminho], check=False)


def listar_exercicios_por_nivel(nivel):
    chave = (nivel or "").strip().lower()
    return list(EXERCICIOS_POR_NIVEL.get(chave, []))


def registrar_progresso(arquivo_exercicio, arquivo="progresso_exercicios.json"):
    caminho = Path(arquivo)
    if not caminho.is_absolute():
        caminho = Path(__file__).with_name(arquivo)

    dados = {"concluidos": [], "ultimo": None, "atualizado_em": None}

    if caminho.exists():
        try:
            with caminho.open("r", encoding="utf-8") as handle:
                dados = json.load(handle)
        except json.JSONDecodeError:
            dados = {"concluidos": [], "ultimo": None, "atualizado_em": None}

    concluidos = dados.setdefault("concluidos", [])
    if arquivo_exercicio not in concluidos:
        concluidos.append(arquivo_exercicio)

    dados["ultimo"] = arquivo_exercicio
    dados["atualizado_em"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with caminho.open("w", encoding="utf-8") as handle:
        json.dump(dados, handle, ensure_ascii=False, indent=2)

    return True


def mostrar_progresso():
    caminho = Path(__file__).with_name("progresso_exercicios.json")
    if not caminho.exists():
        print("\n\033[1;93mNenhum progresso registrado ainda.\033[0m")
        return

    try:
        with caminho.open("r", encoding="utf-8") as handle:
            dados = json.load(handle)
    except json.JSONDecodeError:
        print("\n\033[1;91mArquivo de progresso corrompido.\033[0m")
        return

    concluidos = dados.get("concluidos", [])
    ultimo = dados.get("ultimo")
    atualizado = dados.get("atualizado_em", "Nunca")

    print("\n=== PROGRESSO DO ALUNO ===")
    print(f"Último exercício: {ultimo or 'Nenhum'}")
    print(f"Atualizado em: {atualizado}")
    print(f"Total concluído: {len(concluidos)}")
    if concluidos:
        for item in concluidos:
            print(f"- {item}")


def ler_progresso():
    caminho = Path(__file__).with_name("progresso_exercicios.json")
    if not caminho.exists():
        return []

    try:
        with caminho.open("r", encoding="utf-8") as handle:
            dados = json.load(handle)
    except json.JSONDecodeError:
        return []

    return dados.get("concluidos", [])


def mostrar_curso():
    concluidos = set(ler_progresso())
    print("\n" + "═" * 80)
    print("                     CURSO EM SEQUÊNCIA")
    print("═" * 80)
    print("Acompanhe a ordem sugerida para aprender de forma progressiva.\n")

    for etapa in SEQUENCIA_CURSO:
        status = "✅" if all(arquivo in concluidos for arquivo in etapa["arquivos"]) else "📘"
        print(f"{status} Etapa {etapa['etapa']}: {etapa['titulo']}")
        print(f"    Objetivo: {etapa['objetivo']}")
        print(f"    Exercícios: {', '.join(etapa['arquivos'])}")
        print()

    print("Dica: resolva a etapa atual e depois avance para a próxima sem pular conceitos.")
    print("═" * 80)


def mostrar_proximo_desafio():
    concluidos = set(ler_progresso())
    recomendados = []

    for etapa in SEQUENCIA_CURSO:
        for arquivo in etapa["arquivos"]:
            if arquivo not in concluidos:
                recomendados.append(arquivo)
                break
        if recomendados:
            break

    if not recomendados:
        print("\n\033[1;92mVocê já concluiu toda a trilha. Parabéns!\033[0m")
        return

    arquivo = recomendados[0]
    print("\n" + "═" * 80)
    print("                 PRÓXIMO DESAFIO")
    print("═" * 80)
    print(f"Recomendação: {arquivo}")
    print("Desafio: tente resolver esse exercício sem olhar a resposta completa.")
    print("Depois, revise o conceito com o modo professor e explique o programa em voz alta.")
    print("═" * 80)


def menu_exercicio_1():
    while True:
        limpar_tela()
        borda("EXERCÍCIO 1 - FUNDAMENTOS", "\033[1;96m")
        print("\033[1;93m[1]\033[0m Boas-vindas")
        print("\033[1;93m[2]\033[0m Cálculo do IMC")
        print("\033[1;93m[3]\033[0m Média de números")
        print("\033[1;93m[4]\033[0m Função simples")
        print("\033[1;93m[5]\033[0m Operações matemáticas")
        print("\033[1;93m[6]\033[0m Tipos de dados")
        print("\033[1;93m[7]\033[0m Bibliotecas básicas")
        print("\033[1;91m[0]\033[0m Voltar")

        try:
            opcao = input("\033[1;92mEscolha uma parte: \033[0m").strip()
        except EOFError:
            print("\n\033[1;91mEntrada encerrada. Voltando...\033[0m")
            break

        if opcao == "0":
            break
        if opcao in EXERCICIOS_1:
            executar_arquivo(EXERCICIOS_1[opcao])
            registrar_progresso(EXERCICIOS_1[opcao])
        else:
            print("\n\033[1;91mOpção inválida!\033[0m")

        continue


def menu_trilha_por_nivel():
    niveis = [
        ("1", "iniciante"),
        ("2", "intermediario"),
        ("3", "avancado"),
    ]

    while True:
        limpar_tela()
        print("\033[1;96m" + "═" * 80 + "\033[0m")
        print("\033[1;92m                 TRILHA DE APRENDIZAGEM\033[0m")
        print("\033[1;96m" + "═" * 80 + "\033[0m")
        print("\033[1;93m[1]\033[0m Iniciante")
        print("\033[1;93m[2]\033[0m Intermediário")
        print("\033[1;93m[3]\033[0m Avançado")
        print("\033[1;91m[0]\033[0m Voltar")
        print("\033[1;96m" + "─" * 80 + "\033[0m")

        try:
            opcao = input("\033[1;92mEscolha o nível: \033[0m").strip()
        except EOFError:
            print("\n\033[1;91mEntrada encerrada. Voltando...\033[0m")
            break

        if opcao == "0":
            break

        nivel = next((nome for codigo, nome in niveis if codigo == opcao), None)
        if not nivel:
            print("\n\033[1;91mNivel inválido!\033[0m")
            continue

        itens = listar_exercicios_por_nivel(nivel)
        print(f"\n=== {nivel.upper()} ===")
        for indice, item in enumerate(itens, start=1):
            print(f"[{indice}] {item['titulo']} - {item['objetivo']}")

        try:
            input("\n\033[1;90mPressione Enter para continuar no mesmo menu...\033[0m")
        except EOFError:
            print("\n\033[1;91mEntrada encerrada. Voltando...\033[0m")
            break


def abrir_exercicio_por_codigo(codigo):
    mapa = {
        "1": "boas_vindas.py",
        "2": "sistema_notas_turma.py",
        "3": "loteria.py",
        "4": "conversor_temperatura.py",
        "5": "media_notas.py",
        "6": "jogo_adivinhacao.py",
        "7": "cadastro_alunos.py",
        "8": "agenda_contatos.py",
        "9": "controle_estoque.py",
        "10": "sistema_bancario.py",
        "11": "jogo_forca.py",
        "12": "biblioteca.py",
        "13": "calculadora.py",
        "14": "par_ou_impar.py",
        "15": "lista_tarefas.py",
    }
    arquivo = mapa.get(codigo)
    if arquivo:
        executar_arquivo(arquivo)
        registrar_progresso(arquivo)
    else:
        print("\n\033[1;91mCódigo inválido!\033[0m")


def aguardar_enter(mensagem="Pressione Enter para voltar..."):
    try:
        input(f"\n{mensagem}")
        return True
    except EOFError:
        return False


def mostrar_como_usar():
    limpar_tela()
    borda("GUIA RÁPIDO DE USO", "\033[1;96m")
    print("\nSiga este caminho para aprender:")
    print("1. Curso guiado: estude um conceito, veja um exemplo e resolva o desafio.")
    print("2. Exercícios práticos: escolha um programa pronto para executar e explorar.")
    print("3. Aulas explicativas: selecione um exercício para ver sua explicação completa.")
    print("4. Trilhas de aprendizagem: consulte os níveis, a ordem do curso e a próxima sugestão.")
    print("5. Meu progresso: veja os exercícios que já abriu.")
    print("\nEncontros da apostila dentro do curso guiado:")
    print("- Encontro 1: traduza os fundamentos de Portugol para Python.")
    print("- Encontro 2: construa a Central com funções, validações e menu.")
    print("- Encontro 3: pratique textos, listas, matrizes, dicionários, módulos e arquivos.")
    print("\nDurante o curso guiado:")
    print("- Leia a aula rápida antes de começar cada desafio.")
    print("- Digite sua resposta em Python; respostas erradas podem ser tentadas novamente.")
    print("- Digite /dica para receber uma pista ou /sair para pausar e continuar depois.")
    print("- O curso salva automaticamente os desafios concluídos.")
    print("- No encontro 3, use o depurador do VS Code: ponto de parada e F10 para avançar linha a linha.")
    print("\nDica: comece pelo curso guiado se esta for sua primeira visita.")
    aguardar_enter()


def menu_exercicios_praticos():
    while True:
        limpar_tela()
        borda("EXERCÍCIOS PRÁTICOS", "\033[1;96m")
        print("\nEscolha um programa para executar:")
        print("[1] Fundamentos iniciais")
        nomes = {
            "2": "Sistema de notas da turma",
            "3": "Loteria",
            "4": "Conversor de temperatura",
            "5": "Média de notas",
            "6": "Jogo da adivinhação",
            "7": "Cadastro de alunos",
            "8": "Agenda de contatos",
            "9": "Controle de estoque",
            "10": "Sistema bancário",
            "11": "Jogo da forca",
            "12": "Biblioteca",
            "13": "Calculadora",
            "14": "Par ou ímpar",
            "15": "Lista de tarefas",
        }
        for codigo, nome in nomes.items():
            print(f"[{codigo}] {nome}")
        print("[0] Voltar")

        try:
            opcao = input("\nNúmero do exercício: ").strip()
        except EOFError:
            return

        if opcao == "0":
            return
        if opcao == "1":
            menu_exercicio_1()
        elif opcao in nomes:
            abrir_exercicio_por_codigo(opcao)
            aguardar_enter()
        else:
            print("Opção inválida.")
            aguardar_enter()


def menu_trilhas_e_aulas():
    while True:
        limpar_tela()
        borda("TRILHAS E AULAS", "\033[1;96m")
        print("\n[1] Aulas explicativas por exercício")
        print("[2] Ver exercícios por nível")
        print("[3] Ver curso em sequência")
        print("[4] Ver próximo exercício recomendado")
        print("[0] Voltar")
        try:
            opcao = input("\nEscolha uma opção: ").strip()
        except EOFError:
            return

        if opcao == "0":
            return
        if opcao == "1":
            mostrar_guia_professor()
        elif opcao == "2":
            menu_trilha_por_nivel()
        elif opcao == "3":
            mostrar_curso()
            aguardar_enter()
        elif opcao == "4":
            mostrar_proximo_desafio()
            aguardar_enter()
        else:
            print("Opção inválida.")
            aguardar_enter()


def menu_principal():
    if os.name == "nt":
        os.system("color")

    while True:
        limpar_tela()
        borda("ESCOLA DE PROGRAMAÇÃO | PYTHON", "\033[1;96m")
        print("\nEscolha o que deseja fazer:")
        print("[1] Começar / continuar o curso guiado")
        print("[2] Exercícios práticos")
        print("[3] Trilhas e aulas explicativas")
        print("[4] Meu progresso")
        print("[5] Como usar o programa")
        print("[0] Sair")

        try:
            opcao = input("\nSua escolha: ").strip()
        except EOFError:
            print("\n\033[1;91mEntrada encerrada. Saindo...\033[0m")
            break

        if opcao == "1":
            iniciar_curso_guiado()
        elif opcao == "2":
            menu_exercicios_praticos()
        elif opcao == "3":
            menu_trilhas_e_aulas()
        elif opcao == "4":
            mostrar_progresso()
            aguardar_enter()
        elif opcao == "5":
            mostrar_como_usar()
        elif opcao == "0":
            print("\n\033[1;92mAté a próxima!\033[0m")
            break
        else:
            print("\n\033[1;91mOpção inválida!\033[0m")

        continue


if __name__ == "__main__":
    menu_principal()
