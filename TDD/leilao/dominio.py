from TDD.leilao.excessoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self._valor_eh_valido(valor):
            raise LanceInvalido('Lance não é válido. Valor do lance superior ao valor da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def _valor_eh_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe(self, lance: Lance):
        if not self.lances or self.lances[-1].usuario != lance.usuario and lance.valor > self.lances[-1].valor:
            if not self.__lances:
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise LanceInvalido('Erro ao propor lance')


    @property
    def lances(self):
        return self.__lances[:]