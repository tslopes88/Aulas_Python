"""
SUITE DE TESTES UNITARIOS - CENTRAL DE ATENDIMENTO
Trabalho de Conclusao de Modulo - Escola de Programadores
Arquivo: desafio_final_testes.py
"""

import unittest
from unittest.mock import patch
from collections import deque

import desafio_final as d


class TestCentralAtendimento(unittest.TestCase):

    def setUp(self):
        """Prepara estruturas limpas para cada teste."""
        self.fila = deque()
        self.todos = []
        self.historico = []

    def _popular_cenario(self):
        """Cria o cenario de teste padrao com 4 chamados."""
        c1 = d.abrir_chamado(self.fila, self.todos, "Ana", "sem internet", 2)
        c2 = d.abrir_chamado(self.fila, self.todos, "Bruno", "tela azul", 3)
        c3 = d.abrir_chamado(self.fila, self.todos, "Carla", "trocar mouse", 1)
        c4 = d.abrir_chamado(self.fila, self.todos, "Davi", "servidor caiu", 3)
        return c1, c2, c3, c4

    # -----------------------------------------------------------------------
    # 1. Nivel 1 - Fila (FIFO)
    # -----------------------------------------------------------------------

    def test_abrir_chamado_estrutura_e_protocolo_sequencial(self):
        """Valida criacao de chamados e geracao sequencial de protocolos."""
        c1 = d.abrir_chamado(self.fila, self.todos, "Ana", "sem internet", 2)
        c2 = d.abrir_chamado(self.fila, self.todos, "Bruno", "tela azul", 3)

        self.assertEqual(c1["protocolo"], 1)
        self.assertEqual(c2["protocolo"], 2)
        self.assertEqual(c1["status"], "pendente")
        self.assertEqual(len(self.fila), 2)
        self.assertEqual(len(self.todos), 2)
        self.assertIs(self.fila[0], c1)

    def test_atender_proximo_fifo(self):
        """Valida que o primeiro da fila e o primeiro atendido (FIFO)."""
        self._popular_cenario()
        atendido = d.atender_proximo(self.fila, self.historico)
        self.assertEqual(atendido["nome"], "Ana")
        self.assertEqual(atendido["status"], "atendido")
        self.assertEqual(len(self.fila), 3)
        self.assertEqual(len(self.historico), 1)

    def test_atender_proximo_fila_vazia_retorna_none(self):
        """Atender com fila vazia devolve None."""
        self.assertIsNone(d.atender_proximo(self.fila, self.historico))

    def test_fila_um_elemento(self):
        """Abertura e atendimento com fila de apenas 1 elemento."""
        c = d.abrir_chamado(self.fila, self.todos, "Unico", "Problema", 2)
        atendido = d.atender_proximo(self.fila, self.historico)
        self.assertIs(atendido, c)
        self.assertEqual(len(self.fila), 0)

    def test_abertura_apos_atendimento_preserva_sequencia(self):
        """Protocolo incremental nao retrocede apos atendimento."""
        d.abrir_chamado(self.fila, self.todos, "C1", "D1", 1)
        d.atender_proximo(self.fila, self.historico)
        c2 = d.abrir_chamado(self.fila, self.todos, "C2", "D2", 2)
        self.assertEqual(c2["protocolo"], 2)

    # -----------------------------------------------------------------------
    # 2. Nivel 2 - Pilha (LIFO)
    # -----------------------------------------------------------------------

    def test_desfazer_atendimento_lifo(self):
        """Desfazer devolve o ultimo atendido para a FRENTE da fila."""
        self._popular_cenario()
        d.atender_proximo(self.fila, self.historico)  # Ana
        d.atender_proximo(self.fila, self.historico)  # Bruno

        desfeito = d.desfazer_atendimento(self.fila, self.historico)
        self.assertEqual(desfeito["nome"], "Bruno")
        self.assertEqual(desfeito["status"], "pendente")
        self.assertIs(self.fila[0], desfeito)
        self.assertEqual(len(self.historico), 1)

    def test_desfazer_dois_atendimentos(self):
        """Desfazer consecutivo restaura a ordem cronologica exata."""
        self._popular_cenario()
        d.atender_proximo(self.fila, self.historico)  # 1: Ana
        d.atender_proximo(self.fila, self.historico)  # 2: Bruno

        d.desfazer_atendimento(self.fila, self.historico)  # Devolve Bruno
        d.desfazer_atendimento(self.fila, self.historico)  # Devolve Ana

        self.assertEqual(self.fila[0]["nome"], "Ana")
        self.assertEqual(self.fila[1]["nome"], "Bruno")
        self.assertEqual(len(self.historico), 0)

    def test_desfazer_sem_historico_retorna_none(self):
        """Desfazer sem historico devolve None."""
        self.assertIsNone(d.desfazer_atendimento(self.fila, self.historico))

    def test_consultar_ultimo_atendido(self):
        """Consulta do topo da pilha sem desempilhar (peek)."""
        self.assertIsNone(d.consultar_ultimo_atendido(self.historico))
        self._popular_cenario()
        d.atender_proximo(self.fila, self.historico)
        ultimo = d.consultar_ultimo_atendido(self.historico)
        self.assertEqual(ultimo["nome"], "Ana")
        self.assertEqual(len(self.historico), 1)

    def test_sequencia_atender_abrir_desfazer(self):
        """Chamado desfeito volta a frente mesmo se novos chamados entraram."""
        d.abrir_chamado(self.fila, self.todos, "A1", "D1", 1)
        d.atender_proximo(self.fila, self.historico)
        d.abrir_chamado(self.fila, self.todos, "A2", "D2", 2)
        d.desfazer_atendimento(self.fila, self.historico)
        self.assertEqual([c["nome"] for c in self.fila], ["A1", "A2"])

    # -----------------------------------------------------------------------
    # 3. Nivel 3 - Ordenacao por Prioridade (Bubble Sort)
    # -----------------------------------------------------------------------

    def test_ordenar_por_prioridade_decrescente_e_estavel(self):
        """Ordena decrescente por prioridade mantendo a ordem de chegada."""
        self._popular_cenario()
        ordenados = d.ordenar_por_prioridade(self.fila)
        nomes = [c["nome"] for c in ordenados]
        self.assertEqual(nomes, ["Bruno", "Davi", "Ana", "Carla"])

    def test_ordenar_nao_altera_fila_original(self):
        """A fila original nao pode ser alterada pela ordenacao."""
        self._popular_cenario()
        nomes_antes = [c["nome"] for c in self.fila]
        d.ordenar_por_prioridade(self.fila)
        nomes_depois = [c["nome"] for c in self.fila]
        self.assertEqual(nomes_antes, nomes_depois)

    def test_ordenar_casos_borda(self):
        """Ordenacao com lista vazia, 1 elemento, ja ordenada e prioridades iguais."""
        self.assertEqual(d.ordenar_por_prioridade([]), [])

        um = [{"protocolo": 1, "prioridade": 2, "nome": "X"}]
        self.assertEqual(d.ordenar_por_prioridade(um), um)

        iguais = [
            {"protocolo": 1, "prioridade": 2, "nome": "P1"},
            {"protocolo": 2, "prioridade": 2, "nome": "P2"}
        ]
        self.assertEqual([c["nome"] for c in d.ordenar_por_prioridade(iguais)], ["P1", "P2"])

    # -----------------------------------------------------------------------
    # 4. Nivel 4 - Busca Binaria e Recursao
    # -----------------------------------------------------------------------

    def test_buscar_protocolo_busca_binaria(self):
        """Busca binaria acha elementos e devolve None para chaves inexistentes."""
        self._popular_cenario()
        self.assertEqual(d.buscar_protocolo(self.todos, 3)["nome"], "Carla")
        self.assertEqual(d.buscar_protocolo(self.todos, 1)["nome"], "Ana")
        self.assertEqual(d.buscar_protocolo(self.todos, 4)["nome"], "Davi")
        self.assertIsNone(d.buscar_protocolo(self.todos, 99))
        self.assertIsNone(d.buscar_protocolo([], 1))

    def test_buscar_protocolo_entradas_invalidas(self):
        """Busca binaria rejeita valores invalidos sem quebrar."""
        self._popular_cenario()
        for invalido in [-1, 0, 3.14, "2", None, True, False]:
            with self.subTest(invalido=invalido):
                self.assertIsNone(d.buscar_protocolo(self.todos, invalido))

    def test_contar_por_prioridade_recursivo(self):
        """Contagem recursiva correta por prioridade e lista vazia."""
        self._popular_cenario()
        self.assertEqual(d.contar_por_prioridade(self.todos, 3), 2)
        self.assertEqual(d.contar_por_prioridade(self.todos, 2), 1)
        self.assertEqual(d.contar_por_prioridade(self.todos, 1), 1)
        self.assertEqual(d.contar_por_prioridade([], 3), 0)

    def test_contar_por_prioridade_variacoes(self):
        """Contagem com 1 e 2 elementos."""
        lista = [{"prioridade": 2}, {"prioridade": 2}, {"prioridade": 1}]
        self.assertEqual(d.contar_por_prioridade(lista, 2), 2)
        self.assertEqual(d.contar_por_prioridade(lista, 3), 0)

    def test_contar_por_prioridade_limite_cpython(self):
        """Documenta que a recursao linear atinge RecursionError acima de ~1000 chamadas."""
        lista_1005 = [{"prioridade": 3} for _ in range(1005)]
        with self.assertRaises(RecursionError):
            d.contar_por_prioridade(lista_1005, 3)

    # -----------------------------------------------------------------------
    # 5. Validacoes de Entrada e Protocolo
    # -----------------------------------------------------------------------

    def test_validacao_campos_texto(self):
        """Valida que textos vazios ou preenchidos apenas com espacos sao rejeitados."""
        with self.assertRaises(ValueError):
            d.validar_texto("", "nome")
        with self.assertRaises(ValueError):
            d.validar_texto("   ", "descricao")
        with self.assertRaises(TypeError):
            d.validar_texto(123, "nome")
        self.assertEqual(d.validar_texto(" Carlos Silva "), "Carlos Silva")

    def test_validacao_prioridade(self):
        """Valida prioridades inteiras entre 1 e 3 e rejeita tipos invalidos."""
        self.assertEqual(d.validar_prioridade(1), 1)
        self.assertEqual(d.validar_prioridade(2), 2)
        self.assertEqual(d.validar_prioridade(3), 3)

        for invalido in [True, False, 0, 4, -1, 2.5, "2", None]:
            with self.subTest(invalido=invalido):
                with self.assertRaises((TypeError, ValueError)):
                    d.validar_prioridade(invalido)

    def test_protocolo_sequencial(self):
        """Gera protocolo monotonicamente sequencial baseado na quantidade total."""
        self.assertEqual(d.gerar_proximo_protocolo([]), 1)
        lista = [{"protocolo": 1}, {"protocolo": 2}, {"protocolo": 3}]
        self.assertEqual(d.gerar_proximo_protocolo(lista), 4)

    # -----------------------------------------------------------------------
    # 6. Menu Interativo e Submenu de Consulta
    # -----------------------------------------------------------------------

    @patch("sys.stdout")
    @patch("builtins.input", side_effect=["7"])
    def test_menu_encerramento_imediato(self, _mock_input, _mock_stdout):
        """Opcao 7 encerra o menu sem erros."""
        d.menu(self.fila, self.todos, self.historico)

    @patch("sys.stdout")
    @patch("builtins.input", side_effect=["abc", "99", "7"])
    def test_menu_entradas_invalidas(self, _mock_input, _mock_stdout):
        """Trata entradas invalidas no menu sem encerrar com erro."""
        d.menu(self.fila, self.todos, self.historico)

    @patch("sys.stdout")
    @patch("builtins.input", side_effect=[
        "1", "Alice", "Sem internet", "2", "",  # 1. Abrir chamado + pausa
        "2", "",                                # 2. Atender proximo + pausa
        "3", "",                                # 3. Desfazer atendimento + pausa
        "4", "1", "",                           # 4. Consultar -> 1. Ver fila + pausa
        "2", "",                                # Consultar -> 2. Ordenar por prioridade + pausa
        "3", "1", "",                           # Consultar -> 3. Buscar protocolo 1 + pausa
        "4",                                    # Consultar -> 4. Voltar ao menu principal
        "5", "",                                # 5. Relatorio geral + pausa
        "6", "6", "", "7",                      # 6. Guia -> 6. Manual completo + pausa + 7. Voltar
        "7"                                     # 7. Sair
    ])
    def test_menu_fluxo_completo(self, _mock_input, _mock_stdout):
        """Simula a navegacao completa pelo menu principal e pelo submenu de consulta."""
        d.menu(self.fila, self.todos, self.historico)
        self.assertEqual(len(self.todos), 1)
        self.assertEqual(self.todos[0]["nome"], "Alice")

    # -----------------------------------------------------------------------
    # 7. Cenario Canonico Oficial do Professor (9 Assercoes)
    # -----------------------------------------------------------------------

    def test_cenario_oficial_professor_9_requisitos(self):
        """Valida exatamente o cenario e os 9 testes originais do professor."""
        fila, todos, historico = deque(), [], []
        d.abrir_chamado(fila, todos, "Ana", "sem internet", 2)
        d.abrir_chamado(fila, todos, "Bruno", "tela azul", 3)
        d.abrir_chamado(fila, todos, "Carla", "trocar mouse", 1)
        d.abrir_chamado(fila, todos, "Davi", "servidor caiu", 3)

        # 1. Nivel 1: protocolos 1, 2, 3, 4
        self.assertEqual([c["protocolo"] for c in todos], [1, 2, 3, 4])
        self.assertEqual(len(fila), 4)

        # 2. Nivel 1: atender FIFO
        self.assertEqual(d.atender_proximo(fila, historico)["nome"], "Ana")
        self.assertEqual(d.atender_proximo(fila, historico)["nome"], "Bruno")
        self.assertEqual(len(fila), 2)
        self.assertEqual(len(historico), 2)

        # 3. Nivel 1: fila vazia
        self.assertIsNone(d.atender_proximo(deque(), []))

        # 4. Nivel 2: desfazer LIFO
        c = d.desfazer_atendimento(fila, historico)
        self.assertEqual(c["nome"], "Bruno")
        self.assertEqual(fila[0]["nome"], "Bruno")
        self.assertEqual(c["status"], "pendente")

        # 5. Nivel 2: desfazer sem historico
        self.assertIsNone(d.desfazer_atendimento(deque(), []))

        # 6. Nivel 3: ordena por prioridade (3 primeiro), estavel
        f_ord = deque(todos)
        nomes = [ch["nome"] for ch in d.ordenar_por_prioridade(f_ord)]
        self.assertEqual(nomes, ["Bruno", "Davi", "Ana", "Carla"])

        # 7. Nivel 3: nao altera fila original
        d.ordenar_por_prioridade(f_ord)
        self.assertEqual([ch["nome"] for ch in f_ord], ["Ana", "Bruno", "Carla", "Davi"])

        # 8. Nivel 4: busca binaria
        self.assertEqual(d.buscar_protocolo(todos, 3)["nome"], "Carla")
        self.assertEqual(d.buscar_protocolo(todos, 1)["nome"], "Ana")
        self.assertIsNone(d.buscar_protocolo(todos, 99))
        self.assertIsNone(d.buscar_protocolo([], 1))

        # 9. Nivel 4: contagem recursiva
        self.assertEqual(d.contar_por_prioridade(todos, 3), 2)
        self.assertEqual(d.contar_por_prioridade(todos, 1), 1)
        self.assertEqual(d.contar_por_prioridade([], 3), 0)


if __name__ == "__main__":
    unittest.main()
