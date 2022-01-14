import random

def jogar():
    print("*" * 7, "Bem-vindo ao jogo de Forca!", "*" * 7)
    
    palavra_secreta = escolher_palavra_secreta()
    palavra_secreta = palavra_secreta.upper()
   
    letras_acertadas = ["_" for letra in palavra_secreta ]
    enforcou = False
    acertou = False
    erros = 0

    print("Palavra secreta -->",letras_acertadas)
    while(not enforcou and not acertou):
        chute = tentativa()
        
        if (chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            print("Você errou! Faltam {} tentativas".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou")
    else:
        print("Você perdeu!")
    print("Fim do jogo!")



def escolher_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    return palavra_secreta

def tentativa():
    chute = input("Qual a letra? ")
    return chute.strip().upper()

def marca_chute_correto(chute, palavra, letras_acertadas):
    index = 0          
    for letra in palavra:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

if (__name__ == "__main__"):
    jogar()