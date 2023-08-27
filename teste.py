arquivo = open("palavras.txt", "r")
lista = []
for linha in arquivo:
    lista.append(linha.strip())

print(lista.__len__())