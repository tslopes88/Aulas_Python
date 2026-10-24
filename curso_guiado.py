import json
from pathlib import Path


PROGRESSO_ARQUIVO = Path(__file__).with_name("progresso_curso_guiado.json")

NIVEIS = [
    {
        "nome": "Fundamentos",
        "desafios": [
            {
                "id": "fundamentos-01",
                "instrucao": "Escreva uma linha que mostre a mensagem Ola, mundo! na tela.",
                "respostas": ['print("Ola, mundo!")', "print('Ola, mundo!')"],
                "dica": "Use print() e coloque a mensagem entre aspas.",
                "explicacao": "A funcao print() exibe na tela o valor que recebe.",
            },
            {
                "id": "fundamentos-02",
                "instrucao": "Guarde o nome digitado pelo usuario na variavel nome.",
                "respostas": ['nome = input("Qual e seu nome? ")', "nome = input()"],
                "dica": "A funcao input() recebe texto. Use nome = input(...).",
                "explicacao": "input() recebe texto do teclado, e o sinal = guarda esse valor na variavel nome.",
            },
            {
                "id": "fundamentos-03",
                "instrucao": "Escreva uma linha para mostrar o conteudo da variavel nome.",
                "respostas": ["print(nome)"],
                "dica": "Passe o nome da variavel para print(), sem aspas.",
                "explicacao": "Sem aspas, nome representa o valor guardado na variavel; com aspas seria apenas um texto literal.",
            },
            {
                "id": "fundamentos-04",
                "instrucao": "Receba a idade digitada e transforme o texto em um numero inteiro, guardando em idade.",
                "respostas": ['idade = int(input("Sua idade: "))', "idade = int(input())"],
                "dica": "Combine int() com input() para converter o texto digitado em numero.",
                "explicacao": "input() retorna texto; int() converte esse texto para um numero inteiro.",
            },
            {
                "id": "fundamentos-05",
                "instrucao": "Calcule 8 + 5 e guarde o resultado na variavel total.",
                "respostas": ["total = 8 + 5"],
                "dica": "Use o operador + a direita do sinal =.",
                "explicacao": "A expressao a direita e calculada primeiro, e o resultado e armazenado em total.",
            },
        ],
    },
    {
        "nome": "Decisoes e repeticao",
        "desafios": [
            {
                "id": "logica-01",
                "instrucao": "Escreva a condicao que verifica se idade e maior ou igual a 18.",
                "respostas": ["idade >= 18"],
                "dica": "O operador >= significa maior ou igual.",
                "explicacao": "A comparacao produz True ou False e pode ser usada dentro de um if.",
            },
            {
                "id": "logica-02",
                "instrucao": "Escreva uma condicao que verifica se numero e par.",
                "respostas": ["numero % 2 == 0"],
                "dica": "O operador % calcula o resto da divisao; numeros pares deixam resto zero ao dividir por 2.",
                "explicacao": "== compara valores, enquanto % 2 obtem o resto da divisao por dois.",
            },
            {
                "id": "logica-03",
                "instrucao": "Escreva um for que percorra os numeros de 1 ate 5, incluindo o 5.",
                "respostas": ["for numero in range(1, 6):"],
                "dica": "O limite final de range() nao e incluido, entao use 6.",
                "explicacao": "range(1, 6) gera 1, 2, 3, 4 e 5; o dois-pontos inicia o bloco repetido.",
            },
            {
                "id": "logica-04",
                "instrucao": "Adicione o texto Estudar a lista chamada tarefas.",
                "respostas": ['tarefas.append("Estudar")', "tarefas.append('Estudar')"],
                "dica": "Use o metodo append() da lista.",
                "explicacao": "append() adiciona um novo item ao final de uma lista.",
            },
            {
                "id": "logica-05",
                "instrucao": "Defina uma funcao chamada dobro que receba um parametro chamado numero.",
                "respostas": ["def dobro(numero):"],
                "dica": "Uma funcao comeca com def, seguido do nome, dos parametros entre parenteses e de dois-pontos.",
                "explicacao": "A definicao cria uma funcao reutilizavel; o corpo dela sera escrito na linha seguinte, com indentacao.",
            },
        ],
    },
    {
        "nome": "Projetos e dados",
        "desafios": [
            {
                "id": "projetos-01",
                "instrucao": "Dentro da funcao dobro, devolva o valor de numero multiplicado por 2.",
                "respostas": ["return numero * 2", "return 2 * numero"],
                "dica": "Use return para devolver o resultado da multiplicacao.",
                "explicacao": "return encerra a chamada da funcao e entrega o resultado para quem a chamou.",
            },
            {
                "id": "projetos-02",
                "instrucao": "Crie um dicionario aluno com nome Ana e media 8.5.",
                "respostas": ['aluno = {"nome": "Ana", "media": 8.5}', "aluno = {'nome': 'Ana', 'media': 8.5}"],
                "dica": "Dicionarios usam chaves e valores separados por dois-pontos, dentro de chaves {}.",
                "explicacao": "O dicionario associa a chave nome ao texto Ana e a chave media ao numero 8.5.",
            },
            {
                "id": "projetos-03",
                "instrucao": "Crie uma lista pares com os numeros pares encontrados em numeros.",
                "respostas": ["pares = [numero for numero in numeros if numero % 2 == 0]"],
                "dica": "Na compreensao de lista, coloque o for antes do if e filtre com resto igual a zero.",
                "explicacao": "A compreensao percorre numeros e inclui em pares somente valores divisiveis por 2.",
            },
            {
                "id": "projetos-04",
                "instrucao": "Escreva a condicao que permite um saque apenas quando saldo e suficiente para saque.",
                "respostas": ["if saldo >= saque:"],
                "dica": "Compare saldo com saque usando maior ou igual; uma condicao if termina com dois-pontos.",
                "explicacao": "A comparacao impede que o saque seja autorizado quando o saldo e menor que o valor solicitado.",
            },
            {
                "id": "projetos-05",
                "instrucao": "Escreva uma linha que tente converter texto para inteiro e capture um valor invalido.",
                "respostas": ["except ValueError:"],
                "dica": "O erro de conversao de texto para inteiro e ValueError; use a palavra-chave except.",
                "explicacao": "Um bloco except ValueError: permite tratar entradas que nao podem ser convertidas para inteiro.",
            },
        ],
    },
    {
        "nome": "Desafios avançados",
        "desafios": [
            {
                "id": "avancado-01",
                "instrucao": "Calcule a média dos valores da lista notas e guarde em media.",
                "respostas": ["media = sum(notas) / len(notas)"],
                "dica": "Use sum() para somar os valores e len() para contar quantos existem.",
                "explicacao": "A média é a soma dos valores dividida pela quantidade de valores.",
            },
            {
                "id": "avancado-02",
                "instrucao": "Filtre em aprovados os dicionários da lista alunos cuja média seja pelo menos 7.",
                "respostas": [
                    'aprovados = [aluno for aluno in alunos if aluno["media"] >= 7]',
                    "aprovados = [aluno for aluno in alunos if aluno['media'] >= 7]",
                ],
                "dica": "Use uma compreensão de lista e consulte a chave media de cada aluno.",
                "explicacao": "A compreensão percorre os cadastros e mantém apenas os que atendem à condição de aprovação.",
            },
            {
                "id": "avancado-03",
                "instrucao": "Ordene a lista produtos pelo campo preco, do menor para o maior, e guarde em ordenados.",
                "respostas": ['ordenados = sorted(produtos, key=lambda produto: produto["preco"])', "ordenados = sorted(produtos, key=lambda produto: produto['preco'])"],
                "dica": "sorted() aceita key= para escolher o campo de cada dicionário usado na ordenação.",
                "explicacao": "A função lambda extrai o preço de cada produto e sorted() cria uma nova lista ordenada.",
            },
            {
                "id": "avancado-04",
                "instrucao": "Some um valor ao contador de uma chave, iniciando em zero se ela ainda não existir.",
                "respostas": ["contagem[chave] = contagem.get(chave, 0) + valor"],
                "dica": "O método get() aceita um valor padrão para chaves ausentes.",
                "explicacao": "get(chave, 0) evita erro quando a chave ainda não existe; depois o valor é acumulado.",
            },
            {
                "id": "avancado-05",
                "instrucao": "Escreva uma condição que rejeite um nome vazio ou composto apenas por espaços.",
                "respostas": ["if not nome.strip():"],
                "dica": "strip() remove espaços das pontas; not inverte o resultado lógico.",
                "explicacao": "Depois de remover espaços, uma string vazia é considerada falsa em uma condição.",
            },
            {
                "id": "avancado-06",
                "instrucao": "Percorra a lista tarefas com índice e valor usando enumerate().",
                "respostas": ["for indice, tarefa in enumerate(tarefas):"],
                "dica": "enumerate() entrega o índice e o item em cada repetição.",
                "explicacao": "Desempacotar o par retornado por enumerate() dá acesso ao número da posição e ao item.",
            },
            {
                "id": "avancado-07",
                "instrucao": "Abra dados.json para escrita com codificação UTF-8, usando a variável arquivo.",
                "respostas": ['with open("dados.json", "w", encoding="utf-8") as arquivo:', "with open('dados.json', 'w', encoding='utf-8') as arquivo:"],
                "dica": "Use with open(..., 'w', encoding='utf-8') as arquivo para gerenciar o arquivo com segurança.",
                "explicacao": "O bloco with fecha o arquivo automaticamente, inclusive quando ocorre um erro.",
            },
            {
                "id": "avancado-08",
                "instrucao": "Grave o objeto dados no arquivo aberto, preservando acentos e usando indentação de 2 espaços.",
                "respostas": ["json.dump(dados, arquivo, ensure_ascii=False, indent=2)"],
                "dica": "json.dump() recebe os dados e o arquivo; ensure_ascii=False mantém acentos legíveis.",
                "explicacao": "json.dump() serializa o objeto no arquivo, e indent=2 deixa o conteúdo organizado para leitura.",
            },
        ],
    },
]

AULAS_DESAFIOS = {
    "fundamentos-01": ("print() mostra informações na tela.", 'Exemplo: print("Bem-vindo")'),
    "fundamentos-02": ("input() pausa o programa e recebe o que a pessoa digitar como texto.", 'Exemplo: cidade = input("Sua cidade: ")'),
    "fundamentos-03": ("Uma variável guarda um valor. Use o nome sem aspas para acessar o valor guardado.", "Exemplo: print(cidade)"),
    "fundamentos-04": ("input() retorna texto. int() converte um texto numérico para inteiro.", 'Exemplo: quantidade = int(input("Quantidade: "))'),
    "fundamentos-05": ("O sinal = atribui um resultado a uma variável; + realiza uma soma.", "Exemplo: subtotal = 4 + 3"),
    "logica-01": ("Uma comparação cria uma condição verdadeira ou falsa. >= significa maior ou igual.", "Exemplo: temperatura >= 30"),
    "logica-02": ("O operador % retorna o resto da divisão. Um número par dividido por 2 tem resto zero.", "Exemplo: 10 % 2 resulta em 0"),
    "logica-03": ("for repete um bloco para cada item. range(início, limite) não inclui o limite final.", "Exemplo: range(2, 5) percorre 2, 3 e 4"),
    "logica-04": ("Listas guardam vários valores. append() acrescenta um item ao final.", 'Exemplo: compras.append("Pão")'),
    "logica-05": ("def cria uma função. Parâmetros entre parênteses recebem os dados usados por ela.", "Exemplo: def saudacao(nome):"),
    "projetos-01": ("return devolve um resultado da função para quem a chamou.", "Exemplo: return valor + 1"),
    "projetos-02": ("Dicionários organizam valores associados a chaves, como campos de um cadastro.", '{"produto": "Caderno", "preco": 12.5}'),
    "projetos-03": ("Uma compreensão de lista cria uma lista percorrendo itens e aplicando uma condição.", "Exemplo: [n for n in valores if n > 0]"),
    "projetos-04": ("Antes de alterar um saldo, compare o valor disponível com o valor solicitado.", "Exemplo: saldo >= valor_solicitado"),
    "projetos-05": ("try/except permite lidar com erros esperados sem encerrar o programa.", "Exemplo: except ValueError:"),
    "avancado-01": ("sum() soma os valores e len() conta os itens. Juntos permitem calcular médias.", "Exemplo: total = sum(valores)"),
    "avancado-02": ("Uma compreensão de lista pode filtrar registros usando uma condição sobre cada dicionário.", 'Exemplo: [item for item in itens if item["ativo"]]'),
    "avancado-03": ("sorted() recebe uma função key para ordenar registros por um campo específico.", 'Exemplo: sorted(livros, key=lambda livro: livro["titulo"])'),
    "avancado-04": ("dict.get(chave, padrão) consulta uma chave e fornece um valor quando ela ainda não existe.", "Exemplo: pontos.get(jogador, 0)"),
    "avancado-05": ("strip() remove espaços laterais. Strings vazias podem ser verificadas em condições.", 'Exemplo: if not entrada.strip():'),
    "avancado-06": ("enumerate() percorre uma sequência e fornece posição e conteúdo juntos.", "Exemplo: for indice, item in enumerate(lista):"),
    "avancado-07": ("with open() gerencia o ciclo de vida do arquivo e o fecha ao sair do bloco.", 'Exemplo: with open("arquivo.txt", "r", encoding="utf-8") as arquivo:'),
    "avancado-08": ("JSON transforma estruturas Python em texto para armazenamento e troca de dados.", "Exemplo: json.dump(dados, arquivo, indent=2)"),
}


def normalizar_resposta(resposta):
    return " ".join(resposta.strip().casefold().split())


def resposta_correta(resposta, desafio):
    resposta_normalizada = normalizar_resposta(resposta)
    return any(
        resposta_normalizada == normalizar_resposta(aceita)
        for aceita in desafio["respostas"]
    )


def carregar_progresso(caminho=PROGRESSO_ARQUIVO):
    try:
        with Path(caminho).open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except (OSError, json.JSONDecodeError):
        return set()
    return set(dados.get("concluidos", []))


def salvar_progresso(concluidos, caminho=PROGRESSO_ARQUIVO):
    destino = Path(caminho)
    with destino.open("w", encoding="utf-8") as arquivo:
        json.dump({"concluidos": sorted(concluidos)}, arquivo, ensure_ascii=False, indent=2)


def proximo_desafio(concluidos):
    for indice_nivel, nivel in enumerate(NIVEIS):
        for desafio in nivel["desafios"]:
            if desafio["id"] not in concluidos:
                return indice_nivel, desafio
    return None, None


def mostrar_aula_desafio(desafio):
    conceito, exemplo = AULAS_DESAFIOS[desafio["id"]]
    print("\nAULA RÁPIDA")
    print(f"Conceito: {conceito}")
    print(f"Exemplo:  {exemplo}")
    print("Entenda a ideia e depois aplique-a no desafio, sem copiar o exemplo literalmente.")


def iniciar_curso_guiado():
    concluidos = carregar_progresso()
    print("\n" + "=" * 72)
    print("CURSO GUIADO DE PYTHON")
    print("Escreva sua resposta em Python. Digite /dica para uma pista ou /sair para pausar.")

    while True:
        indice_nivel, desafio = proximo_desafio(concluidos)
        if desafio is None:
            print("\nParabéns! Você concluiu todos os níveis do curso guiado.")
            return

        nivel = NIVEIS[indice_nivel]
        total_nivel = len(nivel["desafios"])
        feitos_nivel = sum(item["id"] in concluidos for item in nivel["desafios"])
        print(f"\nNível {indice_nivel + 1}: {nivel['nome']} ({feitos_nivel}/{total_nivel})")
        mostrar_aula_desafio(desafio)
        try:
            input("\nPressione Enter quando estiver pronto para o desafio...")
        except EOFError:
            print("\nCurso pausado. Seu progresso foi mantido.")
            return
        print(f"Desafio {feitos_nivel + 1}: {desafio['instrucao']}")

        while True:
            try:
                resposta = input("\nSua resposta: ").strip()
            except EOFError:
                print("\nCurso pausado. Seu progresso foi mantido.")
                return

            comando = resposta.casefold()
            if comando == "/sair":
                print("Curso pausado. Seu progresso foi mantido.")
                return
            if comando == "/dica":
                print(f"Dica: {desafio['dica']}")
                continue
            if resposta_correta(resposta, desafio):
                concluidos.add(desafio["id"])
                salvar_progresso(concluidos)
                print(f"Correto! {desafio['explicacao']}")
                if feitos_nivel + 1 == total_nivel:
                    if indice_nivel + 1 < len(NIVEIS):
                        print(f"Nível concluído. Próximo nível desbloqueado: {NIVEIS[indice_nivel + 1]['nome']}.")
                    else:
                        print("Último nível concluído!")
                break
            print("Ainda não. Revise a instrução, ajuste o código e tente novamente. Digite /dica se precisar.")


if __name__ == "__main__":
    iniciar_curso_guiado()