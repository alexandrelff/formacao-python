import adivinhacao
import forca

print("*" * 7, "Escolha o seu jogo", "*" * 7)


print("1- Forca \n2- Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando Adivinhação")
    adivinhacao.jogar()