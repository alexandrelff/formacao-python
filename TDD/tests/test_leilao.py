from unittest import TestCase

from TDD.leilao.dominio import Usuario, Lance, Leilao
from TDD.leilao.excessoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.alexandre = Usuario('Alexandre', 500.0)
        self.stanley = Usuario('Stanley', 500.0)

        self.lance_do_Alexandre = Lance(self.alexandre, 100.0)
        self.lance_do_Stanley = Lance(self.stanley, 150.0)

        self.leilao = Leilao('Celular')

    # teste quando adicionados lances em ordem crescente deve retornar o maior e o menor lance
    def test_lance_crescente(self):
        self.leilao.propoe(self.lance_do_Alexandre)
        self.leilao.propoe(self.lance_do_Stanley)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # não deve ser permitido propor lances em ordem decrescente
    def test_lance_decrescente(self):
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_Stanley)
            self.leilao.propoe(self.lance_do_Alexandre)

    # teste quando adicionado lance único deve retornar o mesmo valor para maior e o menor lance
    def test_lance_unico(self):
        self.leilao.propoe(self.lance_do_Stanley)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    # teste quando adicionados 3 lances deve retornar o maior e o menor lance
    def test_recebendo_3_lances(self):
        lais = Usuario('Laís', 500.0)

        lance_da_Lais = Lance(lais, 200.0)

        self.leilao.propoe(self.lance_do_Alexandre)
        self.leilao.propoe(self.lance_do_Stanley)
        self.leilao.propoe(lance_da_Lais)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # se o leilão não tiver lances, deve permitir propor um lance
    def test_lance_inicial(self):
        self.leilao.propoe(self.lance_do_Stanley)

        quantidade_de_lances = len(self.leilao.lances) #quantidade de lances recebidos
        self.assertEqual(1, quantidade_de_lances)

    # se o último usuário for diferente, deve permitir propor o lance
    def test_lance_com_usuarios_diferentes(self):
        self.leilao.propoe(self.lance_do_Alexandre)
        self.leilao.propoe(self.lance_do_Stanley)

        quantidade_de_lances = len(self.leilao.lances) #quantidade de lances recebidos
        self.assertEqual(2, quantidade_de_lances)

    # se o último usuário for o mesmo, não deve permitir propor o lance
    def test_lances_mesmo_usuario(self):
        lance2_do_Alexandre = Lance(self.alexandre, 200.0)
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_Alexandre)
            self.leilao.propoe(lance2_do_Alexandre)
