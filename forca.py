import random

print("*******************************")
print("Seja bem vindo ao jogo da forca")
print("*******************************")

arquivo = open("palavras.txt", "r")
palavras = []

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

arquivo.close()

numero = random.randrange(0,len(palavras))
palavra_secreta = palavras[numero].upper()

letras_acertadas = ["_" for letra in palavra_secreta]


enforcou = False
acertou = False
erros = 0

print(letras_acertadas)

while(not enforcou and not acertou):

    chute = input("Digite uma letra!")
    chute = chute.strip().upper()

    if( chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
               letras_acertadas[index] = letra
            index = index + 1
    else:
        erros = erros + 1

    enforcou = erros == 5
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

if(acertou):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
else:
    print("Você perdeu! A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/          ")