from unittest import TestCase

from TDD.dominio import Usuario, Lance, Leilao

class TestAvaliador(TestCase):

    def setUp(self):
        self.alexandre = Usuario('Alexandre')
        self.stanley = Usuario('Stanley')

        self.lance_do_Alexandre = Lance(self.alexandre, 100.0)
        self.lance_do_Stanley = Lance(self.stanley, 150.0)

        self.leilao = Leilao('Celular')

    # teste quando adicionados lances em ordem crescente deve retornar o maior e o menor lance
    def test_lance_crescente(self):
        self.leilao.propoe(self.lance_do_Stanley)
        self.leilao.propoe(self.lance_do_Alexandre)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # teste quando adicionados lances em ordem decrescente deve retornar o maior e o menor lance
    def test_lance_decrescente(self):
        self.leilao.propoe(self.lance_do_Alexandre)
        self.leilao.propoe(self.lance_do_Stanley)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # teste quando adicionado lance único deve retornar o mesmo valor para maior e o menor lance
    def test_lance_unico(self):
        self.leilao.propoe(self.lance_do_Stanley)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    # teste quando adicionados 3 lances deve retornar o maior e o menor lance
    def test_recebendo_3_lances(self):
        lais = Usuario('Laís')

        lance_da_Lais = Lance(lais, 200.0)

        self.leilao.propoe(self.lance_do_Alexandre)
        self.leilao.propoe(self.lance_do_Stanley)
        self.leilao.propoe(lance_da_Lais)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
