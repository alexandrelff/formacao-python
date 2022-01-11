import random

def jogar():
    numero_secreto = random.randint(1, 100)
    total_tentativas = 0
    pontos = 100

    print("*" * 7, "Bem-vindo ao jogo de adivinhação!", "*" * 7)

    print("Qual o nível de dificuldade?")
    print("1- Fácio \n2- Médio \n3- Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = int(input("Digite um valor entre 1 e 100: "))

        print("Você digitou:", chute)

        if (chute < 1 or chute > 100):
            print("Você deveria digitar um número entre 1 e 100!")
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if (maior):
                print("Errou! Seu chute foi maior que o número secreto")
            elif(menor):
                print("Errou! Seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo! O número sorteado foi:", numero_secreto)

if (__name__ == "__main__"):
    jogar()