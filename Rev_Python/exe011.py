#Escrever/Criar um arquivo
with open("exemplo.txt", 'w') as arquivo:
    arquivo.write("Hello World!")

#ler o arquivo
with open("exemplo.txt", 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)