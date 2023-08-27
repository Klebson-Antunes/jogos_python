import random

def jogar():
  
    imprime_mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    acertou = False
    enforcou = False
    tentativas = 0
    
    while( not enforcou and not acertou):
        chute = solicita_chute()
        if(chute in palavra_secreta):
           marca_chute(palavra_secreta, letras_acertadas, chute)
        else:
            tentativas += 1
            desenha_forca(tentativas)  
            
        enforcou = tentativas == palavra_secreta.__len__()
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
        
        
    if(acertou):
        imprime_mensagem_vitoria()
    else:
        imprime_mensagem_derrota(palavra_secreta)
               
    print("Fim do Jogo")  
# desenha a forca de acordo com erros  
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
   
# mensagem de derrota
def imprime_mensagem_derrota(palavra_secreta):
    print("\nPoxa, você foi enforcado!")
    print("A palavra era '{}'".format(palavra_secreta))
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
    print("       \_______/           ")

# mensagem de vitoria
def imprime_mensagem_vitoria():
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

# marca um chute se acertado
def marca_chute(palavra_secreta, letras_acertadas, chute):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

# inicia as letras acertadas  
def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]    

# solicita um chute ao usuario e devolve o chute  
def solicita_chute():
    chute = input("\nDigite uma letra: ")
    chute = chute.strip().upper()
    return chute           
 
# função que devolvebuma palavra secreta
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    lista_palavras = []
    for linha in arquivo:
        lista_palavras.append(linha.strip())
    arquivo.close()

    palavra_secreta_aleatoria = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[palavra_secreta_aleatoria].upper()
    return palavra_secreta
 
 # função de Mensagem de boas vindas
def imprime_mensagem_de_abertura():
    print("\n***************************")
    print("Bem vindo ao jogo de Forca")
    print("***************************")
 
# executa o arquivo forca 
if(__name__ == "__main__"):
    jogar()