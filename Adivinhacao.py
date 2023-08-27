import random
def jogar():
    # função de Mensagem de boas vindas
    def boas_vindas():
        print("\n********************************")
        print("Bem vindo ao jogo de Adivinhação")
        print("********************************")
        
    boas_vindas()

    # game - funcionalidades
    numero_secreto = random.randrange(1 , 101)
    print(f"Numero secreto: {numero_secreto}")


    quantidade_tentativas = 0
    pontos = 1000


    print("Qual nível de dificuldade ?")
    print("(1) Fácil - (2) Médio - (3) Difícil")
    nivel = int(input("Selecione o Nível: "))



    if (nivel == 1):
        quantidade_tentativas = 8
    elif (nivel == 2):
        quantidade_tentativas = 6
    elif(nivel == 3):
        quantidade_tentativas = 3
    else:
        print("Essa opção não está no menu! Digite uma opção válida.")

    for tentativas in range(1, quantidade_tentativas + 1):
        
        print(f"\nTentativa: {tentativas} de {quantidade_tentativas}\n")
        
        chute = int(input("Digite um numero entre 1 a 100: "))
        print(f"Voce digitou: {chute}")
        
        if (chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 a 100.")
            continue

        # Verificações
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        # Condições
        if (acertou):
            print(f"Voce acertou! Na {tentativas}° tentativa e fez * {pontos} * pontos.")
            break
        else:
            
            if (maior):
                print("Voce errou! Seu chute foi maior que o numero secreto.")
            elif (menor):
                print("Voce errou! Seu chute foi menor que o numero secreto.")
            
            pontos_perdidos = abs(numero_secreto - chute)
            
            pontos -= pontos_perdidos
        
        
                
        


    print("\nFim do jogo")


if(__name__ == "__main__"):
    jogar()


    







