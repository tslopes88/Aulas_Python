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
    {
        "nome": "Encontro 1: Portugol para Python",
        "objetivo": "Traduzir entrada, saída, variáveis, condições, repetições e listas do Portugol.",
        "roteiro": "Leia a explicação, observe o exemplo, diga em voz alta o que espera que aconteça, escreva a solução e compare o resultado. No VS Code, use quatro espaços de indentação e execute o arquivo pelo terminal.",
        "desafios": [
            {
                "id": "apostila-encontro1-01",
                "instrucao": "Mostre a variável nome dentro da frase Ola, nome! usando um f-string.",
                "respostas": ['print(f"Ola, {nome}!")', "print(f'Ola, {nome}!')"],
                "dica": "Coloque f antes das aspas e a variável entre chaves.",
                "explicacao": "O f-string substitui {nome} pelo conteúdo da variável durante a impressão.",
            },
            {
                "id": "apostila-encontro1-02",
                "instrucao": "Leia um peso decimal do teclado e converta a entrada para float.",
                "respostas": ['peso = float(input("Peso: "))', "peso = float(input())"],
                "dica": "input() retorna texto; envolva a chamada com float().",
                "explicacao": "float() converte a entrada textual em número decimal para permitir cálculos.",
            },
            {
                "id": "apostila-encontro1-03",
                "instrucao": "Converta a entrada de nota em float e aceite vírgula decimal trocando-a por ponto.",
                "respostas": ['nota = float(input("Nota: ").replace(",", "."))', 'nota = float(input().replace(",", "."))'],
                "dica": "Encadeie replace(',', '.') antes de chamar float().",
                "explicacao": "replace() adapta a vírgula decimal comum no Brasil ao formato aceito por float().",
            },
            {
                "id": "apostila-encontro1-04",
                "instrucao": "Escreva a condição Python que verifica se peso e altura são positivos.",
                "respostas": ["if peso > 0 and altura > 0:"],
                "dica": "Use and para exigir que as duas comparações sejam verdadeiras e finalize com dois-pontos.",
                "explicacao": "A condição composta só aceita os dados se peso e altura forem maiores que zero.",
            },
            {
                "id": "apostila-encontro1-05",
                "instrucao": "Percorra os índices de uma lista notas usando range e len.",
                "respostas": ["for i in range(len(notas)):"],
                "dica": "len(notas) informa quantas posições existem; range cria os índices começando em zero.",
                "explicacao": "range(len(notas)) percorre índices de zero até a última posição válida.",
            },
            {
                "id": "apostila-encontro1-06",
                "instrucao": "Adicione a variável nota ao final da lista notas.",
                "respostas": ["notas.append(nota)"],
                "dica": "Use append() para acrescentar um valor sem definir previamente o tamanho da lista.",
                "explicacao": "Listas Python crescem dinamicamente; append() inclui o novo valor no final.",
            },
        ],
    },
    {
        "nome": "Encontro 2: Central de Sistemas",
        "objetivo": "Montar funções reutilizáveis, validar entradas e organizar um menu que permanece aberto.",
        "roteiro": "Construa a Central por partes: primeiro a leitura segura, depois as funções de cada sistema e por fim o menu. Teste entradas válidas e inválidas; não avance enquanto não souber explicar por que cada função existe.",
        "desafios": [
            {
                "id": "apostila-encontro2-01",
                "instrucao": "Inicie um bloco para tentar converter um texto em número.",
                "respostas": ["try:"],
                "dica": "A palavra-chave que inicia o tratamento de erros é try, seguida de dois-pontos.",
                "explicacao": "O bloco try contém a operação que pode falhar, como uma conversão numérica.",
            },
            {
                "id": "apostila-encontro2-02",
                "instrucao": "Capture um erro de conversão numérica e mostre uma mensagem amigável.",
                "respostas": ["except ValueError:"],
                "dica": "Conversões inválidas com int() ou float() geram ValueError.",
                "explicacao": "except ValueError trata a entrada inválida e permite que o programa continue.",
            },
            {
                "id": "apostila-encontro2-03",
                "instrucao": "Defina ler_numero com mensagem e tipo opcional, cujo padrão é float.",
                "respostas": ["def ler_numero(mensagem, tipo=float):"],
                "dica": "Parâmetros com valor padrão usam nome=valor dentro dos parênteses.",
                "explicacao": "O parâmetro tipo permite reutilizar a função para converter para float ou int.",
            },
            {
                "id": "apostila-encontro2-04",
                "instrucao": "Dentro da função leitora, devolva o texto convertido pelo tipo recebido.",
                "respostas": ["return tipo(texto)"],
                "dica": "Chame o parâmetro tipo como uma função e devolva o resultado usando return.",
                "explicacao": "A função de conversão recebida no parâmetro transforma texto e retorna o número.",
            },
            {
                "id": "apostila-encontro2-05",
                "instrucao": "Inicie um menu que se repete até que opcao seja igual a zero.",
                "respostas": ["while opcao != 0:"],
                "dica": "Use while e o operador !=, que significa diferente.",
                "explicacao": "O menu continua repetindo enquanto a opção escolhida não for a opção de saída.",
            },
            {
                "id": "apostila-encontro2-06",
                "instrucao": "Escreva a condição que executa main apenas quando este arquivo é iniciado diretamente.",
                "respostas": ['if __name__ == "__main__":', "if __name__ == '__main__':"],
                "dica": "Compare a variável especial __name__ com a string __main__.",
                "explicacao": "Esse padrão permite importar funções sem iniciar automaticamente o menu do programa.",
            },
        ],
    },
    {
        "nome": "Encontro 3: Recursos do Python",
        "objetivo": "Conhecer ferramentas do Python para tratar textos e dados, usar módulos, salvar informações e depurar.",
        "roteiro": "Pratique um recurso de cada vez com dados pequenos. No depurador do VS Code, marque um ponto de parada e avance linha a linha com F10, observando como variáveis e listas mudam.",
        "desafios": [
            {
                "id": "apostila-encontro3-01",
                "instrucao": "Remova espaços das pontas do texto nome e guarde o resultado em nome_limpo.",
                "respostas": ["nome_limpo = nome.strip()"],
                "dica": "O método strip() remove espaços antes e depois do texto.",
                "explicacao": "Limpar espaços evita tratar entradas aparentemente vazias ou com espaços extras como diferentes.",
            },
            {
                "id": "apostila-encontro3-02",
                "instrucao": "Mostre o valor media com exatamente duas casas decimais usando f-string.",
                "respostas": ['print(f"{media:.2f}")', "print(f'{media:.2f}')"],
                "dica": "Dentro das chaves use dois-pontos seguido de .2f.",
                "explicacao": ".2f formata o número com duas casas depois do separador decimal.",
            },
            {
                "id": "apostila-encontro3-03",
                "instrucao": "Crie uma nova lista ranking com notas ordenadas da maior para a menor.",
                "respostas": ["ranking = sorted(notas, reverse=True)"],
                "dica": "sorted() cria uma lista ordenada; reverse=True inverte a ordem crescente padrão.",
                "explicacao": "A ordenação decrescente facilita montar um ranking sem implementar bubble sort.",
            },
            {
                "id": "apostila-encontro3-04",
                "instrucao": "Acesse a nota da linha 2 e coluna 3 da matriz notas usando índices Python.",
                "respostas": ["notas[1][2]"],
                "dica": "Python começa a contar índices em zero: subtraia um da linha e da coluna indicadas.",
                "explicacao": "Uma matriz é uma lista de listas; o primeiro índice seleciona a linha e o segundo, a coluna.",
            },
            {
                "id": "apostila-encontro3-05",
                "instrucao": "Percorra um dicionário notas recebendo nome e nota em cada repetição.",
                "respostas": ["for nome, nota in notas.items():"],
                "dica": "items() fornece cada par chave e valor; use dois nomes no for para desempacotá-lo.",
                "explicacao": "O laço visita cada aluno e sua nota sem precisar manter listas paralelas.",
            },
            {
                "id": "apostila-encontro3-06",
                "instrucao": "Percorra nomes e notas ao mesmo tempo usando zip().",
                "respostas": ["for nome, nota in zip(nomes, notas):"],
                "dica": "zip() combina os itens que ocupam a mesma posição nas duas listas.",
                "explicacao": "zip() permite percorrer listas relacionadas em conjunto, posição por posição.",
            },
            {
                "id": "apostila-encontro3-07",
                "instrucao": "Importe o módulo random para usar sorteios.",
                "respostas": ["import random"],
                "dica": "Módulos da biblioteca padrão são carregados com import seguido do nome.",
                "explicacao": "random oferece funções prontas de sorteio, como randint() e choice().",
            },
            {
                "id": "apostila-encontro3-08",
                "instrucao": "Sorteie um número inteiro entre 1 e 100 usando random.",
                "respostas": ["random.randint(1, 100)"],
                "dica": "A função randint recebe os limites mínimo e máximo, ambos incluídos.",
                "explicacao": "random.randint(1, 100) pode retornar qualquer inteiro entre 1 e 100, inclusive.",
            },
            {
                "id": "apostila-encontro3-09",
                "instrucao": "Abra notas.txt para escrita em UTF-8, associando o arquivo à variável arquivo.",
                "respostas": ['with open("notas.txt", "w", encoding="utf-8") as arquivo:', "with open('notas.txt', 'w', encoding='utf-8') as arquivo:"],
                "dica": "Use with open com modo w e encoding UTF-8.",
                "explicacao": "O modo w grava texto e with fecha o arquivo ao sair do bloco.",
            },
            {
                "id": "apostila-encontro3-10",
                "instrucao": "Escreva a variável nota no arquivo aberto e acrescente uma quebra de linha.",
                "respostas": ['arquivo.write(f"{nota}\\n")', "arquivo.write(str(nota) + \'\\n\')"],
                "dica": "Use o método write() e inclua o caractere de nova linha \\n dentro do texto.",
                "explicacao": "write() grava texto; cada nota fica em uma linha para poder ser lida depois.",
            },
            {
                "id": "apostila-encontro3-11",
                "instrucao": "Defina uma função calcula_media com parâmetro notas e valor padrão minimo igual a 6.0.",
                "respostas": ["def calcula_media(notas, minimo=6.0):"],
                "dica": "Combine uma função com um parâmetro opcional definido por um valor padrão.",
                "explicacao": "Valores padrão tornam a função flexível; quem chama pode aceitar a média mínima padrão ou substituí-la.",
            },
            {
                "id": "apostila-encontro3-12",
                "instrucao": "Devolva ao mesmo tempo a média e um booleano que informa se ela atingiu minimo.",
                "respostas": ["return media, media >= minimo"],
                "dica": "Separe os dois valores retornados por uma vírgula.",
                "explicacao": "Python permite retornar uma tupla, que pode ser desempacotada em duas variáveis.",
            },
            {
                "id": "apostila-encontro3-13",
                "instrucao": "Crie o texto limpo a partir de entrada removendo espaços das pontas e convertendo para minúsculas.",
                "respostas": ["limpo = entrada.strip().lower()"],
                "dica": "Encadeie strip() e lower() no texto antes de guardar o resultado.",
                "explicacao": "Métodos podem ser encadeados; normalizar texto ajuda a comparar entradas sem diferenças de espaços ou maiúsculas.",
            },
            {
                "id": "apostila-encontro3-14",
                "instrucao": "Separe o texto nome em palavras e guarde a lista em partes.",
                "respostas": ["partes = nome.split()"],
                "dica": "O método split() separa por espaços quando é chamado sem argumento.",
                "explicacao": "split() transforma uma frase em uma lista de palavras.",
            },
            {
                "id": "apostila-encontro3-15",
                "instrucao": "Guarde os cinco primeiros caracteres de texto em inicio.",
                "respostas": ["inicio = texto[0:5]", "inicio = texto[:5]"],
                "dica": "Fatiamento usa texto[início:fim], sem incluir a posição final.",
                "explicacao": "A fatia começa no índice zero e termina antes do índice cinco.",
            },
            {
                "id": "apostila-encontro3-16",
                "instrucao": "Verifique se a palavra Python aparece dentro da variável frase.",
                "respostas": ['"Python" in frase', "'Python' in frase"],
                "dica": "O operador in verifica se um texto está contido em outro.",
                "explicacao": "in retorna True se a palavra for encontrada e False caso contrário.",
            },
            {
                "id": "apostila-encontro3-17",
                "instrucao": "Insira a nota 10.0 no início da lista notas.",
                "respostas": ["notas.insert(0, 10.0)"],
                "dica": "insert() recebe primeiro a posição e depois o valor.",
                "explicacao": "insert(0, valor) coloca o item na primeira posição e desloca os outros.",
            },
            {
                "id": "apostila-encontro3-18",
                "instrucao": "Remova e guarde em ultima a última nota da lista notas.",
                "respostas": ["ultima = notas.pop()"],
                "dica": "pop() sem posição remove e devolve o último item.",
                "explicacao": "pop() altera a lista e retorna o item removido para que possa ser usado depois.",
            },
            {
                "id": "apostila-encontro3-19",
                "instrucao": "Importe a função mean do módulo statistics.",
                "respostas": ["from statistics import mean"],
                "dica": "Use from módulo import função para importar apenas o recurso necessário.",
                "explicacao": "statistics.mean calcula a média aritmética de uma sequência de números.",
            },
            {
                "id": "apostila-encontro3-20",
                "instrucao": "Calcule a média da lista notas usando a função mean importada.",
                "respostas": ["media = mean(notas)"],
                "dica": "Passe a lista de números para mean().",
                "explicacao": "A função retorna a média dos valores, evitando implementar a soma e a divisão manualmente.",
            },
            {
                "id": "apostila-encontro3-21",
                "instrucao": "Importe date do módulo datetime.",
                "respostas": ["from datetime import date"],
                "dica": "Use from datetime import date.",
                "explicacao": "datetime fornece tipos e ferramentas para trabalhar com datas e horários.",
            },
            {
                "id": "apostila-encontro3-22",
                "instrucao": "Leia todas as linhas de notas.txt em UTF-8 usando a variável arquivo.",
                "respostas": ['with open("notas.txt", "r", encoding="utf-8") as arquivo:', "with open('notas.txt', 'r', encoding='utf-8') as arquivo:"],
                "dica": "Use o modo r para leitura dentro de with open().",
                "explicacao": "O modo r lê um arquivo existente; o bloco with fecha o arquivo automaticamente.",
            },
            {
                "id": "apostila-encontro3-23",
                "instrucao": "Converta a linha de texto em um decimal e acrescente o valor à lista notas.",
                "respostas": ["notas.append(float(linha))"],
                "dica": "Converta com float() antes de usar append().",
                "explicacao": "O conteúdo lido de um arquivo é texto; a conversão permite reutilizar os dados em cálculos.",
            },
            {
                "id": "apostila-encontro3-24",
                "instrucao": "Importe o módulo math para usar funções matemáticas, como raiz quadrada.",
                "respostas": ["import math"],
                "dica": "math faz parte da biblioteca padrão e é carregado com import.",
                "explicacao": "O módulo math oferece funções e constantes matemáticas, como sqrt() e pi.",
            },
            {
                "id": "apostila-encontro3-25",
                "instrucao": "Mostre a data atual usando a classe date já importada de datetime.",
                "respostas": ["print(date.today())"],
                "dica": "Chame today() a partir de date e mostre o resultado com print().",
                "explicacao": "date.today() retorna a data local atual como um objeto de data.",
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
    "apostila-encontro1-01": ("f-strings inserem variáveis em textos usando chaves.", 'Exemplo: f"Bom dia, {nome}"'),
    "apostila-encontro1-02": ("input() sempre devolve texto; float() converte esse texto para decimal.", 'Exemplo: altura = float(input("Altura: "))'),
    "apostila-encontro1-03": ("replace() troca partes de um texto; pode normalizar vírgula decimal antes da conversão.", 'Exemplo: "7,5".replace(",", ".")'),
    "apostila-encontro1-04": ("and exige que duas condições sejam verdadeiras ao mesmo tempo.", "Exemplo: idade >= 18 and ativo"),
    "apostila-encontro1-05": ("range() cria índices inteiros e len() informa o tamanho da lista.", "Exemplo: range(len(cores)) percorre todas as posições"),
    "apostila-encontro1-06": ("Listas não precisam de tamanho fixo; append() adiciona valores conforme necessário.", 'Exemplo: nomes.append("Lia")'),
    "apostila-encontro2-01": ("try marca um bloco cuja execução pode gerar um erro esperado.", "Exemplo: try: valor = int(texto)"),
    "apostila-encontro2-02": ("except permite responder a um erro específico, como a conversão inválida ValueError.", "Exemplo: except ValueError:"),
    "apostila-encontro2-03": ("Parâmetros padrão permitem escolher uma conversão e ainda possibilitam substituí-la.", "Exemplo: def ler(mensagem, tipo=float):"),
    "apostila-encontro2-04": ("return pode chamar uma função recebida como parâmetro e entregar seu resultado.", "Exemplo: return conversor(texto)"),
    "apostila-encontro2-05": ("while repete o menu até a condição de saída ser verdadeira.", "Exemplo: while opcao != 0:"),
    "apostila-encontro2-06": ("__name__ == '__main__' diferencia execução direta de importação do módulo.", 'Exemplo: if __name__ == "__main__":"'),
    "apostila-encontro3-01": ("Métodos de texto são chamados depois do ponto e podem limpar entradas.", 'Exemplo: cidade.strip()'),
    "apostila-encontro3-02": ("A formatação .2f em f-strings mostra duas casas decimais.", 'Exemplo: f"{preco:.2f}"'),
    "apostila-encontro3-03": ("sorted() cria uma lista ordenada e reverse=True organiza do maior para o menor.", "Exemplo: sorted(valores, reverse=True)"),
    "apostila-encontro3-04": ("Listas começam no índice zero; matrizes são acessadas com dois índices.", "Exemplo: matriz[0][1] seleciona linha 1, coluna 2"),
    "apostila-encontro3-05": ("items() percorre pares de chave e valor de um dicionário.", "Exemplo: for chave, valor in dados.items():"),
    "apostila-encontro3-06": ("zip() percorre listas relacionadas juntando os valores de cada posição.", "Exemplo: zip(produtos, precos)"),
    "apostila-encontro3-07": ("import carrega módulos da biblioteca padrão sem instalação extra.", "Exemplo: import math"),
    "apostila-encontro3-08": ("random.randint() sorteia um inteiro incluindo os dois limites informados.", "Exemplo: random.randint(1, 6)"),
    "apostila-encontro3-09": ("with open() abre um arquivo e cuida do fechamento; UTF-8 preserva caracteres acentuados.", 'Exemplo: with open("dados.txt", "w", encoding="utf-8") as arquivo:'),
    "apostila-encontro3-10": ("write() grava texto; \\n representa uma quebra de linha dentro da string.", 'Exemplo: arquivo.write("linha\\n")'),
    "apostila-encontro3-11": ("Parâmetros padrão simplificam chamadas comuns e podem ser substituídos quando necessário.", "Exemplo: def aprovado(notas, minimo=6.0):"),
    "apostila-encontro3-12": ("Uma função pode retornar vários valores, que podem ser guardados em variáveis diferentes.", "Exemplo: return total, quantidade"),
    "apostila-encontro3-13": ("strip() remove espaços laterais e lower() padroniza o texto em minúsculas.", 'Exemplo: cidade.strip().lower()'),
    "apostila-encontro3-14": ("split() divide um texto em palavras e devolve uma lista.", 'Exemplo: "ola mundo".split()'),
    "apostila-encontro3-15": ("Fatiamento seleciona parte do texto; a posição final não entra no resultado.", 'Exemplo: codigo[:3] pega os três primeiros caracteres'),
    "apostila-encontro3-16": ("O operador in verifica se um trecho existe dentro de uma string ou lista.", 'Exemplo: "py" in linguagem'),
    "apostila-encontro3-17": ("insert(posicao, valor) insere um item em uma posição específica da lista.", "Exemplo: fila.insert(0, pessoa)"),
    "apostila-encontro3-18": ("pop() remove e devolve o último item da lista.", "Exemplo: removido = fila.pop()"),
    "apostila-encontro3-19": ("statistics oferece funções estatísticas prontas na biblioteca padrão.", "Exemplo: from statistics import mean"),
    "apostila-encontro3-20": ("mean() calcula a média de uma coleção numérica.", "Exemplo: mean([6, 8, 10])"),
    "apostila-encontro3-21": ("datetime contém tipos de data e hora; date.today() obtém a data local atual.", "Exemplo: from datetime import date"),
    "apostila-encontro3-22": ("O modo r abre um arquivo para leitura; encoding UTF-8 preserva textos internacionais.", 'Exemplo: open("notas.txt", "r", encoding="utf-8")'),
    "apostila-encontro3-23": ("Cada linha lida é texto; converta-a antes de adicionar à lista numérica.", 'Exemplo: float("7.5") resulta em 7.5'),
    "apostila-encontro3-24": ("math reúne funções matemáticas como raiz, arredondamento e constantes como pi.", "Exemplo: math.sqrt(16) resulta em 4.0"),
    "apostila-encontro3-25": ("date.today() fornece a data local atual para relatórios e registros.", "Exemplo: hoje = date.today()"),
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
    print("\nRoteiro baseado na apostila:")
    print("1. Portugol para Python: entrada, saída, decisões, repetição e listas.")
    print("2. Central de Sistemas: funções, validação de dados e menu interativo.")
    print("3. Recursos do Python: textos, coleções, módulos, arquivos e depuração.")
    print("Prepare o Python 3 e abra a pasta do projeto no VS Code ou no Codespaces.")

    while True:
        indice_nivel, desafio = proximo_desafio(concluidos)
        if desafio is None:
            print("\nParabéns! Você concluiu todos os níveis do curso guiado.")
            return

        nivel = NIVEIS[indice_nivel]
        total_nivel = len(nivel["desafios"])
        feitos_nivel = sum(item["id"] in concluidos for item in nivel["desafios"])
        print(f"\nNível {indice_nivel + 1}: {nivel['nome']} ({feitos_nivel}/{total_nivel})")
        if feitos_nivel == 0 and "objetivo" in nivel:
            print(f"Objetivo do encontro: {nivel['objetivo']}")
            print(f"Passo a passo: {nivel['roteiro']}")
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