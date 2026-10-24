import os
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

import curso_guiado
import menu_exercicios


class TestProjetoPython(unittest.TestCase):
    def test_registro_por_nivel(self):
        self.assertIn("iniciante", menu_exercicios.EXERCICIOS_POR_NIVEL)
        self.assertIn("intermediario", menu_exercicios.EXERCICIOS_POR_NIVEL)
        self.assertIn("avancado", menu_exercicios.EXERCICIOS_POR_NIVEL)

    def test_listar_exercicios(self):
        iniciante = menu_exercicios.listar_exercicios_por_nivel("iniciante")
        self.assertTrue(iniciante)
        self.assertTrue(any(item["arquivo"] == "boas_vindas.py" for item in iniciante))

    def test_registrar_progresso(self):
        with tempfile.TemporaryDirectory() as tmp:
            arquivo = os.path.join(tmp, "progresso.json")
            ok = menu_exercicios.registrar_progresso("loteria.py", arquivo=arquivo)
            self.assertTrue(ok)
            self.assertTrue(os.path.exists(arquivo))

    def test_curso_guiado_valida_resposta(self):
        desafio = curso_guiado.NIVEIS[0]["desafios"][2]
        self.assertTrue(curso_guiado.resposta_correta(" print(nome) ", desafio))
        self.assertFalse(curso_guiado.resposta_correta("print(outra)", desafio))

    def test_todos_os_desafios_guiados_tem_aula(self):
        ids_desafios = {
            desafio["id"]
            for nivel in curso_guiado.NIVEIS
            for desafio in nivel["desafios"]
        }
        self.assertEqual(ids_desafios, set(curso_guiado.AULAS_DESAFIOS))

    def test_encontros_da_apostila_tem_objetivo_e_roteiro(self):
        encontros = [
            nivel for nivel in curso_guiado.NIVEIS
            if nivel["nome"].startswith("Encontro ")
        ]
        self.assertEqual(len(encontros), 3)
        self.assertEqual(sum(len(nivel["desafios"]) for nivel in curso_guiado.NIVEIS), 60)
        for encontro in encontros:
            self.assertTrue(encontro["objetivo"])
            self.assertTrue(encontro["roteiro"])
            self.assertTrue(encontro["desafios"])

    def test_curso_guiado_desbloqueia_nivel_seguinte(self):
        primeiro_nivel = curso_guiado.NIVEIS[0]["desafios"]
        concluidos = {desafio["id"] for desafio in primeiro_nivel}
        indice, desafio = curso_guiado.proximo_desafio(concluidos)
        self.assertEqual(indice, 1)
        self.assertEqual(desafio["id"], curso_guiado.NIVEIS[1]["desafios"][0]["id"])

    def test_curso_guiado_preserva_progresso_ate_nivel_avancado(self):
        concluidos = {
            desafio["id"]
            for nivel in curso_guiado.NIVEIS[:3]
            for desafio in nivel["desafios"]
        }
        indice, desafio = curso_guiado.proximo_desafio(concluidos)
        self.assertEqual(indice, 3)
        self.assertEqual(desafio["id"], "avancado-01")

    def test_curso_guiado_salva_progresso(self):
        with tempfile.TemporaryDirectory() as tmp:
            arquivo = os.path.join(tmp, "curso.json")
            concluidos = {"fundamentos-01", "fundamentos-02"}
            curso_guiado.salvar_progresso(concluidos, arquivo)
            self.assertEqual(curso_guiado.carregar_progresso(arquivo), concluidos)

    def test_curso_guiado_completo_com_dica_e_nova_tentativa(self):
        respostas = []
        for indice, nivel in enumerate(curso_guiado.NIVEIS):
            for desafio_indice, desafio in enumerate(nivel["desafios"]):
                respostas.append("")
                if indice == 0 and desafio_indice == 0:
                    respostas.extend(["/dica", "resposta incorreta"])
                respostas.append(desafio["respostas"][0])
        saida = StringIO()

        with patch("curso_guiado.carregar_progresso", return_value=set()), patch(
            "curso_guiado.salvar_progresso"
        ) as salvar, patch("builtins.input", side_effect=respostas), redirect_stdout(saida):
            curso_guiado.iniciar_curso_guiado()

        total_desafios = sum(len(nivel["desafios"]) for nivel in curso_guiado.NIVEIS)
        self.assertEqual(salvar.call_count, total_desafios)
        self.assertIn("Dica:", saida.getvalue())
        self.assertEqual(saida.getvalue().count("AULA RÁPIDA"), total_desafios)
        self.assertIn("Roteiro baseado na apostila", saida.getvalue())
        self.assertIn("Objetivo do encontro:", saida.getvalue())
        self.assertIn("Passo a passo:", saida.getvalue())
        self.assertIn("Parabéns!", saida.getvalue())


if __name__ == "__main__":
    unittest.main()
