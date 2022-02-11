from TDD.leilao.dominio import Usuario, Leilao


#deve subtrair valor da carteira do usuário uando este propor um lance
def test_subtrair_da_carteira():
    vini = Usuario('Vini', 100)

    leilao = Leilao('Celular')

    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0
