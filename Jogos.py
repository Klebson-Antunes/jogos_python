import Adivinhacao
import Forca
# função de Mensagem de boas vindas
def boas_vindas():
    print("\n***************")
    print("Escolha o jogo")
    print("***************")
    
boas_vindas()

print("(1) Forca - (2) Adivinhação")
jogo = int(input("Digite a opção do jogo que irá jogar: "))

if jogo == 1:
    Forca.jogar()
elif jogo == 2:
    Adivinhacao.jogar()
else:
    print("Digite uma opção valida! 1 ou 2.")