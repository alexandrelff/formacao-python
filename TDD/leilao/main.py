from TDD.leilao.dominio import Usuario, Lance, Leilao, Avaliador

alexandre = Usuario('Alexandre')
stanley = Usuario('Stanley')

lance_do_Alexandre = Lance(alexandre, 100.0)
lance_do_Stanley = Lance(stanley, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_Alexandre)
leilao.lances.append(lance_do_Stanley)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance}, e o maior lance foi de {avaliador.maior_lance}')



