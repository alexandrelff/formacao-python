from TDD.leilao.dominio import Usuario, Leilao
import pytest

from TDD.leilao.excessoes import LanceInvalido


@pytest.fixture
def vini():
    return Usuario('vini', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')

#deve subtrair valor da carteira do usuário quando este propor um lance
def test_subtrair_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0

#deve permitir propor o lance quando o valor for menor que o valor da carteira
def test_lance_menor_que_valor_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 90.0)

    assert vini.carteira == 10.0

#deve permitir propor o lance quando o valor for igual ao valor da carteira
def test_lance_igual_ao_valor_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.0

#não deve permitir propor lance maior que o valor da carteira
def test_lance_maior_que_valor_da_carteira(vini, leilao):
    with pytest.raises(LanceInvalido):
        vini.propoe_lance(leilao, 200.0)

        assert vini.carteira == 100.0